import re
import json
import os

VALID_SUBJECTS_PRE_2022 = ["Biology", "Chemistry", "Physics", "English"]
VALID_SUBJECTS_POST_2022 = ["Biology", "Chemistry", "Physics", "English", "Logical Reasoning"]

def classify_subject(year, raw_subject, raw_unit, raw_topic, stem, options):
    year = int(year)
    s = raw_subject.strip() if raw_subject else ""
    full_text = (stem + " " + " ".join(o.get("text", "") for o in options)).lower()
    
    # Check Logical Reasoning strictly for 2022+
    if year >= 2022:
        lr_patterns = [
            r"all\s+\w+\s+are\s+\w+", r"some\s+\w+\s+are\s+\w+", r"no\s+\w+\s+are\s+\w+",
            r"statement\s*i\s*is\s*the\s*cause", r"cause\s+and\s+effect", r"courses\s+of\s+action",
            r"who\s+copied\s+", r"select\s+the\s+next\s+term\s+in\s+the\s+sequence",
            r"what\s+will\s+come\s+next\?\s*1,\s*4,\s*2", r"cab,\s*fae,\s*iah", r"sssss,\s*ssrss",
            r"how\s+many\s+trees\s+are\s+in\s+the\s+orchard", r"one\s+apple\s+pie\s+has\s+10\s+slices",
            r"queen\s+elizabeth\s+ii", r"read\s+the\s+passage\s+and\s+the\s+following\s+statements\s+below",
            r"pakistan\s+is\s+rich\s+in\s+wildlife\s+and\s+culture", r"p,\s*q\s*and\s*r\s*are\s*m’s\s*parents",
            r"p,\s*q\s*and\s*r\s*are\s*one-digit", r"x,\s*y\s*and\s*z\s*are\s*three\s*whole\s*numbers",
            r"conclusions?[\s\S]*?(follow|necessarily true)"
        ]
        for pat in lr_patterns:
            if re.search(pat, full_text):
                return "Logical Reasoning"
    
    # If tagged as Logical Reasoning before 2022, reclassify to Physics/Chemistry/Biology/English
    if year < 2022 and s == "Logical Reasoning":
        s = "Unclassified"

    # Physics keywords
    physics_keywords = [
        "velocity", "acceleration", "projectile", "momentum", "angular", "torque", "inertia",
        "wavelength", "frequency", "doppler", "sound wave", "speed of light", "refraction", "diffraction",
        "electric field", "magnetic field", "capacitance", "capacitor", "current", "resistor", "resistance",
        "solenoid", "transformer", "emf", "faraday", "lenz", "coulomb", "ohm", "joule", "watt",
        "thermodynamics", "isothermal", "adiabatic", "half-life", "radioactive", "alpha particle", "beta particle",
        "gamma ray", "decay constant", "photoelectric", "compton", "x-ray", "laser", "diode", "rectification",
        "stokes", "bernoulli", "viscosity", "terminal velocity", "fluid", "simple harmonic", "pendulum",
        "mass-spring", "young's modulus", "stress", "strain", "logic gate", "nand gate", "de-broglie"
    ]

    # Chemistry keywords
    chemistry_keywords = [
        "orbital", "electron configuration", "mole", "molar", "stoichiometry", "empirical formula",
        "avogadro", "enthalpy", "exothermic", "endothermic", "chemical equilibrium", "le chatelier",
        "reaction rate", "activation energy", "catalyst", "alkane", "alkene", "alkyne", "benzene",
        "alcohol", "phenol", "aldehyde", "ketone", "carboxylic", "ester", "acyl", "polymer", "polystyrene",
        "pvc", "nylon", "periodic table", "oxidation state", "redox", "cathode", "anode", "galvanic",
        "electrolytic", "buffer", "ph of", "ksp", "dipole moment", "electronegativity", "sp3", "sp2",
        "hybridization", "haber", "sulfuric acid", "nitric acid", "iodoform", "tollen"
    ]

    # Biology keywords
    biology_keywords = [
        "cell", "nucleus", "organelle", "mitochondria", "ribosome", "lysosome", "chloroplast", "membrane",
        "dna", "rna", "chromosome", "gene", "allele", "mitosis", "meiosis", "enzyme", "protein", "amino acid",
        "carbohydrate", "glucose", "glycogen", "starch", "lipid", "fatty acid", "bacteria", "virus", "hiv",
        "aids", "phage", "respiration", "glycolysis", "krebs", "photosynthesis", "chlorophyll", "heart",
        "blood", "lymph", "artery", "vein", "neuron", "nerve", "synapse", "brain", "cerebrum", "cerebellum",
        "medulla", "hormone", "pituitary", "insulin", "glucagon", "kidney", "nephron", "urea", "urine",
        "muscle", "sarcomere", "myosin", "actin", "skeleton", "bone", "cartilage", "joint", "reproduction",
        "sperm", "ovary", "ovum", "menstrual", "testis", "evolution", "darwin", "lamarck", "ecology",
        "ecosystem", "immunity", "antibody", "antigen", "lymphocyte"
    ]

    # English keywords
    english_keywords = [
        "synonym", "antonym", "meaning of", "nearest meaning", "spot the error", "correct sentence",
        "grammatically correct", "punctuated", "spelling", "preposition", "fill in the blank",
        "underlined", "passive voice", "direct speech", "indirect speech", "narrations", "idiom"
    ]

    # Check if raw_subject matches a valid subject
    valid_list = VALID_SUBJECTS_POST_2022 if year >= 2022 else VALID_SUBJECTS_PRE_2022
    if s in valid_list and s != "Unclassified":
        # Check for obvious cross-domain mismatch
        # e.g., Biology question placed in English
        if s == "English":
            # Is this actually Biology/Chemistry/Physics?
            bio_hits = sum(1 for k in biology_keywords if k in full_text)
            chem_hits = sum(1 for k in chemistry_keywords if k in full_text)
            phy_hits = sum(1 for k in physics_keywords if k in full_text)
            eng_hits = sum(1 for k in english_keywords if k in full_text)
            
            if eng_hits == 0 and (bio_hits >= 2 or chem_hits >= 2 or phy_hits >= 2):
                if bio_hits > chem_hits and bio_hits > phy_hits:
                    return "Biology"
                elif chem_hits > phy_hits:
                    return "Chemistry"
                else:
                    return "Physics"
        return s

    # Count hits
    bio_score = sum(1 for k in biology_keywords if k in full_text)
    chem_score = sum(1 for k in chemistry_keywords if k in full_text)
    phy_score = sum(1 for k in physics_keywords if k in full_text)
    eng_score = sum(1 for k in english_keywords if k in full_text)

    # Check unit/topic hints
    meta_text = (raw_unit + " " + raw_topic).lower()
    if "formal and lexical" in meta_text or "reading and thinking" in meta_text or "vocabulary" in meta_text or "grammar" in meta_text:
        if bio_score < 2 and chem_score < 2 and phy_score < 2:
            return "English"
    if "biological" in meta_text or "cell" in meta_text or "genetics" in meta_text or "organism" in meta_text:
        return "Biology"
    if "chemical" in meta_text or "hydrocarbon" in meta_text or "organic" in meta_text or "acid" in meta_text or "equilibrium" in meta_text:
        return "Chemistry"
    if "wave" in meta_text or "motion" in meta_text or "current" in meta_text or "radiation" in meta_text or "thermodynamics" in meta_text:
        return "Physics"

    scores = [("Biology", bio_score), ("Chemistry", chem_score), ("Physics", phy_score), ("English", eng_score)]
    scores.sort(key=lambda x: x[1], reverse=True)
    if scores[0][1] > 0:
        return scores[0][0]
        
    return "Biology"  # fallback default

def parse_year_text(year, text):
    lines = text.replace('\r', '').split('\n')
    questions = []
    
    current_meta = {"subject": "Unclassified", "unit": "General", "topic": "General"}
    current_q = None
    
    i = 0
    while i < len(lines):
        line = lines[i].strip()
        if not line:
            i += 1
            continue
            
        # Section header check (e.g., in 2020: PHYSICS, CHEMISTRY, BIOLOGY, ENGLISH)
        if line.upper() in ["PHYSICS", "CHEMISTRY", "BIOLOGY", "ENGLISH"]:
            sub = line.capitalize()
            current_meta = {"subject": sub, "unit": f"{sub} Practice", "topic": f"{sub} Unit"}
            i += 1
            continue
            
        # Metadata header [Subject | Unit: ... | Topic: ...]
        m_tag = re.match(r"^\[\s*([^|\]]+)\s*\|\s*Unit:\s*([^|\]]+)\s*\|\s*Topic:\s*([^\]]+)\]", line)
        if m_tag:
            current_meta = {
                "subject": m_tag.group(1).strip(),
                "unit": m_tag.group(2).strip(),
                "topic": m_tag.group(3).strip()
            }
            i += 1
            continue
            
        # Question stem Q.001. or Q.1. or 1.
        m_q = re.match(r"^(?:Q\.\s*(\d+)[\.\:]?|(\d+)[\.\:]\s*)\s*(.*)", line, re.IGNORECASE)
        if m_q:
            if current_q:
                # Classify subject
                current_q["subject"] = classify_subject(
                    year, current_q["raw_subject"], current_q["unit"], current_q["topic"],
                    current_q["stem"], current_q["options"]
                )
                del current_q["raw_subject"]
                questions.append(current_q)
                
            q_num = int(m_q.group(1) or m_q.group(2))
            stem_first = (m_q.group(3) or "").strip()
            current_q = {
                "id": len(questions) + 1,
                "original_number": q_num,
                "raw_subject": current_meta["subject"],
                "unit": current_meta["unit"],
                "topic": current_meta["topic"],
                "stem": stem_first,
                "options": []
            }
            i += 1
            continue
            
        # Options A. ... or - **A. ...**
        m_opt = re.match(r"^(?:-\s*\*\*)?([A-E])[\.\:]\s*(?:\*\*)?\s*(.*)", line)
        if m_opt and current_q:
            label = m_opt.group(1).upper()
            txt = m_opt.group(2).replace('✓', '').replace('**', '').strip()
            current_q["options"].append({"label": label, "text": txt})
            i += 1
            continue
            
        # If inside a question and not an option or new tag, append to stem
        if current_q and len(current_q["options"]) == 0:
            if not line.startswith("="):
                current_q["stem"] += " " + line
                
        i += 1
        
    if current_q:
        current_q["subject"] = classify_subject(
            year, current_q["raw_subject"], current_q["unit"], current_q["topic"],
            current_q["stem"], current_q["options"]
        )
        del current_q["raw_subject"]
        questions.append(current_q)
        
    return questions

def save_year_json(year, questions):
    out_dir = os.path.join(os.getcwd(), "data", "years")
    os.makedirs(out_dir, exist_ok=True)
    out_path = os.path.join(out_dir, f"{year}.json")
    with open(out_path, "w", encoding="utf-8") as f:
        json.dump({
            "year": int(year),
            "total": len(questions),
            "questions": questions
        }, f, indent=2, ensure_ascii=False)
    print(f"Saved {year}: {len(questions)} MCQs to {out_path}")
