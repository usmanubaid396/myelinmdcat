import { initializeApp } from 'https://www.gstatic.com/firebasejs/10.13.0/firebase-app.js';
import { getAuth, signInWithPopup, GoogleAuthProvider, signOut, onAuthStateChanged } from 'https://www.gstatic.com/firebasejs/10.13.0/firebase-auth.js';
import { getFirestore, doc, setDoc, getDocs, getDoc, collection, onSnapshot, query, orderBy, limit, getDocFromServer } from 'https://www.gstatic.com/firebasejs/10.13.0/firebase-firestore.js';
import * as d3 from 'https://cdn.jsdelivr.net/npm/d3@7/+esm';

// DOM selector helper (hoisted)
function $(s) {
  return document.querySelector(s);
}

// Firebase Configuration from firebase-applet-config.json
export const firebaseConfig = {
  projectId: "versatile-sunspot-zk91c",
  appId: "1:44456574606:web:66e02338fec79a0ad253df",
  apiKey: "AIzaSyBHRxHOysAD7rXPSikHerpe8YzVpQYjiHM",
  authDomain: "versatile-sunspot-zk91c.firebaseapp.com",
  firestoreDatabaseId: "ai-studio-myelinmdcat-4aca1bdb-6839-4ce4-bbea-e238bce1a747",
  storageBucket: "versatile-sunspot-zk91c.firebasestorage.app",
  messagingSenderId: "44456574606",
  measurementId: "",
  oAuthClientId: "44456574606-kql19k4d6j6g844t605cb4f09c9qm0s8.apps.googleusercontent.com",
  recaptchaSiteKey: ""
};

// Initialize Firebase
const firebaseApp = initializeApp(firebaseConfig);
export const db = getFirestore(firebaseApp, firebaseConfig.firestoreDatabaseId); /* CRITICAL: The app will break without this line */
export const auth = getAuth(firebaseApp);

// Connection test on boot
async function testConnection() {
  try {
    await getDocFromServer(doc(db, 'test', 'connection'));
  } catch (error) {
    if (error instanceof Error && error.message.includes('the client is offline')) {
      console.error("Please check your Firebase configuration.");
    }
  }
}
testConnection();

// Standardized Firestore Error Handler
const OperationType = {
  CREATE: 'create',
  UPDATE: 'update',
  DELETE: 'delete',
  LIST: 'list',
  GET: 'get',
  WRITE: 'write',
};

function handleFirestoreError(error, operationType, path) {
  const errInfo = {
    error: error instanceof Error ? error.message : String(error),
    authInfo: {
      userId: auth.currentUser?.uid,
      email: auth.currentUser?.email,
      emailVerified: auth.currentUser?.emailVerified,
      isAnonymous: auth.currentUser?.isAnonymous,
      tenantId: auth.currentUser?.tenantId,
      providerInfo: auth.currentUser?.providerData?.map(provider => ({
        providerId: provider.providerId,
        email: provider.email,
      })) || []
    },
    operationType,
    path
  };
  console.error('Firestore Error: ', JSON.stringify(errInfo));
  throw new Error(JSON.stringify(errInfo));
}

// Google Auth Provider setup
const googleProvider = new GoogleAuthProvider();
googleProvider.setCustomParameters({ prompt: 'select_account' });

async function loginWithGoogle() {
  const loginBtn = $('#google-login-btn');
  if (loginBtn) {
    loginBtn.disabled = true;
    loginBtn.style.opacity = '0.7';
  }

  try {
    const result = await signInWithPopup(auth, googleProvider);
    const user = result.user;
    if (user) {
      const userRef = doc(db, 'users', user.uid);
      try {
        await setDoc(userRef, {
          userId: user.uid,
          email: user.email || '',
          displayName: user.displayName || 'MDCAT Aspirant',
          photoURL: user.photoURL || '',
          updatedAt: new Date().toISOString()
        }, { merge: true });
      } catch (err) {
        handleFirestoreError(err, OperationType.WRITE, 'users/' + user.uid);
      }
      await syncSessionsFromFirestore(user.uid);
    }
  } catch (error) {
    const errCode = error?.code || '';
    const errMsg = error?.message || '';

    // Benign user cancellations: user intentionally dismissed or closed the OAuth popup
    if (
      errCode === 'auth/popup-closed-by-user' ||
      errCode === 'auth/cancelled-popup-request' ||
      errCode === 'auth/user-cancelled' ||
      errMsg.includes('auth/popup-closed-by-user') ||
      errMsg.includes('auth/cancelled-popup-request')
    ) {
      console.info('Google Sign-In: Popup closed by user.');
      return;
    }

    // Popup blocker alert
    if (errCode === 'auth/popup-blocked' || errMsg.includes('auth/popup-blocked')) {
      console.warn('Google Sign-In popup was blocked by browser settings.');
      return;
    }

    console.error('Google Sign-In unexpected error:', error);
  } finally {
    if (loginBtn) {
      loginBtn.disabled = false;
      loginBtn.style.opacity = '1';
    }
  }
}

async function logoutUser() {
  try {
    await signOut(auth);
  } catch (error) {
    console.error('Logout error:', error);
  }
}

// Sync saved sessions from Firestore cloud
async function syncSessionsFromFirestore(userId) {
  if (!userId) return;
  const path = `users/${userId}/sessions`;
  try {
    const sessionsCol = collection(db, 'users', userId, 'sessions');
    const snapshot = await getDocs(sessionsCol);
    snapshot.forEach(docSnap => {
      const data = docSnap.data();
      if (data && data.paperKey) {
        const localKey = 'myelin-session:' + data.paperKey;
        // Merge or populate if not present locally
        const existing = localStorage.getItem(localKey);
        if (!existing) {
          localStorage.setItem(localKey, JSON.stringify({
            key: data.paperKey,
            path: data.paperKey.startsWith('paper:') ? `#/past-papers/${data.paperKey.split(':')[1]}` : '#/practice',
            title: data.title || '',
            kicker: '',
            currentIndex: data.currentIndex || 0,
            currentExamSubject: 'All',
            timerSeconds: data.timerSeconds || 0,
            totalQuestions: data.totalQuestions || 200,
            completed: !!data.completed,
            lastUpdated: Date.now()
          }));
        }
      }
    });
    run();
  } catch (err) {
    console.warn('Firestore session sync notice:', err);
  }
}

// Listen to Auth State
onAuthStateChanged(auth, async user => {
  const loginBtn = $('#google-login-btn');
  const userBadge = $('#user-profile-badge');
  const userAvatar = $('#user-avatar');
  const userName = $('#user-display-name');

  if (user) {
    if (loginBtn) loginBtn.hidden = true;
    if (userBadge) userBadge.hidden = false;
    if (userAvatar) {
      userAvatar.src = user.photoURL || 'https://www.gstatic.com/images/branding/product/1x/avatar_square_blue_512dp.png';
      userAvatar.alt = user.displayName || 'User Avatar';
    }
    if (userName) {
      userName.textContent = user.displayName || user.email?.split('@')[0] || 'Student';
    }
    await syncSessionsFromFirestore(user.uid);
  } else {
    if (loginBtn) loginBtn.hidden = false;
    if (userBadge) userBadge.hidden = true;
  }
  if (typeof run === 'function') run();
  if (typeof loadPracticeDashboard === 'function') loadPracticeDashboard();
});

// Attach login/logout button handlers
const authLoginBtn = $('#google-login-btn');
if (authLoginBtn) authLoginBtn.onclick = () => loginWithGoogle();

const authLogoutBtn = $('#google-logout-btn');
if (authLogoutBtn) authLogoutBtn.onclick = () => logoutUser();

const dashRefBtn = $('#btn-dashboard-refresh');
if (dashRefBtn) dashRefBtn.onclick = () => loadPracticeDashboard();

// Core Application Logic
const S = { q: [], sub: 'All' };

// Answer state & flags stored in LocalStorage
let answers = {};
try { answers = JSON.parse(localStorage.getItem('myelin-answers') || '{}'); } catch {}

let flagged = {};
try { flagged = JSON.parse(localStorage.getItem('myelin-flagged') || '{}'); } catch {}

function key(x) {
  return x.year + ':' + (x.id || x.stem);
}

function sanitizeDocId(k) {
  return String(k || '').replace(/[^a-zA-Z0-9_\-]/g, '_');
}

function esc(s) {
  return String(s || '').replace(/[&<>"']/g, c => ({
    '&': '&amp;', '<': '&lt;', '>': '&gt;', '"': '&quot;', "'": '&#39;'
  }[c]));
}

// Timer management
let timerInterval = null, timerSeconds = 0, timerRunning = false, activeSetKey = '';

// Challenge Mode State
let isChallengeMode = false;
let activeChallenge = null;
let challengeTimeLimit = 300; // seconds
let currentLeaderboardUnsub = null;
let cachedChallenges = [];
let selectedChallengeId = null;

function fmtTime(s) {
  const m = Math.floor(s / 60), sec = s % 60;
  if (m >= 60) {
    const h = Math.floor(m / 60), remM = m % 60;
    return String(h).padStart(2, '0') + ':' + String(remM).padStart(2, '0') + ':' + String(sec).padStart(2, '0');
  }
  return String(m).padStart(2, '0') + ':' + String(sec).padStart(2, '0');
}

function updateTimerUI() {
  const d = $('#timer-display');
  const timerCard = $('#practice-timer');
  const timerLabel = timerCard?.querySelector('.timer-label');
  const toggleBtn = $('#timer-toggle-btn');
  const resetBtn = $('#timer-reset-btn');

  if (isChallengeMode && activeChallenge) {
    if (timerLabel) timerLabel.textContent = 'Remaining:';
    if (toggleBtn) toggleBtn.style.display = 'none';
    if (resetBtn) resetBtn.style.display = 'none';

    const rem = Math.max(0, challengeTimeLimit - timerSeconds);
    if (d) d.textContent = fmtTime(rem);

    if (timerCard) {
      timerCard.classList.remove('timer-urgency-warning', 'timer-urgency-critical');
      if (rem <= 30) {
        timerCard.classList.add('timer-urgency-critical');
      } else if (rem <= 60) {
        timerCard.classList.add('timer-urgency-warning');
      }
    }

    if (rem <= 0 && timerRunning) {
      stopTimer();
      handleChallengeTimeOut();
    }
  } else {
    if (timerLabel) timerLabel.textContent = 'Time:';
    if (toggleBtn) toggleBtn.style.display = '';
    if (resetBtn) resetBtn.style.display = '';
    if (timerCard) timerCard.classList.remove('timer-urgency-warning', 'timer-urgency-critical');
    if (d) d.textContent = fmtTime(timerSeconds);
    if (toggleBtn) {
      toggleBtn.textContent = timerRunning ? '⏸' : '▶';
      toggleBtn.setAttribute('aria-label', timerRunning ? 'Pause timer' : 'Resume timer');
      toggleBtn.setAttribute('title', timerRunning ? 'Pause timer' : 'Resume timer');
    }
  }
}

function handleChallengeTimeOut() {
  const modal = $('#challenge-times-up-modal');
  if (modal) {
    modal.hidden = false;
  } else {
    submitExam();
  }
}

function startTimer() {
  if (timerInterval) clearInterval(timerInterval);
  timerRunning = true;
  updateTimerUI();
  timerInterval = setInterval(() => {
    if (timerRunning) {
      timerSeconds++;
      updateTimerUI();
      // Periodically persist elapsed timer every 5 seconds
      if (timerSeconds % 5 === 0 && !isChallengeMode) {
        saveSessionState(false);
      }
    }
  }, 1000);
}

function stopTimer() {
  if (timerInterval) {
    clearInterval(timerInterval);
    timerInterval = null;
  }
  timerRunning = false;
  updateTimerUI();
  if (!isChallengeMode) {
    saveSessionState(false);
  }
}

function resetTimer() {
  timerSeconds = 0;
  updateTimerUI();
  if (!isChallengeMode) {
    saveSessionState(false);
  }
}

// CBT Exam State
let examQuestions = [];
let currentExamIndex = 0;
let currentExamSubject = 'All';
let examTitle = '';
let examKicker = '';

// LocalStorage + Firestore Auto-save Engine
async function saveSessionToFirestore(sessionData) {
  if (!auth.currentUser) return;
  const userId = auth.currentUser.uid;
  const docId = sanitizeDocId(sessionData.key);
  const path = `users/${userId}/sessions/${docId}`;
  try {
    const payload = {
      sessionId: docId,
      userId: userId,
      paperKey: sessionData.key,
      title: sessionData.title,
      currentIndex: sessionData.currentIndex,
      timerSeconds: sessionData.timerSeconds,
      totalQuestions: sessionData.totalQuestions,
      completed: !!sessionData.completed,
      updatedAt: new Date().toISOString()
    };
    if (typeof sessionData.accuracy === 'number') {
      payload.accuracy = sessionData.accuracy;
    }
    if (typeof sessionData.attemptedCount === 'number') {
      payload.attemptedCount = sessionData.attemptedCount;
    }
    if (sessionData.completedAt) {
      payload.completedAt = sessionData.completedAt;
    }
    await setDoc(doc(db, 'users', userId, 'sessions', docId), payload, { merge: true });
  } catch (err) {
    console.warn('Firestore session write caught:', err);
  }
}

function saveSessionState(showFlash = true) {
  if (!activeSetKey || !examQuestions.length) return;
  const sessionData = {
    key: activeSetKey,
    path: location.hash,
    title: examTitle,
    kicker: examKicker,
    currentIndex: currentExamIndex,
    currentExamSubject: currentExamSubject,
    timerSeconds: timerSeconds,
    totalQuestions: examQuestions.length,
    completed: false,
    lastUpdated: Date.now()
  };

  try {
    localStorage.setItem('myelin-session:' + activeSetKey, JSON.stringify(sessionData));
    localStorage.setItem('myelin-last-session', JSON.stringify(sessionData));
  } catch (err) {
    console.warn('LocalStorage save failed:', err);
  }

  // Also push to Firestore if authenticated
  saveSessionToFirestore(sessionData);

  if (showFlash) {
    const status = $('#autosave-status');
    if (status) {
      status.classList.add('saving');
      setTimeout(() => status.classList.remove('saving'), 500);
    }
  }
}

// Persist on tab close, refresh or page navigation
window.addEventListener('beforeunload', () => saveSessionState(false));
window.addEventListener('pagehide', () => saveSessionState(false));

function getSubjectClass(sub) {
  const s = (sub || '').toLowerCase();
  if (s.includes('bio')) return 'bio';
  if (s.includes('chem')) return 'chem';
  if (s.includes('phy')) return 'phy';
  if (s.includes('eng')) return 'eng';
  if (s.includes('logic')) return 'lr';
  return 'bio';
}

function updateOverallProgress() {
  if (!examQuestions.length) return;
  const total = examQuestions.length;
  const doneCount = examQuestions.filter(x => answers[key(x)]).length;
  const flagCount = examQuestions.filter(x => flagged[key(x)]).length;
  const unattempted = total - doneCount;
  const pct = Math.round((doneCount / total) * 100);

  const fill = $('#progress-bar-fill');
  const bar = $('#progress-bar');
  const stats = $('#progress-stats');
  if (fill) fill.style.width = pct + '%';
  if (bar) bar.setAttribute('aria-valuenow', pct);
  if (stats) stats.textContent = `${doneCount} of ${total} completed (${pct}%)`;

  const qCount = $('#question-count');
  if (qCount) {
    qCount.textContent = `${doneCount} / ${total} attempted (${pct}%) · Auto-saved locally & cloud · PMDC syllabus verified`;
  }

  const indA = $('#ind-answered');
  const indF = $('#ind-flagged');
  const indU = $('#ind-unattempted');
  if (indA) indA.textContent = doneCount;
  if (indF) indF.textContent = flagCount;
  if (indU) indU.textContent = unattempted;

  const palCount = $('#palette-summary-count');
  if (palCount) palCount.textContent = `${doneCount}/${total}`;
}

function renderSubjectStrip() {
  const strip = $('#exam-subject-strip');
  if (!strip) return;

  const subjects = ['All', ...new Set(examQuestions.map(q => q.subject).filter(Boolean))];
  if (subjects.length <= 2 && subjects[0] === 'All') {
    strip.innerHTML = '';
    strip.hidden = true;
    return;
  }
  strip.hidden = false;

  strip.innerHTML = subjects.map(sub => {
    const count = sub === 'All' ? examQuestions.length : examQuestions.filter(q => q.subject === sub).length;
    const subCls = sub === 'All' ? '' : 'subject-' + getSubjectClass(sub);
    const activeCls = sub === currentExamSubject ? 'active' : '';
    return `<button type="button" class="exam-subject-tab ${subCls} ${activeCls}" data-exam-sub="${esc(sub)}">
      ${esc(sub)} (${count})
    </button>`;
  }).join('');

  strip.querySelectorAll('[data-exam-sub]').forEach(btn => {
    btn.onclick = () => {
      const selected = btn.dataset.examSub;
      currentExamSubject = selected;
      if (selected !== 'All') {
        const firstIdx = examQuestions.findIndex(q => q.subject === selected);
        if (firstIdx !== -1) currentExamIndex = firstIdx;
      }
      saveSessionState(false);
      renderSubjectStrip();
      renderActiveQuestion();
      renderQuestionPalette();
    };
  });
}

function renderQuestionPalette() {
  const grid = $('#palette-grid');
  if (!grid) return;

  grid.innerHTML = examQuestions.map((q, idx) => {
    const isAnswered = !!answers[key(q)];
    const isFlagged = !!flagged[key(q)];
    const isCurrent = idx === currentExamIndex;

    let cls = ['palette-btn'];
    if (isCurrent) cls.push('current');
    if (isAnswered) cls.push('answered');
    if (isFlagged) cls.push('flagged');

    const flagIcon = isFlagged ? '<span style="font-size:8px;position:absolute;top:1px;right:2px">⚑</span>' : '';

    return `<button type="button" class="${cls.join(' ')}" data-jump-q="${idx}" aria-label="Question ${idx + 1}">
      ${flagIcon}<span>${idx + 1}</span>
    </button>`;
  }).join('');

  grid.querySelectorAll('[data-jump-q]').forEach(btn => {
    btn.onclick = () => {
      currentExamIndex = Number(btn.dataset.jumpQ);
      saveSessionState(false);
      renderActiveQuestion();
      renderQuestionPalette();
      $('#question-palette').classList.remove('open');
    };
  });
}

function renderActiveQuestion() {
  const qList = $('#question-list');
  if (!qList || !examQuestions.length) return;

  const q = examQuestions[currentExamIndex];
  if (!q) return;

  const qKey = key(q);
  const selectedAns = answers[qKey];
  const isFlagged = !!flagged[qKey];
  const subCls = getSubjectClass(q.subject);

  let opts = [];
  if (Array.isArray(q.options) && q.options.length) {
    opts = q.options.map(o => ({ label: o.label || 'A', text: o.text || '' }));
  } else if (Array.isArray(q.a) && q.a.length) {
    opts = q.a.map(item => ({ label: item[1] || item[0], text: item[2] || item[1] }));
  }

  const stemText = q.stem.replace(/^Q\.\d+\.\s*/, '').replace(/^[0-9]+\.\s*/, '');

  qList.innerHTML = `
    <article class="exam-q-inner" role="region" aria-label="Question ${currentExamIndex + 1}">
      <div class="exam-q-header">
        <div class="exam-q-badges">
          <span class="q-num-pill">Question ${currentExamIndex + 1} of ${examQuestions.length}</span>
          <span class="q-subject-pill ${subCls}">${esc(q.subject)}</span>
          ${q.unit ? `<span class="q-topic-pill">${esc(q.unit)}</span>` : ''}
          ${q.topic ? `<span class="q-topic-pill muted">${esc(q.topic)}</span>` : ''}
        </div>
        <button type="button" id="card-flag-btn" class="exam-flag-btn ${isFlagged ? 'flagged' : ''}" aria-pressed="${isFlagged}">
          <span>${isFlagged ? '⚑ Flagged' : '⚐ Flag for Review'}</span>
        </button>
      </div>

      <div class="exam-q-stem">${esc(stemText)}</div>

      <div class="exam-options-stack" role="radiogroup" aria-label="Choices for Question ${currentExamIndex + 1}">
        ${opts.map(opt => {
          const isSelected = selectedAns === opt.label;
          return `
            <button type="button" class="exam-opt-btn ${isSelected ? 'selected' : ''}" data-opt-label="${esc(opt.label)}" role="radio" aria-checked="${isSelected}">
              <span class="exam-opt-letter">${esc(opt.label)}</span>
              <span class="exam-opt-text">${esc(opt.text)}</span>
            </button>
          `;
        }).join('')}
      </div>
    </article>
  `;

  // Attach card option handlers
  qList.querySelectorAll('[data-opt-label]').forEach(btn => {
    btn.onclick = () => {
      const chosen = btn.dataset.optLabel;
      answers[qKey] = chosen;
      try { localStorage.setItem('myelin-answers', JSON.stringify(answers)); } catch {}
      saveSessionState(true);
      renderActiveQuestion();
      updateOverallProgress();
      renderQuestionPalette();
    };
  });

  // Attach card flag toggle
  const cardFlagBtn = $('#card-flag-btn');
  if (cardFlagBtn) {
    cardFlagBtn.onclick = () => toggleFlagCurrent();
  }

  // Update bottom controls
  const btnPrev = $('#btn-prev');
  if (btnPrev) btnPrev.disabled = (currentExamIndex === 0);

  const btnNext = $('#btn-next');
  if (btnNext) {
    if (currentExamIndex === examQuestions.length - 1) {
      btnNext.innerHTML = 'Review & Finish 🏁';
    } else {
      btnNext.innerHTML = 'Next ▶';
    }
  }

  const flagActionBtn = $('#btn-flag');
  if (flagActionBtn) {
    flagActionBtn.textContent = isFlagged ? '⚑ Marked for Review' : '⚐ Mark for Review';
    flagActionBtn.className = 'button secondary exam-flag-btn ' + (isFlagged ? 'flagged' : '');
  }

  // Ensure current question in palette is visible
  const activePalBtn = $(`[data-jump-q="${currentExamIndex}"]`);
  if (activePalBtn && activePalBtn.scrollIntoView) {
    activePalBtn.scrollIntoView({ block: 'nearest', behavior: 'smooth' });
  }
}

function toggleFlagCurrent() {
  if (!examQuestions.length) return;
  const q = examQuestions[currentExamIndex];
  const qKey = key(q);
  if (flagged[qKey]) {
    delete flagged[qKey];
  } else {
    flagged[qKey] = true;
  }
  try { localStorage.setItem('myelin-flagged', JSON.stringify(flagged)); } catch {}
  saveSessionState(true);
  renderActiveQuestion();
  updateOverallProgress();
  renderQuestionPalette();
}

function clearAnswerCurrent() {
  if (!examQuestions.length) return;
  const q = examQuestions[currentExamIndex];
  const qKey = key(q);
  delete answers[qKey];
  try { localStorage.setItem('myelin-answers', JSON.stringify(answers)); } catch {}
  saveSessionState(true);
  renderActiveQuestion();
  updateOverallProgress();
  renderQuestionPalette();
}

function nextQuestion() {
  if (currentExamIndex < examQuestions.length - 1) {
    currentExamIndex++;
    saveSessionState(false);
    renderActiveQuestion();
    renderQuestionPalette();
  } else {
    openFinishModal();
  }
}

function prevQuestion() {
  if (currentExamIndex > 0) {
    currentExamIndex--;
    saveSessionState(false);
    renderActiveQuestion();
    renderQuestionPalette();
  }
}

function openFinishModal() {
  const total = examQuestions.length;
  const doneCount = examQuestions.filter(x => answers[key(x)]).length;
  const flagCount = examQuestions.filter(x => flagged[key(x)]).length;
  const unattempted = total - doneCount;

  const modal = $('#exam-confirm-modal');
  const summaryText = $('#modal-summary-text');
  if (summaryText) {
    summaryText.innerHTML = `
      You have attempted <strong>${doneCount}</strong> out of <strong>${total}</strong> questions.<br>
      • <strong>${unattempted}</strong> questions remain unanswered.<br>
      • <strong>${flagCount}</strong> questions marked for review.<br><br>
      Are you ready to finish and submit your paper?
    `;
  }
  if (modal) modal.hidden = false;
}

function closeFinishModal() {
  const modal = $('#exam-confirm-modal');
  if (modal) modal.hidden = true;
}

function submitExam() {
  closeFinishModal();
  stopTimer();

  const total = examQuestions.length;
  const doneCount = examQuestions.filter(x => answers[key(x)]).length;
  const pct = total > 0 ? Math.round((doneCount / total) * 100) : 0;
  const timeTaken = isChallengeMode ? Math.min(timerSeconds, challengeTimeLimit) : timerSeconds;

  // Mark session as completed in LocalStorage and Firestore
  if (activeSetKey && !isChallengeMode) {
    try {
      const raw = localStorage.getItem('myelin-session:' + activeSetKey);
      if (raw) {
        const s = JSON.parse(raw);
        s.completed = true;
        s.timerSeconds = timeTaken;
        s.accuracy = pct;
        s.attemptedCount = doneCount;
        s.completedAt = new Date().toISOString();
        localStorage.setItem('myelin-session:' + activeSetKey, JSON.stringify(s));
        saveSessionToFirestore(s);
      }
      const lastRaw = localStorage.getItem('myelin-last-session');
      if (lastRaw) {
        const last = JSON.parse(lastRaw);
        if (last.key === activeSetKey) {
          last.completed = true;
          last.accuracy = pct;
          last.attemptedCount = doneCount;
          last.completedAt = new Date().toISOString();
          localStorage.setItem('myelin-last-session', JSON.stringify(last));
        }
      }
    } catch {}
    loadPracticeDashboard();
  }

  // Render results view
  $('#exam-stage').hidden = true;
  $('#exam-subject-strip').hidden = true;
  $('#progress-tracker').hidden = true;

  const resView = $('#exam-results');
  if (resView) resView.hidden = false;

  $('#results-title').textContent = `${examTitle} Completed`;
  $('#results-meta').textContent = `${examKicker} · Submitted in CBT Exam Simulator`;
  $('#res-attempted').textContent = doneCount;
  $('#res-total').textContent = total;
  $('#res-percent').textContent = pct + '%';
  $('#res-time').textContent = fmtTime(timeTaken);

  // Challenge Mode result handling
  if (isChallengeMode && activeChallenge) {
    recordChallengeResult(doneCount, total, pct, timeTaken);
    const retBtn = $('#btn-back-to-papers');
    if (retBtn) retBtn.textContent = '← Return to Challenge Arena';
    const retakeBtn = $('#btn-retake-paper');
    if (retakeBtn) retakeBtn.textContent = '↺ Retake Challenge';
  } else {
    const chalBlock = $('#challenge-results-block');
    if (chalBlock) chalBlock.hidden = true;
    const retBtn = $('#btn-back-to-papers');
    if (retBtn) retBtn.textContent = '← Return to Past Papers';
    const retakeBtn = $('#btn-retake-paper');
    if (retakeBtn) retakeBtn.textContent = '↺ Retake This Paper';
  }

  // Subject breakdown
  const subs = [...new Set(examQuestions.map(q => q.subject).filter(Boolean))];
  const subContainer = $('#results-subject-list');
  if (subContainer) {
    subContainer.innerHTML = subs.map(s => {
      const sQs = examQuestions.filter(q => q.subject === s);
      const sDone = sQs.filter(q => answers[key(q)]).length;
      const sPct = sQs.length ? Math.round((sDone / sQs.length) * 100) : 0;
      const subColor = s === 'Biology' ? '#059669' : s === 'Chemistry' ? '#0284c7' : s === 'Physics' ? '#7c3aed' : s === 'English' ? '#4338ca' : '#d97706';

      return `
        <div class="subject-result-row">
          <div class="subject-result-header">
            <span><strong>${esc(s)}</strong> (${sDone}/${sQs.length} attempted)</span>
            <span style="color:${subColor}; font-weight:800">${sPct}%</span>
          </div>
          <div class="subject-result-bar">
            <div class="subject-result-fill" style="width:${sPct}%; background:${subColor}"></div>
          </div>
        </div>
      `;
    }).join('');
  }
}

function reviewExamAnswers() {
  $('#exam-results').hidden = true;
  $('#exam-stage').hidden = false;
  $('#exam-subject-strip').hidden = false;
  $('#progress-tracker').hidden = false;
  currentExamIndex = 0;
  renderActiveQuestion();
  renderQuestionPalette();
}

function retakeExam() {
  examQuestions.forEach(q => {
    delete answers[key(q)];
    delete flagged[key(q)];
  });
  try {
    localStorage.setItem('myelin-answers', JSON.stringify(answers));
    localStorage.setItem('myelin-flagged', JSON.stringify(flagged));
    if (activeSetKey) {
      localStorage.removeItem('myelin-session:' + activeSetKey);
    }
  } catch {}

  $('#exam-results').hidden = true;
  $('#exam-stage').hidden = false;
  $('#exam-subject-strip').hidden = false;
  $('#progress-tracker').hidden = false;

  currentExamIndex = 0;
  resetTimer();
  startTimer();
  saveSessionState(true);
  updateOverallProgress();
  renderActiveQuestion();
  renderQuestionPalette();
}

// Show Question Set in CBT Professional Exam Style
function show(q, t, k, sessionKey) {
  examQuestions = q || [];
  examTitle = t;
  examKicker = k;
  activeSetKey = sessionKey || k;

  let savedSession = null;
  try {
    const raw = localStorage.getItem('myelin-session:' + activeSetKey);
    if (raw) savedSession = JSON.parse(raw);
  } catch (err) {
    console.warn('Could not read session:', err);
  }

  if (savedSession && !savedSession.completed && typeof savedSession.currentIndex === 'number') {
    currentExamIndex = Math.min(Math.max(0, savedSession.currentIndex), examQuestions.length - 1);
    timerSeconds = typeof savedSession.timerSeconds === 'number' ? savedSession.timerSeconds : 0;
    currentExamSubject = savedSession.currentExamSubject || 'All';
  } else {
    currentExamIndex = 0;
    timerSeconds = 0;
    currentExamSubject = 'All';
  }

  $('#question-kicker').textContent = k;
  $('#question-title').textContent = t;

  $('#exam-results').hidden = true;
  $('#exam-stage').hidden = false;
  $('#progress-tracker').hidden = false;

  startTimer();
  updateOverallProgress();
  renderSubjectStrip();
  renderActiveQuestion();
  renderQuestionPalette();

  saveSessionState(false);

  $('#questions').hidden = false;
  window.scrollTo({ top: 0, behavior: 'smooth' });
}

// Navigation event wireups
$('#btn-prev').onclick = () => prevQuestion();
$('#btn-next').onclick = () => nextQuestion();
$('#btn-flag').onclick = () => toggleFlagCurrent();
$('#btn-clear').onclick = () => clearAnswerCurrent();
$('#btn-finish-test').onclick = () => openFinishModal();
$('#btn-sidebar-finish').onclick = () => openFinishModal();
$('#modal-btn-cancel').onclick = () => closeFinishModal();
$('#modal-btn-confirm').onclick = () => submitExam();
$('#btn-review-questions').onclick = () => reviewExamAnswers();
$('#btn-retake-paper').onclick = () => {
  if (isChallengeMode && activeChallenge) {
    startChallenge(activeChallenge.challengeId);
  } else {
    retakeExam();
  }
};
$('#btn-back-to-papers').onclick = () => {
  if (isChallengeMode) {
    isChallengeMode = false;
    activeChallenge = null;
    location.hash = '#/challenges';
  } else {
    location.hash = '/past-papers';
  }
};

// Question Palette Toggle for Mobile/Drawer
const paletteToggleBtn = $('#palette-toggle-btn');
if (paletteToggleBtn) {
  paletteToggleBtn.onclick = () => {
    const pal = $('#question-palette');
    if (pal) pal.classList.toggle('open');
  };
}
const paletteCloseBtn = $('#palette-close-btn');
if (paletteCloseBtn) {
  paletteCloseBtn.onclick = () => {
    const pal = $('#question-palette');
    if (pal) pal.classList.remove('open');
  };
}

// Keyboard shortcuts for CBT Exam
window.addEventListener('keydown', e => {
  if ($('#questions').hidden) return;
  if (['INPUT', 'TEXTAREA'].includes(e.target.tagName)) return;

  const k = e.key.toUpperCase();
  if (['A', 'B', 'C', 'D'].includes(k)) {
    const optBtn = $(`[data-opt-label="${k}"]`);
    if (optBtn) optBtn.click();
  } else if (['1', '2', '3', '4'].includes(k)) {
    const map = { '1': 'A', '2': 'B', '3': 'C', '4': 'D' };
    const optBtn = $(`[data-opt-label="${map[k]}"]`);
    if (optBtn) optBtn.click();
  } else if (e.key === 'ArrowRight') {
    nextQuestion();
  } else if (e.key === 'ArrowLeft') {
    prevQuestion();
  } else if (k === 'F') {
    toggleFlagCurrent();
  }
});

// Timer controls
const timerToggleBtn = $('#timer-toggle-btn');
if (timerToggleBtn) {
  timerToggleBtn.onclick = () => {
    if (timerRunning) stopTimer();
    else startTimer();
  };
}
const timerResetBtn = $('#timer-reset-btn');
if (timerResetBtn) {
  timerResetBtn.onclick = () => resetTimer();
}

$('#back-button').onclick = () => {
  stopTimer();
  activeSetKey = '';
  if (isChallengeMode) {
    isChallengeMode = false;
    activeChallenge = null;
    location.hash = '#/challenges';
  } else {
    run();
    location.hash = location.hash.startsWith('#/practice/') ? '/practice' : '/past-papers';
  }
};

$('#copyright-year').textContent = new Date().getFullYear();

// Search filter for year grid
$('#year-search').oninput = e => {
  const val = e.target.value.trim().toLowerCase();
  document.querySelectorAll('[data-y]').forEach(b => {
    b.hidden = !b.dataset.y.toLowerCase().includes(val);
  });
};

// Render Main Views (Past Papers grid & Practice by Unit grid)
function run() {
  const bannerSlot = $('#resume-banner-slot');
  if (bannerSlot) {
    let lastSession = null;
    try {
      const raw = localStorage.getItem('myelin-last-session');
      if (raw) lastSession = JSON.parse(raw);
    } catch {}

    if (lastSession && !lastSession.completed && lastSession.path) {
      bannerSlot.innerHTML = `
        <div class="resume-banner">
          <div class="resume-banner-left">
            <strong>Resume In-Progress Paper</strong>
            <span>${esc(lastSession.title)} · Question ${lastSession.currentIndex + 1} of ${lastSession.totalQuestions} (⏱ ${fmtTime(lastSession.timerSeconds)})</span>
          </div>
          <a href="${esc(lastSession.path)}" class="button primary" style="white-space:nowrap;font-size:13px">
            Resume Paper (Q ${lastSession.currentIndex + 1}) →
          </a>
        </div>
      `;
    } else {
      bannerSlot.innerHTML = '';
    }
  }

  let c = {};
  S.q.forEach(x => c[x.year] = (c[x.year] || 0) + 1);

  // Year Grid
  const sortedYears = Object.keys(c).sort((a, b) => Number(a) - Number(b));
  $('#year-grid').innerHTML = sortedYears.map(y => {
    const yQs = S.q.filter(x => x.year === Number(y));
    const done = yQs.filter(x => answers[key(x)]).length;
    const subs = [...new Set(yQs.map(x => x.subject).filter(Boolean))];
    const subBadges = subs.map(s => {
      const cls = getSubjectClass(s);
      return `<span class="q-subject-pill ${cls}" style="font-size:10px;padding:2px 6px">${esc(s)}</span>`;
    }).join(' ');

    let saved = null;
    try {
      const raw = localStorage.getItem('myelin-session:paper:' + y);
      if (raw) saved = JSON.parse(raw);
    } catch {}

    const hasActiveSession = saved && !saved.completed;
    const btnLabel = hasActiveSession
      ? `RESUME PAPER (Q ${saved.currentIndex + 1}) →`
      : `PRACTICE FULL PAPER →`;
    const btnClass = 'primary';

    const resumeBadge = hasActiveSession
      ? `<div class="session-resume-badge">⏱ In progress · Resume at Q ${saved.currentIndex + 1} (${fmtTime(saved.timerSeconds)})</div>`
      : '';

    return `
      <div class="year-card" data-y="${y}">
        <div style="display:flex; justify-content:space-between; align-items:flex-start">
          <strong>${y}</strong>
          <span style="font-size:11px;font-weight:700;color:var(--blue);background:#eff6ff;padding:3px 8px;border-radius:6px">
            ${c[y]} MCQs
          </span>
        </div>
        <div style="margin:10px 0 6px; display:flex; gap:4px; flex-wrap:wrap">
          ${subBadges}
        </div>
        <div style="font-size:12px;font-weight:600;color:var(--navy);margin-top:8px">
          ${done} / ${c[y]} completed
        </div>
        ${resumeBadge}
        <button type="button" class="button ${btnClass} w-full" style="margin-top:14px;padding:9px 12px;font-size:13px;justify-content:center" data-open-year="${y}">
          ${btnLabel}
        </button>
      </div>
    `;
  }).join('');

  document.querySelectorAll('[data-open-year]').forEach(b => {
    b.onclick = e => {
      e.stopPropagation();
      location.hash = '/past-papers/' + b.dataset.openYear;
    };
  });

  document.querySelectorAll('.year-card').forEach(b => {
    b.onclick = () => {
      location.hash = '/past-papers/' + b.dataset.y;
    };
  });

  // Unit Grid by Subject
  let d = {};
  S.q.filter(x => S.sub === 'All' || x.subject === S.sub).forEach(x => {
    (d[x.unit] ??= []).push(x);
  });

  $('#unit-grid').innerHTML = Object.entries(d).map(([u, q], i) => {
    const done = q.filter(x => answers[key(x)]).length;
    const subName = q[0]?.subject || '';
    const subCls = getSubjectClass(subName);

    let saved = null;
    try {
      const raw = localStorage.getItem(`myelin-session:unit:${S.sub}:${u}`);
      if (raw) saved = JSON.parse(raw);
    } catch {}

    const hasActiveSession = saved && !saved.completed;
    const btnLabel = hasActiveSession
      ? `RESUME QUIZ (Q ${saved.currentIndex + 1}) →`
      : `PRACTICE UNIT QUIZ →`;
    const resumeBadge = hasActiveSession
      ? `<div class="session-resume-badge">⏱ In progress · Resume at Q ${saved.currentIndex + 1} (${fmtTime(saved.timerSeconds)})</div>`
      : '';

    return `
      <div class="unit-card" data-u="${i}">
        <div style="display:flex; justify-content:space-between; align-items:flex-start; margin-bottom:8px">
          <span class="q-subject-pill ${subCls}" style="font-size:10px;padding:2px 6px">${esc(subName)}</span>
          <span style="font-size:11px;font-weight:700;color:var(--muted)">${q.length} MCQs</span>
        </div>
        <strong>${esc(u)}</strong>
        <span style="display:block;font-size:12px;margin-top:10px;font-weight:600;color:var(--navy)">
          ${done} / ${q.length} completed
        </span>
        ${resumeBadge}
        <button type="button" class="button secondary w-full" style="margin-top:12px;padding:8px 12px;font-size:12px;justify-content:center" data-open-unit="${i}">
          ${btnLabel}
        </button>
      </div>
    `;
  }).join('');

  document.querySelectorAll('[data-open-unit]').forEach(b => {
    b.onclick = e => {
      e.stopPropagation();
      const entry = Object.entries(d)[b.dataset.openUnit];
      if (entry) {
        location.hash = '/practice/' + encodeURIComponent(S.sub) + '/' + encodeURIComponent(entry[0]);
      }
    };
  });

  document.querySelectorAll('.unit-card').forEach(b => {
    b.onclick = () => {
      const entry = Object.entries(d)[b.dataset.u];
      if (entry) {
        location.hash = '/practice/' + encodeURIComponent(S.sub) + '/' + encodeURIComponent(entry[0]);
      }
    };
  });

  // Subject Tabs
  const allSubs = ['All', 'Biology', 'Chemistry', 'Physics', 'English', 'Logical Reasoning'];
  const existingSubs = new Set(S.q.map(x => x.subject).filter(Boolean));
  const validTabs = allSubs.filter(s => s === 'All' || existingSubs.has(s));

  $('#subject-tabs').innerHTML = validTabs.map(x => {
    const active = x === S.sub ? 'active' : '';
    const cls = x === 'All' ? '' : 'subject-' + getSubjectClass(x);
    return `<button class="tab ${active} ${cls}" data-s="${esc(x)}">${esc(x)}</button>`;
  }).join('');

  document.querySelectorAll('[data-s]').forEach(b => {
    b.onclick = () => {
      S.sub = b.dataset.s;
      run();
    };
  });

  loadPracticeDashboard();
  loadChallengeDashboard();
}

// ==========================================================================
// Practice Dashboard & Accuracy Trends Component (D3 & Firestore)
// ==========================================================================
let isDashboardLoading = false;

async function loadPracticeDashboard() {
  const container = $('#dashboard-chart-container');
  const metricsStrip = $('#dashboard-metrics-strip');
  const syncPill = $('#dashboard-sync-pill');
  if (!container || !metricsStrip) return;

  // If user is not authenticated with Google
  if (!auth.currentUser) {
    if (syncPill) {
      syncPill.textContent = '🔒 Guest Mode';
      syncPill.style.background = '#f1f5f9';
      syncPill.style.color = '#64748b';
      syncPill.style.borderColor = '#cbd5e1';
    }
    metricsStrip.innerHTML = `
      <div class="dashboard-metric-card">
        <span class="metric-card-label">Total Tests Taken</span>
        <span class="metric-card-value">-</span>
        <span class="metric-card-sub">Sign in to track</span>
      </div>
      <div class="dashboard-metric-card">
        <span class="metric-card-label">Average Accuracy</span>
        <span class="metric-card-value">-</span>
        <span class="metric-card-sub">PMDC target is 75%</span>
      </div>
      <div class="dashboard-metric-card">
        <span class="metric-card-label">Peak Score</span>
        <span class="metric-card-value">-</span>
        <span class="metric-card-sub">Best session recorded</span>
      </div>
      <div class="dashboard-metric-card">
        <span class="metric-card-label">Total Time Spent</span>
        <span class="metric-card-value">-</span>
        <span class="metric-card-sub">Practice duration</span>
      </div>
    `;
    container.innerHTML = `
      <div class="dashboard-guest-card">
        <span class="dashboard-empty-icon">📊</span>
        <h4 class="dashboard-empty-title">Track Your MDCAT Practice & Accuracy Trends</h4>
        <p class="dashboard-empty-desc">
          Sign in with your Google account to record every completed past paper, plot your accuracy trends over time in Firestore, and compare against the PMDC 75% benchmark.
        </p>
        <button type="button" class="google-sign-in-btn" id="dashboard-google-login-btn" style="margin:auto">
          <svg width="18" height="18" viewBox="0 0 24 24" aria-hidden="true">
            <path fill="#4285F4" d="M22.56 12.25c0-.78-.07-1.53-.2-2.25H12v4.26h5.92c-.26 1.37-1.04 2.53-2.21 3.31v2.77h3.57c2.08-1.92 3.28-4.74 3.28-8.09z"/>
            <path fill="#34A853" d="M12 23c2.97 0 5.46-.98 7.28-2.66l-3.57-2.77c-.98.66-2.23 1.06-3.71 1.06-2.86 0-5.29-1.93-6.16-4.53H2.18v2.84C3.99 20.53 7.7 23 12 23z"/>
            <path fill="#FBBC05" d="M5.84 14.09c-.22-.66-.35-1.36-.35-2.09s.13-1.43.35-2.09V7.06H2.18C1.43 8.55 1 10.22 1 12s.43 3.45 1.18 4.94l2.85-2.22.81-.63z"/>
            <path fill="#EA4335" d="M12 5.38c1.62 0 3.06.56 4.21 1.64l3.15-3.15C17.45 2.09 14.97 1 12 1 7.7 1 3.99 3.47 2.18 7.06l3.66 2.84c.87-2.6 3.3-4.52 6.16-4.52z"/>
          </svg>
          <span>Sign in with Google</span>
        </button>
      </div>
    `;
    const dBtn = $('#dashboard-google-login-btn');
    if (dBtn) dBtn.onclick = () => loginWithGoogle();
    return;
  }

  if (syncPill) {
    syncPill.textContent = '☁ Synced with Firestore';
    syncPill.style.background = '#ecfdf5';
    syncPill.style.color = '#047857';
    syncPill.style.borderColor = '#a7f3d0';
  }

  if (isDashboardLoading) return;
  isDashboardLoading = true;

  try {
    const userId = auth.currentUser.uid;
    const colRef = collection(db, 'users', userId, 'sessions');
    const snap = await getDocs(colRef);
    const sessionsMap = new Map();

    snap.forEach(docSnap => {
      const data = docSnap.data();
      if (data && data.paperKey) {
        sessionsMap.set(data.paperKey, data);
      }
    });

    // Also merge any locally saved sessions if not already present
    for (let i = 0; i < localStorage.length; i++) {
      const k = localStorage.key(i);
      if (k && k.startsWith('myelin-session:')) {
        try {
          const lData = JSON.parse(localStorage.getItem(k));
          if (lData && lData.key && !sessionsMap.has(lData.key)) {
            sessionsMap.set(lData.key, {
              sessionId: sanitizeDocId(lData.key),
              userId: userId,
              paperKey: lData.key,
              title: lData.title,
              accuracy: typeof lData.accuracy === 'number' ? lData.accuracy : Math.round(((lData.currentIndex || 0) / (lData.totalQuestions || 1)) * 100),
              attemptedCount: lData.currentIndex || 0,
              totalQuestions: lData.totalQuestions || 200,
              timerSeconds: lData.timerSeconds || 0,
              completed: !!lData.completed,
              updatedAt: new Date(lData.lastUpdated || Date.now()).toISOString()
            });
          }
        } catch {}
      }
    }

    const allSessions = Array.from(sessionsMap.values());

    const dataPoints = allSessions.map(s => {
      let acc = typeof s.accuracy === 'number' ? s.accuracy : null;
      if (acc === null && s.totalQuestions) {
        acc = Math.round(((s.attemptedCount || s.currentIndex || 0) / s.totalQuestions) * 100);
      }
      return {
        key: s.paperKey || s.sessionId,
        title: s.title || s.paperKey || 'Practice Session',
        accuracy: Math.min(100, Math.max(0, acc || 0)),
        attempted: s.attemptedCount || s.currentIndex || 0,
        total: s.totalQuestions || 200,
        completed: !!s.completed,
        timerSeconds: s.timerSeconds || 0,
        timestamp: new Date(s.completedAt || s.updatedAt || Date.now()).getTime(),
        dateStr: new Date(s.completedAt || s.updatedAt || Date.now()).toLocaleDateString('en-US', { month: 'short', day: 'numeric' })
      };
    }).sort((a, b) => a.timestamp - b.timestamp);

    const totalSessions = dataPoints.length;
    const completedSessions = dataPoints.filter(d => d.completed).length;
    const avgAccuracy = totalSessions > 0 ? Math.round(dataPoints.reduce((sum, d) => sum + d.accuracy, 0) / totalSessions) : 0;
    const peakAccuracy = totalSessions > 0 ? Math.max(...dataPoints.map(d => d.accuracy)) : 0;
    const totalTimeSecs = dataPoints.reduce((sum, d) => sum + (d.timerSeconds || 0), 0);

    metricsStrip.innerHTML = `
      <div class="dashboard-metric-card">
        <span class="metric-card-label">Total Tests Taken</span>
        <span class="metric-card-value">${totalSessions}</span>
        <span class="metric-card-sub">${completedSessions} completed papers</span>
      </div>
      <div class="dashboard-metric-card">
        <span class="metric-card-label">Average Accuracy</span>
        <span class="metric-card-value" style="color:${avgAccuracy >= 75 ? '#059669' : 'var(--navy)'}">${avgAccuracy}%</span>
        <span class="metric-card-sub">PMDC benchmark is 75%</span>
      </div>
      <div class="dashboard-metric-card">
        <span class="metric-card-label">Peak Score</span>
        <span class="metric-card-value" style="color:#2563eb">${peakAccuracy}%</span>
        <span class="metric-card-sub">Best session recorded</span>
      </div>
      <div class="dashboard-metric-card">
        <span class="metric-card-label">Total Time Spent</span>
        <span class="metric-card-value">${fmtTime(totalTimeSecs)}</span>
        <span class="metric-card-sub">Practice duration</span>
      </div>
    `;

    if (totalSessions === 0) {
      container.innerHTML = `
        <div class="dashboard-empty-state">
          <span class="dashboard-empty-icon">📈</span>
          <h4 class="dashboard-empty-title">No Practice Records Yet</h4>
          <p class="dashboard-empty-desc">
            Choose a past paper or unit test from the sections below. As you practice and submit tests, your accuracy trends and time analysis will be automatically calculated and plotted here.
          </p>
          <a href="#/past-papers" class="button primary" style="font-size:13px">Start a Past Paper →</a>
        </div>
      `;
    } else {
      renderD3AccuracyChart(dataPoints, container);
    }
  } catch (err) {
    console.error('Error fetching dashboard from Firestore:', err);
    try {
      handleFirestoreError(err, OperationType.LIST, 'users/' + auth.currentUser.uid + '/sessions');
    } catch {}
    container.innerHTML = `
      <div class="dashboard-empty-state">
        <p style="color:#dc2626">Unable to load sessions from Firestore. Please check connection.</p>
      </div>
    `;
  } finally {
    isDashboardLoading = false;
  }
}

function renderD3AccuracyChart(data, container) {
  container.innerHTML = '';
  const tooltip = $('#chart-tooltip');

  const containerWidth = container.clientWidth || container.getBoundingClientRect().width || 600;
  const margin = { top: 20, right: 30, bottom: 40, left: 45 };
  const width = Math.max(300, containerWidth - margin.left - margin.right);
  const height = 260 - margin.top - margin.bottom;

  const svg = d3.create('svg')
    .attr('viewBox', `0 0 ${width + margin.left + margin.right} ${height + margin.top + margin.bottom}`)
    .attr('width', '100%')
    .attr('height', '100%')
    .style('max-height', '280px');

  const defs = svg.append('defs');
  const gradient = defs.append('linearGradient')
    .attr('id', 'accuracy-gradient')
    .attr('x1', '0%').attr('y1', '0%')
    .attr('x2', '0%').attr('y2', '100%');
  gradient.append('stop').attr('offset', '0%').attr('stop-color', '#2563eb').attr('stop-opacity', 0.28);
  gradient.append('stop').attr('offset', '100%').attr('stop-color', '#2563eb').attr('stop-opacity', 0.02);

  const g = svg.append('g')
    .attr('transform', `translate(${margin.left},${margin.top})`);

  const xScale = d3.scalePoint()
    .domain(data.map((_, i) => i))
    .range([0, width])
    .padding(0.3);

  const yScale = d3.scaleLinear()
    .domain([0, 100])
    .range([height, 0]);

  // Horizontal Grid lines
  g.append('g')
    .attr('class', 'grid-lines')
    .call(
      d3.axisLeft(yScale)
        .tickValues([25, 50, 75, 100])
        .tickSize(-width)
        .tickFormat('')
    )
    .call(g => g.select('.domain').remove())
    .call(g => g.selectAll('.tick line').attr('stroke', '#e2e8f0').attr('stroke-dasharray', '3,3'));

  // Benchmark target line (75%)
  const benchmarkY = yScale(75);
  g.append('line')
    .attr('x1', 0)
    .attr('x2', width)
    .attr('y1', benchmarkY)
    .attr('y2', benchmarkY)
    .attr('stroke', '#10b981')
    .attr('stroke-width', 1.5)
    .attr('stroke-dasharray', '4,4');

  g.append('text')
    .attr('x', width - 4)
    .attr('y', benchmarkY - 6)
    .attr('text-anchor', 'end')
    .attr('fill', '#059669')
    .attr('font-size', '11px')
    .attr('font-weight', '700')
    .text('Target (75%)');

  // Area under curve
  if (data.length > 1) {
    const area = d3.area()
      .x((d, i) => xScale(i))
      .y0(height)
      .y1(d => yScale(d.accuracy))
      .curve(d3.curveMonotoneX);

    g.append('path')
      .datum(data)
      .attr('fill', 'url(#accuracy-gradient)')
      .attr('d', area);
  }

  // Line path
  const line = d3.line()
    .x((d, i) => xScale(i))
    .y(d => yScale(d.accuracy))
    .curve(data.length > 1 ? d3.curveMonotoneX : d3.curveLinear);

  g.append('path')
    .datum(data)
    .attr('fill', 'none')
    .attr('stroke', '#2563eb')
    .attr('stroke-width', 3)
    .attr('d', line);

  // X Axis
  g.append('g')
    .attr('transform', `translate(0,${height})`)
    .call(
      d3.axisBottom(xScale)
        .tickFormat(i => {
          const item = data[i];
          if (!item) return '';
          return item.title.length > 14 ? item.title.slice(0, 12) + '…' : item.title;
        })
    )
    .call(g => g.select('.domain').attr('stroke', '#cbd5e1'))
    .call(g => g.selectAll('.tick text')
      .attr('fill', '#64748b')
      .attr('font-size', '11px')
      .attr('font-weight', '600')
    );

  // Y Axis
  g.append('g')
    .call(
      d3.axisLeft(yScale)
        .tickValues([0, 25, 50, 75, 100])
        .tickFormat(d => d + '%')
    )
    .call(g => g.select('.domain').remove())
    .call(g => g.selectAll('.tick text')
      .attr('fill', '#64748b')
      .attr('font-size', '11px')
      .attr('font-weight', '600')
    );

  // Data Dots with interactive hover tooltips
  g.selectAll('.data-dot')
    .data(data)
    .enter()
    .append('circle')
    .attr('class', 'data-dot')
    .attr('cx', (d, i) => xScale(i))
    .attr('cy', d => yScale(d.accuracy))
    .attr('r', 5)
    .attr('fill', '#2563eb')
    .attr('stroke', '#ffffff')
    .attr('stroke-width', 2.5)
    .style('cursor', 'pointer')
    .on('mouseenter', (event, d) => {
      d3.select(event.currentTarget).transition().duration(150).attr('r', 8).attr('fill', '#1d4ed8');
      if (tooltip) {
        tooltip.hidden = false;
        tooltip.innerHTML = `
          <strong>${esc(d.title)}</strong><br>
          Accuracy: <b style="color:#93c5fd">${d.accuracy}%</b> (${d.attempted}/${d.total} MCQs)<br>
          <span style="font-size:11px;color:#94a3b8">Date: ${esc(d.dateStr)} · Time: ${fmtTime(d.timerSeconds)}</span>
        `;
        const rect = container.getBoundingClientRect();
        tooltip.style.left = (event.clientX - rect.left) + 'px';
        tooltip.style.top = (event.clientY - rect.top - 10) + 'px';
      }
    })
    .on('mouseleave', (event) => {
      d3.select(event.currentTarget).transition().duration(150).attr('r', 5).attr('fill', '#2563eb');
      if (tooltip) tooltip.hidden = true;
    });

  container.appendChild(svg.node());
}

// Window resize listener for responsive chart
window.addEventListener('resize', () => {
  const heroEl = $('.hero');
  if (heroEl && !heroEl.hidden && auth.currentUser) {
    loadPracticeDashboard();
  }
});

// ==========================================================================
// Challenge Mode & Live Peer Leaderboard (Firestore Real-time)
// ==========================================================================

function getGuestIdentifier() {
  let gid = localStorage.getItem('myelin-guest-id');
  if (!gid) {
    gid = 'guest_' + Math.random().toString(36).substring(2, 9) + '_' + Date.now().toString(36);
    localStorage.setItem('myelin-guest-id', gid);
  }
  return gid;
}

function getGuestDisplayName() {
  let gname = localStorage.getItem('myelin-guest-name');
  if (!gname) {
    const num = Math.floor(1000 + Math.random() * 9000);
    gname = 'Aspirant #' + num;
    localStorage.setItem('myelin-guest-name', gname);
  }
  return gname;
}

function selectChallengeQuestions(subject, count) {
  let pool = S.q;
  if (subject && subject !== 'All') {
    pool = pool.filter(q => q.subject === subject);
  }
  if (!pool.length) pool = S.q;

  const countNeeded = Math.min(count, pool.length);
  const selected = [];
  const poolCopy = [...pool];
  const step = Math.max(1, Math.floor(poolCopy.length / countNeeded));

  for (let i = 0; i < countNeeded && (i * step) < poolCopy.length; i++) {
    selected.push(poolCopy[i * step]);
  }
  let fillIdx = 0;
  while (selected.length < countNeeded && fillIdx < poolCopy.length) {
    if (!selected.includes(poolCopy[fillIdx])) {
      selected.push(poolCopy[fillIdx]);
    }
    fillIdx++;
  }
  return selected;
}

function getQuestionsFromKeys(keysArray) {
  const map = new Map(S.q.map(q => [key(q), q]));
  const matched = [];
  for (const k of keysArray) {
    if (map.has(k)) matched.push(map.get(k));
  }
  return matched;
}

function subscribeToLeaderboard(challengeId, containerId = 'leaderboard-rows-list', onEntriesLoaded = null) {
  if (currentLeaderboardUnsub) {
    currentLeaderboardUnsub();
    currentLeaderboardUnsub = null;
  }

  const lbRef = collection(db, 'challenges', challengeId, 'leaderboard');
  const lbQuery = query(lbRef, limit(50));

  currentLeaderboardUnsub = onSnapshot(lbQuery, snapshot => {
    const entries = [];
    snapshot.forEach(docSnap => {
      entries.push(docSnap.data());
    });

    // Primary sort: score desc, Secondary sort: timeTakenSeconds asc, Tertiary: submittedAt asc
    entries.sort((a, b) => {
      if ((b.score ?? 0) !== (a.score ?? 0)) return (b.score ?? 0) - (a.score ?? 0);
      if ((a.timeTakenSeconds ?? 9999) !== (b.timeTakenSeconds ?? 9999)) {
        return (a.timeTakenSeconds ?? 9999) - (b.timeTakenSeconds ?? 9999);
      }
      return (a.submittedAt || '').localeCompare(b.submittedAt || '');
    });

    renderLeaderboardRows(entries, containerId);
    if (typeof onEntriesLoaded === 'function') {
      onEntriesLoaded(entries);
    }
  }, error => {
    console.error('Leaderboard snapshot error:', error);
  });
}

function renderLeaderboardRows(entries, containerId = 'leaderboard-rows-list') {
  const container = $('#' + containerId);
  if (!container) return;

  if (!entries || entries.length === 0) {
    container.innerHTML = `
      <div style="text-align:center;padding:36px 20px;color:var(--muted)">
        <div style="font-size:32px;margin-bottom:8px">⚔️</div>
        <strong style="display:block;color:var(--navy);font-size:15px;margin-bottom:4px">No contenders on the board yet</strong>
        <span style="font-size:13px">Be the first to finish this timed set and claim Rank #1 🏆</span>
      </div>
    `;
    return;
  }

  const currentUid = auth.currentUser?.uid || getGuestIdentifier();

  container.innerHTML = entries.map((entry, idx) => {
    const rank = idx + 1;
    let rankBadge = `<span class="rank-badge rank-regular">#${rank}</span>`;
    if (rank === 1) rankBadge = `<span class="rank-badge rank-1" title="1st Place (Gold)">🥇</span>`;
    else if (rank === 2) rankBadge = `<span class="rank-badge rank-2" title="2nd Place (Silver)">🥈</span>`;
    else if (rank === 3) rankBadge = `<span class="rank-badge rank-3" title="3rd Place (Bronze)">🥉</span>`;

    const isCurrent = entry.participantId === currentUid;
    const isCurrentUserClass = isCurrent ? 'is-current-user' : '';
    const youBadge = isCurrent ? '<span class="you-badge">YOU</span>' : '';

    const avatar = entry.photoURL
      ? `<div class="user-avatar"><img src="${esc(entry.photoURL)}" alt="${esc(entry.displayName)}" loading="lazy"></div>`
      : `<div class="user-avatar">${esc((entry.displayName || 'A').slice(0, 2).toUpperCase())}</div>`;

    const acc = Math.round(entry.accuracy ?? (entry.totalQuestions ? (entry.score / entry.totalQuestions) * 100 : 0));
    const accClass = acc >= 75 ? 'acc-high' : acc >= 50 ? 'acc-mid' : 'acc-low';

    let timeAgo = 'Just now';
    if (entry.submittedAt) {
      const diffMin = Math.floor((Date.now() - new Date(entry.submittedAt).getTime()) / 60000);
      if (diffMin > 1440) timeAgo = `${Math.floor(diffMin / 1440)}d ago`;
      else if (diffMin > 60) timeAgo = `${Math.floor(diffMin / 60)}h ago`;
      else if (diffMin > 0) timeAgo = `${diffMin}m ago`;
    }

    return `
      <div class="leaderboard-row ${isCurrentUserClass}">
        <div class="col-rank">${rankBadge}</div>
        <div class="col-user">
          ${avatar}
          <div class="user-name-group">
            <span class="user-name">${esc(entry.displayName || 'Aspirant')}${youBadge}</span>
          </div>
        </div>
        <div class="col-score">${entry.score} / ${entry.totalQuestions}</div>
        <div class="col-accuracy">
          <span class="accuracy-chip ${accClass}">${acc}%</span>
        </div>
        <div class="col-time">⏱ ${fmtTime(entry.timeTakenSeconds || 0)}</div>
        <div class="col-status">${timeAgo}</div>
      </div>
    `;
  }).join('');
}

async function seedFeaturedChallengesIfEmpty() {
  try {
    const snap = await getDocs(collection(db, 'challenges'));
    if (!snap.empty) return;

    console.log('Seeding initial featured challenges to Firestore...');

    const defaultChallenges = [
      {
        challengeId: 'chal_uhs_2024_sprint',
        code: 'CHAL-2024',
        title: 'UHS 2024 Speed Sprint',
        creatorId: 'system',
        creatorName: 'MDCAT Academic Board',
        subject: 'All',
        timeLimitSeconds: 300,
        totalQuestions: 15,
        participantCount: 4,
        createdAt: new Date().toISOString(),
        status: 'active'
      },
      {
        challengeId: 'chal_bio_blitz',
        code: 'CHAL-BIO1',
        title: 'Cell & Genetics High-Yield Blitz',
        creatorId: 'system',
        creatorName: 'Prof. Rehan (Biology)',
        subject: 'Biology',
        timeLimitSeconds: 300,
        totalQuestions: 15,
        participantCount: 3,
        createdAt: new Date().toISOString(),
        status: 'active'
      },
      {
        challengeId: 'chal_phys_rush',
        code: 'CHAL-PHYS',
        title: 'Physics Mechanics & Force Rush',
        creatorId: 'system',
        creatorName: 'Physics Faculty',
        subject: 'Physics',
        timeLimitSeconds: 180,
        totalQuestions: 10,
        participantCount: 2,
        createdAt: new Date().toISOString(),
        status: 'active'
      }
    ];

    for (const c of defaultChallenges) {
      const qList = selectChallengeQuestions(c.subject, c.totalQuestions);
      c.questionKeys = JSON.stringify(qList.map(q => key(q)));
      await setDoc(doc(db, 'challenges', c.challengeId), c);
    }

    // Seed realistic benchmark competitors for the main challenge
    const benchmarkContenders = [
      { participantId: 'bench_1', displayName: 'Dr. Ayesha Noor', photoURL: '', score: 15, totalQuestions: 15, accuracy: 100, timeTakenSeconds: 194, completed: true, submittedAt: new Date(Date.now() - 3600000).toISOString() },
      { participantId: 'bench_2', displayName: 'Zubair Farooq', photoURL: '', score: 14, totalQuestions: 15, accuracy: 93, timeTakenSeconds: 225, completed: true, submittedAt: new Date(Date.now() - 7200000).toISOString() },
      { participantId: 'bench_3', displayName: 'Hamza Tariq', photoURL: '', score: 13, totalQuestions: 15, accuracy: 87, timeTakenSeconds: 242, completed: true, submittedAt: new Date(Date.now() - 14400000).toISOString() },
      { participantId: 'bench_4', displayName: 'Fatima Zahra', photoURL: '', score: 12, totalQuestions: 15, accuracy: 80, timeTakenSeconds: 258, completed: true, submittedAt: new Date(Date.now() - 28800000).toISOString() }
    ];

    for (const cont of benchmarkContenders) {
      await setDoc(doc(db, 'challenges', 'chal_uhs_2024_sprint', 'leaderboard', cont.participantId), cont);
    }
  } catch (err) {
    console.warn('Could not seed featured challenges:', err);
  }
}

async function loadChallengeDashboard() {
  const pillsContainer = $('#challenge-pills-list');
  const bannerContainer = $('#active-challenge-banner');
  if (!pillsContainer || !bannerContainer) return;

  try {
    await seedFeaturedChallengesIfEmpty();

    const snap = await getDocs(collection(db, 'challenges'));
    const list = [];
    snap.forEach(d => list.push(d.data()));

    // Sort by createdAt desc
    list.sort((a, b) => (b.createdAt || '').localeCompare(a.createdAt || ''));
    cachedChallenges = list;

    if (!list.length) return;

    if (!selectedChallengeId || !list.some(c => c.challengeId === selectedChallengeId)) {
      selectedChallengeId = list[0].challengeId;
    }

    const currentChal = list.find(c => c.challengeId === selectedChallengeId) || list[0];

    // Render Pills
    pillsContainer.innerHTML = list.map(c => {
      const isSel = c.challengeId === currentChal.challengeId;
      return `
        <button type="button" class="chal-tab-pill ${isSel ? 'active' : ''}" data-chal-id="${esc(c.challengeId)}">
          <span>⚡ ${esc(c.title)}</span>
          <span class="chal-pill-count">⏱ ${Math.round(c.timeLimitSeconds / 60)}m</span>
        </button>
      `;
    }).join('');

    pillsContainer.querySelectorAll('[data-chal-id]').forEach(btn => {
      btn.onclick = () => {
        selectedChallengeId = btn.dataset.chalId;
        loadChallengeDashboard();
      };
    });

    // Render Active Banner
    const minutes = Math.round(currentChal.timeLimitSeconds / 60);
    bannerContainer.innerHTML = `
      <div class="active-challenge-details">
        <div class="active-challenge-title-row">
          <h4 class="active-challenge-title">${esc(currentChal.title)}</h4>
          <span class="chal-badge chal-badge-subject">📚 ${esc(currentChal.subject || 'All Subjects')}</span>
          <span class="chal-badge chal-badge-time">⏱ ${minutes}m Time Limit</span>
          <span class="chal-badge chal-badge-mcqs">📝 ${currentChal.totalQuestions} MCQs</span>
        </div>
        <div class="active-challenge-meta">
          <span>Created by: <strong>${esc(currentChal.creatorName || 'Aspirant Host')}</strong></span>
          <span>Challenge Code: <strong style="color:var(--blue);letter-spacing:0.04em">${esc(currentChal.code)}</strong></span>
        </div>
      </div>
      <div class="active-challenge-actions">
        <button type="button" class="btn-copy-code" id="btn-banner-copy-code" data-code="${esc(currentChal.code)}">
          📋 Copy Code (${esc(currentChal.code)})
        </button>
        <a href="#/challenge/${esc(currentChal.challengeId)}" class="button primary btn-start-challenge">
          ⚔️ Start Challenge Now →
        </a>
      </div>
    `;

    const copyBtn = $('#btn-banner-copy-code');
    if (copyBtn) {
      copyBtn.onclick = () => {
        navigator.clipboard.writeText(currentChal.code).then(() => {
          copyBtn.textContent = 'Copied! ✓';
          setTimeout(() => {
            copyBtn.textContent = `📋 Copy Code (${currentChal.code})`;
          }, 2000);
        });
      };
    }

    // Subscribe real-time leaderboard
    subscribeToLeaderboard(currentChal.challengeId, 'leaderboard-rows-list');
  } catch (err) {
    console.error('Error loading challenge dashboard:', err);
  }
}

async function recordChallengeResult(score, total, accuracy, timeTaken) {
  const chalBlock = $('#challenge-results-block');
  if (chalBlock) chalBlock.hidden = false;

  const user = auth.currentUser;
  const participantId = user ? user.uid : getGuestIdentifier();
  const displayName = user ? (user.displayName || 'MDCAT Aspirant') : getGuestDisplayName();
  const photoURL = user?.photoURL || '';

  const entryData = {
    participantId,
    displayName,
    photoURL,
    score,
    totalQuestions: total,
    accuracy,
    timeTakenSeconds: Math.max(1, timeTaken),
    completed: true,
    submittedAt: new Date().toISOString()
  };

  try {
    const entryRef = doc(db, 'challenges', activeChallenge.challengeId, 'leaderboard', participantId);
    await setDoc(entryRef, entryData, { merge: true });
  } catch (err) {
    console.error('Error saving leaderboard score:', err);
  }

  // Live subscription on results screen
  subscribeToLeaderboard(activeChallenge.challengeId, 'challenge-post-leaderboard-rows', entries => {
    const myRankIdx = entries.findIndex(e => e.participantId === participantId);
    const rankNum = myRankIdx !== -1 ? myRankIdx + 1 : 1;
    const totalContenders = entries.length;

    const rankText = $('#res-chal-rank-text');
    const badgeIcon = $('#res-chal-badge');
    const summaryText = $('#res-chal-summary-text');

    if (rankText) rankText.textContent = `Rank #${rankNum} of ${totalContenders}`;
    if (badgeIcon) {
      badgeIcon.textContent = rankNum === 1 ? '🥇' : rankNum === 2 ? '🥈' : rankNum === 3 ? '🥉' : '🏆';
    }
    if (summaryText) {
      summaryText.textContent = `Finished in ${fmtTime(timeTaken)} with ${score}/${total} score (${accuracy}%).`;
    }
  });

  const shareBtn = $('#btn-challenge-share-result');
  if (shareBtn) {
    shareBtn.onclick = () => {
      const url = `${window.location.origin}${window.location.pathname}#/challenge/${activeChallenge.challengeId}`;
      const text = `🏆 I ranked on the leaderboard with ${score}/${total} in ${fmtTime(timeTaken)} on MDCAT Challenge "${activeChallenge.title}"! Beat my score with Code: ${activeChallenge.code} -> ${url}`;
      navigator.clipboard.writeText(text).then(() => {
        shareBtn.textContent = 'Challenge Link Copied! ✓';
        setTimeout(() => {
          shareBtn.textContent = 'Share Challenge Link 📋';
        }, 2500);
      });
    };
  }

  const retDashBtn = $('#btn-return-dashboard-leaderboard');
  if (retDashBtn) {
    retDashBtn.onclick = () => {
      stopTimer();
      isChallengeMode = false;
      activeChallenge = null;
      location.hash = '#/challenges';
    };
  }
}

async function startChallenge(challengeId) {
  let challenge = cachedChallenges.find(c => c.challengeId === challengeId);
  if (!challenge) {
    try {
      const snap = await getDoc(doc(db, 'challenges', challengeId));
      if (snap.exists()) {
        challenge = snap.data();
      }
    } catch (e) {
      console.warn('Could not fetch challenge:', e);
    }
  }

  if (!challenge) {
    alert('Challenge not found! Redirecting to Challenge Dashboard.');
    location.hash = '#/challenges';
    return;
  }

  let qs = [];
  if (challenge.questionKeys) {
    try {
      const keys = JSON.parse(challenge.questionKeys);
      qs = getQuestionsFromKeys(keys);
    } catch {}
  }

  if (!qs.length) {
    qs = selectChallengeQuestions(challenge.subject, challenge.totalQuestions || 15);
  }

  isChallengeMode = true;
  activeChallenge = challenge;
  challengeTimeLimit = challenge.timeLimitSeconds || 300;

  const title = challenge.title || 'Timed Peer Challenge';
  const kicker = `⚡ CHALLENGE MODE · CODE: ${challenge.code} · ⏱ ${Math.floor(challengeTimeLimit / 60)}M LIMIT`;
  const sessionKey = 'challenge:' + challenge.challengeId;

  // Clear previous answers for a fresh run
  qs.forEach(q => {
    delete answers[key(q)];
    delete flagged[key(q)];
  });

  show(qs, title, kicker, sessionKey);
  $('#question-kicker').textContent = kicker;

  // Force timer to start from 0
  timerSeconds = 0;
  startTimer();
}

function initChallengeModeUI() {
  // Open Create Challenge Modal
  const openCreateBtn = $('#btn-open-create-challenge');
  const createModal = $('#create-challenge-modal');
  const closeCreateBtn = $('#btn-close-create-modal');
  const cancelCreateBtn = $('#btn-cancel-create');

  if (openCreateBtn && createModal) {
    openCreateBtn.onclick = () => {
      createModal.hidden = false;
    };
  }
  if (closeCreateBtn && createModal) {
    closeCreateBtn.onclick = () => {
      createModal.hidden = true;
    };
  }
  if (cancelCreateBtn && createModal) {
    cancelCreateBtn.onclick = () => {
      createModal.hidden = true;
    };
  }

  // Hint pills to auto-fill title
  document.querySelectorAll('.hint-pill').forEach(pill => {
    pill.onclick = () => {
      const titleInput = $('#chal-title');
      if (titleInput && pill.dataset.hint) {
        titleInput.value = pill.dataset.hint;
        titleInput.focus();
      }
    };
  });

  // Time limit options active visual state
  document.querySelectorAll('.time-opt-card input').forEach(input => {
    input.onchange = () => {
      document.querySelectorAll('.time-opt-card').forEach(card => card.classList.remove('active'));
      input.closest('.time-opt-card')?.classList.add('active');
    };
  });

  // Create Challenge Form Submission
  const createForm = $('#create-challenge-form');
  if (createForm) {
    createForm.onsubmit = async e => {
      e.preventDefault();
      const title = ($('#chal-title')?.value || '').trim();
      const subject = $('#chal-subject')?.value || 'All';
      const mcqs = parseInt($('#chal-mcqs')?.value || '15', 10);
      const timeLimitSec = parseInt(document.querySelector('input[name="time-limit"]:checked')?.value || '300', 10);

      if (!title) {
        alert('Please give your challenge a name.');
        return;
      }

      const submitBtn = createForm.querySelector('button[type="submit"]');
      if (submitBtn) {
        submitBtn.disabled = true;
        submitBtn.textContent = 'Generating Challenge…';
      }

      try {
        const randCode = 'CHAL-' + Math.floor(1000 + Math.random() * 9000);
        const challengeId = 'chal_' + Date.now() + '_' + Math.random().toString(36).substring(2, 7);

        const qs = selectChallengeQuestions(subject, mcqs);
        const qKeys = qs.map(q => key(q));

        const user = auth.currentUser;
        const newChallenge = {
          challengeId,
          code: randCode,
          title,
          creatorId: user ? user.uid : getGuestIdentifier(),
          creatorName: user ? (user.displayName || 'MDCAT Aspirant') : getGuestDisplayName(),
          subject,
          timeLimitSeconds: timeLimitSec,
          totalQuestions: qs.length,
          questionKeys: JSON.stringify(qKeys),
          participantCount: 0,
          createdAt: new Date().toISOString(),
          status: 'active'
        };

        await setDoc(doc(db, 'challenges', challengeId), newChallenge);

        if (createModal) createModal.hidden = true;
        createForm.reset();

        // Open Share Modal
        const shareModal = $('#share-challenge-modal');
        if (shareModal) {
          $('#share-code-display').textContent = randCode;
          const shareUrl = `${window.location.origin}${window.location.pathname}#/challenge/${challengeId}`;
          const linkInput = $('#share-link-input');
          if (linkInput) linkInput.value = shareUrl;

          const copyLinkBtn = $('#btn-copy-share-link');
          if (copyLinkBtn) {
            copyLinkBtn.onclick = () => {
              navigator.clipboard.writeText(shareUrl).then(() => {
                copyLinkBtn.textContent = 'Copied! ✓';
                setTimeout(() => { copyLinkBtn.textContent = 'Copy Link 📋'; }, 2000);
              });
            };
          }

          const startNowBtn = $('#btn-start-shared-challenge');
          if (startNowBtn) {
            startNowBtn.onclick = () => {
              shareModal.hidden = true;
              location.hash = '#/challenge/' + challengeId;
            };
          }

          shareModal.hidden = false;
        }

        await loadChallengeDashboard();
      } catch (err) {
        console.error('Error creating challenge:', err);
        alert('Could not create challenge. Please check your connection.');
      } finally {
        if (submitBtn) {
          submitBtn.disabled = false;
          submitBtn.textContent = 'Launch & Get Challenge Link 🚀';
        }
      }
    };
  }

  // Close Share Modal
  const closeShareBtn = $('#btn-close-share-modal');
  if (closeShareBtn) {
    closeShareBtn.onclick = () => {
      const shareModal = $('#share-challenge-modal');
      if (shareModal) shareModal.hidden = true;
    };
  }

  // Join via code
  const joinBtn = $('#btn-join-challenge');
  const joinInput = $('#join-challenge-input');
  async function handleJoinByCode() {
    if (!joinInput) return;
    const inputCode = joinInput.value.trim().toUpperCase();
    if (!inputCode) {
      alert('Please enter a challenge code (e.g. CHAL-2024).');
      return;
    }

    joinBtn.textContent = 'Searching…';
    joinBtn.disabled = true;

    try {
      let match = cachedChallenges.find(c => c.code.toUpperCase() === inputCode);
      if (!match) {
        const snap = await getDocs(collection(db, 'challenges'));
        snap.forEach(d => {
          const data = d.data();
          if (data.code && data.code.toUpperCase() === inputCode) {
            match = data;
          }
        });
      }

      if (match) {
        joinInput.value = '';
        location.hash = '#/challenge/' + match.challengeId;
      } else {
        alert(`No challenge found with code "${inputCode}". Please verify the code.`);
      }
    } catch (err) {
      console.error('Error finding challenge:', err);
      alert('Could not find challenge. Please try again.');
    } finally {
      joinBtn.textContent = 'Join →';
      joinBtn.disabled = false;
    }
  }

  if (joinBtn) joinBtn.onclick = () => handleJoinByCode();
  if (joinInput) {
    joinInput.onkeydown = e => {
      if (e.key === 'Enter') handleJoinByCode();
    };
  }

  // Times up modal
  const timesUpModal = $('#challenge-times-up-modal');
  const timesUpResultsBtn = $('#btn-times-up-view-results');
  if (timesUpResultsBtn && timesUpModal) {
    timesUpResultsBtn.onclick = () => {
      timesUpModal.hidden = true;
      submitExam();
    };
  }
}

// Data Loader
async function initArchive() {
  $('#stats').textContent = 'Loading past paper archive…';
  try {
    const res = await fetch('/data/all_questions.json');
    if (!res.ok) throw new Error('Could not load all_questions.json');
    const allQs = await res.json();
    S.q = allQs;
  } catch (err) {
    console.warn('Fallback: loading 2008.txt directly', err);
    try {
      const textRes = await fetch('/data/years/2008.txt');
      const text = await textRes.text();
      let y, g, o = [];
      for (let b of text.replace(/\r/g, '').split(/\n\s*\n/)) {
        let m = b.match(/^YEAR:\s*(\d{4})/m);
        if (m) { y = +m[1]; continue; }
        m = b.match(/^\[([^|\]]+)\s*\|\s*Unit:\s*([^|\]]+)\s*\|\s*Topic:\s*([^\]]+)\]/m);
        if (m) g = { subject: m[1].trim(), unit: m[2].trim(), topic: m[3].trim() };
        let q = b.match(/Q\.(\d+)\.\s*([\s\S]*?)(?=\nA\.\s)/),
            a = [...b.matchAll(/^([A-E])\.\s*(.*)$/gm)];
        if (q && g && y && a.length > 1) {
          o.push({
            id: +q[1],
            year: y,
            ...g,
            stem: q[2].trim(),
            options: a.map(opt => ({ label: opt[1], text: opt[2] })),
            a: a
          });
        }
      }
      S.q = o;
    } catch (e2) {
      console.error('Final fallback error:', e2);
      $('#stats').textContent = 'Unable to load past papers. Please refresh.';
      return;
    }
  }

  const ys = new Set(S.q.map(x => x.year));
  const units = new Set(S.q.map(x => x.unit));
  $('#stats').innerHTML = `
    <div class="stat"><strong>${S.q.length.toLocaleString()}</strong><small>IMPORTED MCQs</small></div>
    <div class="stat"><strong>${ys.size}</strong><small>AVAILABLE YEARS</small></div>
    <div class="stat"><strong>${units.size}</strong><small>PMDC UNITS</small></div>
  `;

  initChallengeModeUI();
  run();
  route();
}

// Router
function route() {
  const path = location.hash.slice(1) || '/';

  if (!path.startsWith('/past-papers/') && !path.startsWith('/practice/') && !path.startsWith('/challenge/')) {
    stopTimer();
    activeSetKey = '';
    isChallengeMode = false;
    activeChallenge = null;
  }

  for (const selector of ['.hero', '#years', '#units', '#questions', '#about']) {
    const el = $(selector);
    if (el) el.hidden = true;
  }

  let title = 'Home', active = '/';
  if (path === '/' || path === 'top') {
    run();
    $('.hero').hidden = false;
    loadPracticeDashboard();
    loadChallengeDashboard();
  } else if (path === '/past-papers' || path === 'years') {
    run();
    $('#years').hidden = false;
    title = 'Past Papers';
    active = '/past-papers';
  } else if (path === '/practice' || path === 'units') {
    run();
    $('#units').hidden = false;
    title = 'Unit-wise Practice';
    active = '/practice';
  } else if (path === '/challenges' || path === 'challenges') {
    run();
    $('.hero').hidden = false;
    title = 'Challenge Mode & Live Leaderboard';
    active = '/challenges';
    const cDash = $('#challenge-dashboard');
    if (cDash) {
      setTimeout(() => {
        cDash.scrollIntoView({ behavior: 'smooth', block: 'start' });
      }, 100);
    }
  } else if (path.startsWith('/challenge/')) {
    const challengeId = path.split('/')[2];
    title = 'MDCAT Timed Challenge';
    active = '/challenges';
    startChallenge(challengeId);
  } else if (path === '/about' || path === 'about') {
    $('#about').hidden = false;
    title = 'About';
    active = '/about';
  } else if (path.startsWith('/past-papers/')) {
    const year = Number(path.split('/')[2]);
    const qs = S.q.filter(q => q.year === year);
    active = '/past-papers';
    title = 'MDCAT ' + year + ' Full Exam Paper';
    const paperSessionKey = 'paper:' + year;
    show(qs, title, 'UHS / PMDC MDCAT · ' + year + ' FULL PAPER (' + qs.length + ' MCQs)', paperSessionKey);
    if (!qs.length) {
      $('#question-count').textContent = 'This paper is not available. Choose an uploaded year from Past Papers.';
    }
  } else if (path.startsWith('/practice/')) {
    let parts;
    try { parts = path.split('/').slice(2).map(decodeURIComponent); } catch { parts = []; }
    const [subject, unit] = parts;
    const qs = S.q.filter(q => (subject === 'All' || q.subject === subject) && q.unit === unit);
    title = unit || 'Unit not found';
    active = '/practice';
    const unitSessionKey = `unit:${subject || 'All'}:${unit}`;
    show(qs, title, 'PMDC UNIT PRACTICE / ' + (subject || 'All') + ' (' + qs.length + ' MCQs)', unitSessionKey);
  } else {
    $('#years').hidden = false;
    title = 'Past Papers';
    active = '/past-papers';
  }

  document.title = title + ' | Myelin MDCAT';
  document.querySelectorAll('.topbar nav a').forEach(link => {
    if (link.getAttribute('href') === '#' + active) link.setAttribute('aria-current', 'page');
    else link.removeAttribute('aria-current');
  });

  window.scrollTo(0, 0);
}

window.addEventListener('hashchange', route);
initArchive();
