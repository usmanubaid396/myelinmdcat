import os
import sys
sys.path.append(os.path.dirname(__file__))
from parser_helper import parse_year_text, save_year_json

RAW_2010 = """
[English | Unit: Formal and Lexical Skills | Topic: Vocabulary, sentence correction and usage]
Q.001. My advice had no _ on him.
A. Effect
B. Affect
C. Influence
D. Impression

[English | Unit: Formal and Lexical Skills | Topic: Vocabulary, sentence correction and usage]
Q.002. Do not lose heart, it is just a _ in the teacup.
A. Wind
B. Cyclone
C. Blast
D. Storm

[English | Unit: Formal and Lexical Skills | Topic: Vocabulary, sentence correction and usage]
Q.003. Pakistan _ from voting against Iran in the United Nations.
A. Prevented
B. Detained
C. Abstained
D. Refuse

[English | Unit: Formal and Lexical Skills | Topic: Vocabulary, sentence correction and usage]
Q.004. Please _ the door after you.
A. Close
B. Shut
C. Leave
D. Knock

[English | Unit: Formal and Lexical Skills | Topic: Vocabulary, sentence correction and usage]
Q.005. Spot the error : In the following sentences, some segments of each sentence are underlined.Your task is to identify that underlined segment of the sentence, which contains the mistake that needs to be corrected.Suddenly, he stopped at the edge of the meadow, taking his pocket knife from his pocket, and cut a wisp of alfalfa.
A. Suddenly, he stopped
B. Taking his pocket knife from his pocket
C. His pocket
D. Cut a wisp of alfalfa

[English | Unit: Formal and Lexical Skills | Topic: Vocabulary, sentence correction and usage]
Q.006. Spot the error : In the following sentences, some segments of each sentence are underlined.Your task is to identify that underlined segment of the sentence, which contains the mistake that needs to be corrected.The study of population growth indicates one of the greatest paradox of our time.
A. The study
B. Population growth
C. One of the
D. Paradox

[English | Unit: Formal and Lexical Skills | Topic: Vocabulary, sentence correction and usage]
Q.007. Spot the error : In the following sentences, some segments of each sentence are underlined. Your task is to identify that underlined segment of the sentence, which contains the mistake that needs to be corrected.Among the Western nations, the decline in the death rate is followed after an interval by the reduction in the birth rate, so that the population is not now growing so fast.
A. Among the Western nations
B. Death rate is followed
C. The reduction in the birth
D. Is not now growing

[English | Unit: Formal and Lexical Skills | Topic: Vocabulary, sentence correction and usage]
Q.008. Spot the error : In the following sentences, some segments of each sentence are underlined. Your task is to identify that underlined segment of the sentence, which contains the mistake that needs to be corrected.In view of increasing hazards with our national security it is the duty of every citizen to keep a watch on his surroundings.
A. With
B. It is
C. To keep
D. On his surroundings

[English | Unit: Formal and Lexical Skills | Topic: Vocabulary, sentence correction and usage]
Q.009. Spot the error : In the following sentences, some segments of each sentence are underlined. Your task is to identify that underlined segment of the sentence, which contains the mistake that needs to be corrected.Thrifty housewives preserved their homegrown vegetables and fruits in canning, pickling or drying them for use during the cold weather.
A. In
B. Or
C. For
D. The

[English | Unit: Formal and Lexical Skills | Topic: Vocabulary, sentence correction and usage]
Q.010. Spot the error : In the following sentences, some segments of each sentence are underlined. Your task is to identify that underlined segment of the sentence, which contains the mistake that needs to be corrected.When a low-wage category worker finds he has to maintain a large family, his expenses may exceeds his income.
A. When a low-wage
B. Worker finds
C. Maintain a large family
D. Exceeds his income

[English | Unit: Formal and Lexical Skills | Topic: Vocabulary, sentence correction and usage]
Q.011. In each of the following question, four alternative sentences are given. Choose the correct one.
A. This is different to what had been expected.
B. This is different what had been expected.
C. This is different from what had been expected.
D. This is different to what would be expected.

[English | Unit: Formal and Lexical Skills | Topic: Vocabulary, sentence correction and usage]
Q.012. In each of the following questions, four alternative sentences are given. Choose the correct one.
A. When the fact failed him, he questions his senses.
B. When the fact failed him, he questioned from his senses.
C. When the fact fails him, he questions his senses.
D. He will question his senses, when the fact will fail him.

[English | Unit: Formal and Lexical Skills | Topic: Vocabulary, sentence correction and usage]
Q.013. In each of the following question, four alternative meanings of a word are given. You have to select the nearest correct meaning of the given word and fill the appropriateWallow
A. Roll about
B. Mock
C. Protest
D. Borrow

[English | Unit: Formal and Lexical Skills | Topic: Vocabulary, sentence correction and usage]
Q.014. In each of the following question, four alternative meanings of a word are given. You have to select the nearest correct meaning of the given word and fill the appropriate.Connoisseur
A. Guide
B. Artist
C. Expert critic of art
D. Teacher

[English | Unit: Formal and Lexical Skills | Topic: Vocabulary, sentence correction and usage]
Q.015. In each of the following question, four alternative meanings of a word are given. You have to select the nearest correct meaning of the given word and fill the appropriate.Eccentric
A. Lunatic
B. Stern
C. Upset
D. Odd

[English | Unit: Formal and Lexical Skills | Topic: Vocabulary, sentence correction and usage]
Q.016. In each of the following question, four alternative meanings of a word are given. You have to select the nearest correct meaning of the given word and fill the appropriate.Boulder
A. Rounded stone / hill
B. Builder
C. Magnanimity
D. Magnitude

[English | Unit: Formal and Lexical Skills | Topic: Vocabulary, sentence correction and usage]
Q.017. In each of the following question, four alternative meanings of a word are given. You have to select the nearest correct meaning of the given word and fill the appropriateSlumber
A. Heap
B. Humble
C. Knee
D. Sleep

[English | Unit: Formal and Lexical Skills | Topic: Vocabulary, sentence correction and usage]
Q.018. In each of the following question, four alternative meanings of a word are given. You have to select the nearest correct meaning of the given word and fill the appropriate.Excrement
A. Increment
B. Waste matter expelled from body
C. Excitement
D. Disagreement

[English | Unit: Formal and Lexical Skills | Topic: Vocabulary, sentence correction and usage]
Q.019. In each of the following question, four alternative meanings of a word are given. You have to select the nearest correct meaning of the given word and fill the appropriate.Visage
A. Vision
B. Illusion
C. Trunkless
D. A person’s face

[English | Unit: Formal and Lexical Skills | Topic: Vocabulary, sentence correction and usage]
Q.020. In each of the following question, four alternative meanings of a word are given. You have to select the nearest correct meaning of the given word and fill the appropriate.Felicity
A. Intense Happiness
B. Respite
C. Inspire
D. Sensational

[English | Unit: Formal and Lexical Skills | Topic: Vocabulary, sentence correction and usage]
Q.021. In each of the following question, four alternative meanings of a word are given. You have to select the nearest correct meaning of the given word and fill the appropriate.Enmeshed
A. Sojourn
B. Entangled
C. Gallows
D. Cascade

[English | Unit: Formal and Lexical Skills | Topic: Vocabulary, sentence correction and usage]
Q.022. In each of the following question, four alternative meanings of a word are given. You have to select the nearest correct meaning of the given word and fill the appropriate.Captivate
A. Hesitate
B. Concentrate
C. Hate
D. Fascinate

[Biology | Unit: Respiration | Topic: Human respiratory system]
Q.023. Book lungs are present in arthropods for exchange of gases in class:
A. Crustacea
B. Insecta
C. Myriapoda
D. Arachnida

[Biology | Unit: Evolution | Topic: Evolution and natural selection]
Q.024. Larvae of which group are similar to chordates?
A. Echinodermata
B. Annelida
C. Arthropoda
D. Nematoda

[Biology | Unit: Respiration | Topic: Human respiratory system]
Q.025. The type of respiration that involves the step-by-step breakdown of carbon chain molecules in the cell is called
A. External respiration
B. Pulmonary respiration
C. Cellular respiration
D. Cutaneous respiration

[Biology | Unit: Bioenergetics | Topic: Cellular respiration and photosynthesis]
Q.026. An instrument that is used to measure the relative abilities of different pigments to absorb different wavelengths of light is called
A. Spectrometer
B. Photometer
C. Barometer
D. Spectrophotometer

[Biology | Unit: Bioenergetics | Topic: Cellular respiration and photosynthesis]
Q.027. End products of yeast fermentation, bacterial fermentation, and anaerobic respiration are:
A. Ethyl alcohol, lactic acid, and carbon dioxide
B. Ethyl alcohol, lactic acid, carbon dioxide, and water
C. Glucose, oxygen, and water
D. Pyruvic acid, carbon dioxide, and oxygen

[Biology | Unit: Digestion | Topic: Human digestive system]
Q.028. In human beings, what is the function of amylase in digestion?
A. Digestion of triglycerides
B. Digestion of lipids
C. Digestion of all types of food
D. Digestion of carbohydrates

[Biology | Unit: Digestion | Topic: Human digestive system]
Q.029. Where is the ileocolic sphincter located in your body?
A. At the junction of esophagus and stomach
B. At the junction of stomach and small intestine
C. At the junction of ileum and large intestine
D. At the junction of small intestine and large intestine

[Biology | Unit: Digestion | Topic: Human digestive system]
Q.030. The term which is employed to the loss of appetite due to fear of becoming obese is:
A. Obesity
B. Anorexia nervosa
C. Dyspepsia
D. Bulimia nervosa

[Biology | Unit: Respiration | Topic: Human respiratory system]
Q.031. Which one of the following acts as functional unit of lungs in man?
A. Air sac
B. Trachea
C. Larynx
D. Bronchioles

[Biology | Unit: Circulation | Topic: Heart, blood and vessels]
Q.032. Which one of following factors is directly proportional to oxygen carrying capacity of haemoglobin:
A. Carbon dioxide
B. Temperature
C. pH
D. Light

[Biology | Unit: Respiration | Topic: Human respiratory system]
Q.033. Expiration in human beings is carried out by:
A. Contraction of lungs
B. Contraction of intercostal membrane
C. Relaxation of intercostal and diaphragm muscles
D. Contraction of diaphragm muscles

[Biology | Unit: Coordination and Control | Topic: Nervous system and receptors]
Q.034. Which one of the following is a precursor of steroid hormones?
A. Glycerol
B. Sterol
C. Amino acids
D. Cholesterol

[Biology | Unit: Support and Movement | Topic: Skeleton, muscles and joints]
Q.035. Granulocytes or white blood cells are produced in:
A. Lymph nodes
B. Red bone marrow
C. Tonsils
D. Spleen

[Biology | Unit: Circulation | Topic: Heart, blood and vessels]
Q.036. Which one of the following statements best describes the function of sinoatrial node?
A. It sends out electrical impulses to atrial muscles causing both atria to contract
B. It consists of small number of diffusely oriented cardiac fibres
C. It sends out electrical impulses to ventricular muscles causing both ventricles to contract
D. It is present at upper end of left atrium

[Biology | Unit: Circulation | Topic: Heart, blood and vessels]
Q.037. The flow of lymph in lymphatic vessels is maintained by:
A. Heart, activity of smooth muscles and valves
B. Activity of skeletal muscles, heart and breathing movements
C. Breathing movements, activity of skeletal muscles and valves
D. Exercise, breathing movements and heart

[Biology | Unit: Homeostasis | Topic: Kidney and osmoregulation]
Q.038. Metabolic waste from metabolism of nucleic acid is:
A. Uric acid
B. Creatine
C. Urea
D. Creatinine

[Biology | Unit: Digestion | Topic: Human digestive system]
Q.039. The central metabolic station and clearing house of a body is:
A. Liver
B. Kidney
C. Nephron
D. Glomerulus

[Biology | Unit: Homeostasis | Topic: Kidney and osmoregulation]
Q.040. The muscles that control urine in bladder are known as:
A. Striated muscles
B. Smooth muscles
C. Sphincter muscles
D. Circular muscles

[Biology | Unit: Support and Movement | Topic: Skeleton, muscles and joints]
Q.041. The living cells of cartilage are called:
A. Chrondrocytes
B. Osteoblasts
C. Ostecytes
D. Osteoclasts

[Biology | Unit: Support and Movement | Topic: Skeleton, muscles and joints]
Q.042. The disease which causes immobility and fusion of vertebral joints is:
A. Osteomalacia (soft bones)
B. Disc slip
C. Arthritis
D. Spondylosis

[Biology | Unit: Support and Movement | Topic: Skeleton, muscles and joints]
Q.043. During muscle contraction:
A. I-band shortens
B. Myosin filaments shorten
C. Actin filaments shorten
D. Z-line disappears

[Biology | Unit: Coordination and Control | Topic: Nervous system and receptors]
Q.044. Hormones are the organic compounds of varying structural complexity. Which of the following is not a function or property of these compounds?
A. They initiate new biochemical reactions
B. They are poured directly into blood
C. They may be proteins
D. They affect target cells

[Biology | Unit: Coordination and Control | Topic: Nervous system and receptors]
Q.045. Reflexes and instincts type of behaviours respond to which combinations?
A. Biological rhythms, territorial, courtship and development
B. The responses that do produce same result in different conditions
C. Aggression, mating and altruism
D. The responses that are predetermined like differentiation

[Biology | Unit: Coordination and Control | Topic: Nervous system and receptors]
Q.046. A typical neuron at rest:
A. Is more positive outside than inside
B. Is more negative outside than inside
C. Has no charge on either side
D. Has an equal charge on either side

[Biology | Unit: Reproduction | Topic: Human reproduction and menstrual cycle]
Q.047. The first cells produced by the repeated cell division of germinal epithelium of testis are:
A. Interstitial cells
B. Spermatogonia
C. Secondary spermatocytes
D. Spermatids

[Biology | Unit: Reproduction | Topic: Human reproduction and menstrual cycle]
Q.048. Which of the following sequence is correct?
A. LH → FSH → Estrogen → Progesterone
B. FSH → LH → Progesterone → Estrogen
C. FSH → Estrogen → Progesterone → LH
D. FSH → Estrogen → LH → Progesterone

[Biology | Unit: Inheritance | Topic: Mendelian and sex-linked inheritance]
Q.049. Which chromosomal abnormality in humans causes aggressive and antisocial behavior?
A. XO
B. XXY
C. XYY
D. XXX

[Biology | Unit: Cell Structure and Function | Topic: Cells, organelles and chromosomes]
Q.050. Grey equatorial cytoplasm produces:
A. Muscle cells
B. Gut
C. Notochord and neural tube
D. Larval epidermis

[Biology | Unit: Inheritance | Topic: Mendelian and sex-linked inheritance]
Q.051. Sickle cell Anaemia is an example of which type of chromosomal defect?
A. Chromosomal rearrangement
B. Transposition of gene
C. Chromosomal aberration
D. Point mutation

[Biology | Unit: Cell Structure and Function | Topic: Cells, organelles and chromosomes]
Q.052. The karyotype of an individual is _ of chromosomes.
A. Number
B. Types
C. Number, types and chemical composition
D. Number and types

[Biology | Unit: Biological Molecules | Topic: Carbohydrates, proteins, lipids and nucleic acids]
Q.053. The process of replication of DNA begins at:
A. One place only without any specific sequence of DNA
B. One or more places without any specific sequence of DNA
C. Any place with the uncoiling of two strands of DNA
D. One or more places where there is a specific sequence of nucleotides

[Biology | Unit: Biological Molecules | Topic: Carbohydrates, proteins, lipids and nucleic acids]
Q.054. Amino acid attaches at which site of RNA:
A. Anticodon site
B. Ribosomes recognition site
C. 3’-site with terminal OH
D. Activation enzyme recognition site

[Biology | Unit: Biological Molecules | Topic: Carbohydrates, proteins, lipids and nucleic acids]
Q.055. Microtubules of spindle fibres are composed of a protein called
A. Tubulin
B. Actin
C. Myosin
D. Troponin

[Biology | Unit: Cell Structure and Function | Topic: Cells, organelles and chromosomes]
Q.056. The kinetochore fibres contract and spindle or pole fibres elongate during:
A. Prophase I
B. Metaphase I
C. Telophase I
D. Anaphase I

[Biology | Unit: Cell Structure and Function | Topic: Cells, organelles and chromosomes]
Q.057. Cell death due to tissue damage is called:
A. Necrosis
B. Metastasis
C. Apoptosis
D. Epistasis

[Biology | Unit: Inheritance | Topic: Mendelian and sex-linked inheritance]
Q.058. When a disease is transmitted directly from an affected father to his son, it is called:
A. X-linked
B. Autosomal
C. Y-linked
D. X and Y-linked

[Biology | Unit: Inheritance | Topic: Mendelian and sex-linked inheritance]
Q.059. Epistasis is a relationship between:
A. Alleles of a gene
B. Two different genes at the same locus
C. Two contrasting traits
D. Two different genes at different loci

[Biology | Unit: Cell Structure and Function | Topic: Cells, organelles and chromosomes]
Q.060. Gene for albinism in man is present on chromosome number:
A. 11
B. 22
C. 21
D. 12

[Biology | Unit: Biological Molecules | Topic: Carbohydrates, proteins, lipids and nucleic acids]
Q.061. Gene can be synthesized in laboratory from messenger RNA by using:
A. Restriction enzymes
B. cDNA (complementary DNA)
C. Vector
D. Reverse transcriptase

[Biology | Unit: Biotechnology | Topic: Genetic engineering and applications]
Q.062. Antibiotic resistance gene for tetracycline and ampicillin are present in the plasmid:
A. pSC 101
B. pCR 101
C. pBR 322
D. pBR 233

[Biology | Unit: Biotechnology | Topic: Genetic engineering and applications]
Q.063. Cloning is a form of:
A. Parthenogenesis
B. Sexual Reproduction
C. Apomixis
D. Asexual Reproduction

[Biology | Unit: Evolution | Topic: Evolution and natural selection]
Q.064. Group of interbreeding individuals of particular species, sharing common geographical area is called:
A. Population
B. Community ecology
C. Community
D. Autecology

[Biology | Unit: Evolution | Topic: Evolution and natural selection]
Q.065. Which of the following proteins is common in man and aerobic bacteria?
A. Haemoglobin
B. Myoglobin
C. Cytochrome c
D. Pilin

[Biology | Unit: Bioenergetics | Topic: Cellular respiration and photosynthesis]
Q.066. Ozone filters ultraviolet radiations from the sun in the upper:
A. Biosphere
B. Atmosphere
C. Lithosphere
D. Hydrosphere

[Biology | Unit: Acellular Life | Topic: Viruses and HIV/AIDS]
Q.067. A parasite living inside body of the host is called:
A. Ectoparasite
B. Obligate parasite
C. Facultative parasite
D. Endoparasite

[Biology | Unit: Biological Molecules | Topic: Carbohydrates, proteins, lipids and nucleic acids]
Q.068. The non-protein part of enzyme which is covalently and permanently bonded is called
A. Prosthetic Group
B. Co-Factor
C. Coenzyme
D. Activator

[Biology | Unit: Biological Molecules | Topic: Carbohydrates, proteins, lipids and nucleic acids]
Q.069. One of the pyrimidine bases is absent in DNA:
A. Uracil
B. Thymine
C. Cytosine
D. Adenine

[Biology | Unit: Acellular Life | Topic: Viruses and HIV/AIDS]
Q.070. Which one of the following diseases caused by enveloped RNA virus and spread in epidemic form?
A. Influenza
B. Herpes Simplex
C. Polio
D. Smallpox

[Biology | Unit: Acellular Life | Topic: Viruses and HIV/AIDS]
Q.071. The structure that contains the gene responsible for drug resistance in bacteria is:
A. Nucleoids
B. Mesosomes
C. Chromatin Bodies
D. Plasmids

[Biology | Unit: Immunity | Topic: Immune response and vaccination]
Q.072. Antibiotics that kill microbes immediately are called:
A. Microbistatic
B. Microbicidal
C. Biostatic
D. Chemotherapeutic

[Biology | Unit: Acellular Life | Topic: Viruses and HIV/AIDS]
Q.073. Which one of the following fungi causes vaginal thrush?
A. Candida
B. Aspergillus
C. Tortula
D. Penicillium

[Biology | Unit: Support and Movement | Topic: Skeleton, muscles and joints]
Q.074. Body cavity of roundworms is called:
A. Pseudocoelom
B. Coelom
C. Acoelom
D. Enteron

[Biology | Unit: Digestion | Topic: Human digestive system]
Q.075. Fasciola is endoparasite of:
A. Colon
B. Small Intestine
C. Liver
D. Bile Duct

[Biology | Unit: Acellular Life | Topic: Viruses and HIV/AIDS]
Q.076. Trypanosoma is transmitted in human beings by:
A. Plasmodium
B. House Fly
C. Anopheles
D. Tsetse Fly

[Biology | Unit: Reproduction | Topic: Human reproduction and menstrual cycle]
Q.077. The nervous system develops from which of the following layer during embryonic development of animals?
A. Mesoderm
B. Ectoderm
C. Endoderm
D. Mesoderm and Endoderm

[Biology | Unit: Reproduction | Topic: Human reproduction and menstrual cycle]
Q.078. Endosperm is formed as a result of:
A. Pollination
B. Self-Pollination
C. Double Fertilisation
D. Cross Pollination

[Biology | Unit: Enzymes | Topic: Enzymes and inhibition]
Q.079. Which of the following enzyme is released in an inactive form:
A. Amylase
B. Lipase
C. Enterokinase
D. Pepsin

[Biology | Unit: Digestion | Topic: Human digestive system]
Q.080. Which of the following hormones stimulate the secretion of pancreatic juice from pancreas in the liver?
A. Secretin
B. Pepsinogen
C. Gastrin
D. Both Gastrin and Secretin

[Biology | Unit: Digestion | Topic: Human digestive system]
Q.081. In large intestine, vitamin K is formed by the activity of:
A. Symbiotic Bacteria
B. Obligate Bacteria
C. Parasitic Bacteria
D. Facultative Bacteria

[Biology | Unit: Digestion | Topic: Human digestive system]
Q.082. During swallowing of food which structure closes the nasal opening?
A. Hard Palate
B. Soft Palate
C. Epiglottis
D. Larynx

[Biology | Unit: Circulation | Topic: Heart, blood and vessels]
Q.083. The right atrium of the heart usually receives the
A. Deoxygenated Blood
B. Oxygenated Blood
C. Filtered Blood
D. Non-Filtered Blood

[Biology | Unit: Circulation | Topic: Heart, blood and vessels]
Q.084. The largest lymph duct called thoracic lymph duct drains into:
A. Subclavian Vein
B. Renal Vein
C. Pulmonary Vein
D. Hepatic Portal Vein

[Biology | Unit: Biological Molecules | Topic: Carbohydrates, proteins, lipids and nucleic acids]
Q.085. Which protein plays a major role in maintaining osmotic balance?
A. Albumin
B. Globulin
C. Fibrinogen
D. Prothrombin

[Biology | Unit: Circulation | Topic: Heart, blood and vessels]
Q.086. The type of agranulocytes which stays in blood for a few hours and then enters tissues and become macrophages are:
A. Lymphocytes
B. Monocyte
C. Eosinophils
D. Basophils

[Biology | Unit: Biological Molecules | Topic: Carbohydrates, proteins, lipids and nucleic acids]
Q.087. Reabsorption of water by countercurrent multiplier mechanism takes place at:
A. Proximal Tubule
B. Distal Tubule
C. Collecting Duct
D. Loop of Henle

[Biology | Unit: Biological Molecules | Topic: Carbohydrates, proteins, lipids and nucleic acids]
Q.088. Antiduretic hormone helps in reabsorption of water by changing permeability of:
A. Proximal Tubule
B. Distal Tubule
C. Collecting Duct
D. Loop of Henle

[Biology | Unit: Digestion | Topic: Human digestive system]
Q.089. During peritoneal dialysis, dialysis fluid is introduced into which part of the human body?
A. Liver
B. Abdomen
C. Kidney
D. Pancreas

[Biology | Unit: Digestion | Topic: Human digestive system]
Q.090. Aldosterone helps in conservation or active absorption of:
A. Sodium
B. Calcium
C. Potassium
D. Bicarbonate Ions

[Biology | Unit: Homeostasis | Topic: Kidney and osmoregulation]
Q.091. Maximum reabsorption takes place in which part of the nephron?
A. Distal Tubule
B. Villi
C. Cortical Tissue
D. Proximal Tubule

[Chemistry | Unit: Electrochemistry | Topic: Redox and electrochemical cells]
Q.092. In an electrochemical series, standard electrode potentials are arranged on the basis of:
A. pH scale
B. pOH scale
C. Hydrogen Scale
D. pKa scale

[Chemistry | Unit: Electrochemistry | Topic: Redox and electrochemical cells]
Q.093. The reaction which is responsible for the production of electricity in the voltaic cell is:
A. Hydrolysis reaction
B. Oxidation reaction
C. Redox reaction
D. Reduction reaction

[Chemistry | Unit: Macromolecules | Topic: Polymers and biomolecules]
Q.094. Glucose is converted into ethanol by the enzyme present in the yeast:
A. Urease
B. Zymase
C. Invertase
D. Sucrase

[Chemistry | Unit: Reaction Kinetics | Topic: Rate and activation energy]
Q.095. The rate of reaction involving ions can be studied by _ method.
A. Dilatometric
B. Refractometric
C. Optical rotation
D. Electrical conductivity

[Chemistry | Unit: Thermochemistry and Energetics | Topic: Heat, enthalpy and thermodynamics]
Q.096. When one mole of gaseous hydrogen ions are dissolved in water to form an infinitely dilute solution, the amount of heat liberated is:
A. -1891 kJmol-1
B. -1075 kJmol-1
C. -499 kJmol-1
D. -1562 kJmol-1

[Chemistry | Unit: Liquids and Solids | Topic: Intermolecular forces and states of matter]
Q.097. Energy required to remove an electron from the outermost shell of its isolated gaseous atom in the ground state is:
A. Electron affinity
B. Lattice energy
C. Ionization energy
D. Crystal energy

[Chemistry | Unit: S- and P-Block Elements | Topic: Periodic trends and main-group chemistry]
Q.098. Which of the following carbonates of alkali metals is not stable towards heat and is decomposed on heating to its oxide along with liberation of CO2?
A. Li2CO3
B. Mg2CO3
C. K2CO3
D. Na2CO3

[Chemistry | Unit: S- and P-Block Elements | Topic: Periodic trends and main-group chemistry]
Q.099. The presence of calcium is essential for the normal development of plants. An adequate supply of calcium appears to stimulate the development of which part of the plants?
A. Leaves
B. Fruits
C. Root hairs
D. Branches

[Chemistry | Unit: S- and P-Block Elements | Topic: Periodic trends and main-group chemistry]
Q.100. Which of the following sulphates is not soluble in water?
A. Sodium Sulphate
B. Barium Sulphate
C. Potassium Sulphate
D. Zinc Sulphate

[Chemistry | Unit: S- and P-Block Elements | Topic: Periodic trends and main-group chemistry]
Q.101. The trend in the densities of elements of Group III-A of the Periodic Table is
A. A gradual increase
B. A gradual decrease
C. First decrease then increase
D. First increase then decrease

[Chemistry | Unit: S- and P-Block Elements | Topic: Periodic trends and main-group chemistry]
Q.102. White lead has one of the following properties:
A. Acidic
B. Crystalline
C. Amorphous
D. Neutral

[Chemistry | Unit: S- and P-Block Elements | Topic: Periodic trends and main-group chemistry]
Q.103. The strongest acid among the following is:
A. HF
B. HI
C. HCl
D. HBr

[Chemistry | Unit: S- and P-Block Elements | Topic: Periodic trends and main-group chemistry]
Q.104. The noble gas which is used in radiotherapy of cancer is
A. Radon
B. Xenon
C. Krypton
D. Argon

[Chemistry | Unit: Atomic Structure | Topic: Atomic models and electronic configuration]
Q.105. Paramagnetic behavior of an atom, ion or molecule is due to presence
A. Unpaired electrons
B. Paired electrons
C. Protons
D. Neutrons

[Chemistry | Unit: Chemical Bonding | Topic: Bonding and molecular shape]
Q.106. The geometry of the complexes depends upon the type of _ taking place in the valence shell of the central metal atom.
A. Hybridization
B. Protonation
C. Deprotonation
D. Dissociation

[Chemistry | Unit: Electrochemistry | Topic: Redox and electrochemical cells]
Q.107. KMnO4 acts as a/an:
A. Reducing agent
B. Excellent precipitating reagent
C. Germicide
D. Oxidizing agent

[Chemistry | Unit: Chemistry of Hydrocarbons | Topic: Alkanes, alkenes, alkynes and benzene]
Q.108. A gasoline of higher octane number can be obtained by:
A. Oxidative cleavage
B. Thermal cracking
C. Catalytic cracking
D. Steam cracking

[Chemistry | Unit: Chemistry of Hydrocarbons | Topic: Alkanes, alkenes, alkynes and benzene]
Q.109. Ethyne molecule is formed when two carbon atoms joined together to form a sigma bond by:
A. sp-s overlap
B. sp3-sp3 overlap
C. 2py-2py overlap
D. sp-sp overlap

[Chemistry | Unit: Electrochemistry | Topic: Redox and electrochemical cells]
Q.110. Symmetrical alkanes can be produced by:
A. Sabatier Sender’s Reaction
B. Hydrogenolysis Reaction
C. Reduction Reaction
D. Kolbe’s Electrolytic Reaction

[Chemistry | Unit: Reaction Kinetics | Topic: Rate and activation energy]
Q.111. The catalyst used for the preparation of acrylonitrile is:
A. Cu2Cl2 and NH4Cl
B. Al2O3 and NH4Cl
C. Cu2Cl2 and NH4OH
D. Cu2Cl2 and Al2O3

[Chemistry | Unit: Chemistry of Hydrocarbons | Topic: Alkanes, alkenes, alkynes and benzene]
Q.112. When a hydrogen atom is removed from benzene, the group left behind is called:
A. Alkyl group
B. Phenyl group
C. Benzyl group
D. Methyl group

[Chemistry | Unit: Chemistry of Hydrocarbons | Topic: Alkanes, alkenes, alkynes and benzene]
Q.113. The introduction of NO2 group in benzene ring is called ‘Nitration’. The nitration of benzene takes place when it is heated with a 1:1 mixture of _ at 50 oC-55 oC.
A. Conc. HNO3 and conc. HCl
B. Conc. HNO3 and conc. Acetic acid
C. Conc. HNO3 and H3PO4
D. Conc. HNO3 and conc. H2SO4

[Chemistry | Unit: Alkyl Halides | Topic: Nucleophilic substitution]
Q.114. During SN2 reactions, configuration of the alkyl halide molecule:
A. Gets inverted
B. Remains same
C. Depends upon the carbon atom
D. Depends upon the electronegativity of halide

[Chemistry | Unit: Alcohols and Phenols | Topic: Alcohol and phenol reactions]
Q.115. Grignard reagents are prepared by the reaction of magnesium metal with alkyl halides in the presence of:
A. Dry Ether
B. Alcohol
C. CS2
D. CCl4

[Chemistry | Unit: Reaction Kinetics | Topic: Rate and activation energy]
Q.116. Methanol is prepared from carbon monoxide and hydrogen. The catalyst used for this reaction is:
A. ZnO + CoO2
B. ZnO + CuO
C. ZnO + Ag2O
D. Cr2O3 + ZnO

[Chemistry | Unit: Reaction Kinetics | Topic: Rate and activation energy]
Q.117. Ethanol reacts with Ammonia to produce ethyl amine, the catalyst is
A. ZnCl2
B. ThO2
C. C6H5N
D. Cr2O3

[Chemistry | Unit: Alcohols and Phenols | Topic: Alcohol and phenol reactions]
Q.118. Dissociation constant of phenol is:
A. 1.2 x 10-10
B. 1.2 x 1010
C. 1.3 x 1010
D. 1.3 x 10-10

[Chemistry | Unit: Carboxylic Acids | Topic: Carboxylic acids and derivatives]
Q.119. Dry distillation of a mixture of calcium salts of formic acid and acetic acid results into the formation of:
A. Formaldehyde
B. Acetaldehyde
C. Calcium acetate
D. Sodium acetate

[Chemistry | Unit: Carboxylic Acids | Topic: Carboxylic acids and derivatives]
Q.120. Hydrolysis of cyano group by an aqueous acid results into:
A. Carboxylic Acid
B. Acid Amide
C. Cyanohydride
D. Formaldehyde

[Chemistry | Unit: Aldehydes and Ketones | Topic: Carbonyl compounds]
Q.121. Brick red precipitates are formed when aldehydes react with:
A. Sodium borohydride
B. Sodium bisulphite
C. Sodium nitroprusside
D. Fehling’s solution

[Chemistry | Unit: Macromolecules | Topic: Polymers and biomolecules]
Q.122. The nature of the amino acid ‘lysine’ is:
A. Neutral
B. Acidic
C. Amphoteric
D. Basic

[Chemistry | Unit: Carboxylic Acids | Topic: Carboxylic acids and derivatives]
Q.123. Which of the following compounds, in the form of aqueous solution, on reaction with sodium carbonate will produce carbon dioxide gas?
A. H3C-COO-C2H5
B. H3C2-COO-CH3
C. H3C2-CO-OH
D. H3C2-COO-C2H5

[Chemistry | Unit: Macromolecules | Topic: Polymers and biomolecules]
Q.124. Collagen and albumin are:
A. Simple proteins
B. Derived proteins
C. Polyamides
D. Polysaccharides

[Chemistry | Unit: Industrial Chemistry | Topic: Industrial processes and materials]
Q.125. Urea is produced by the reaction of liquid ammonia with:
A. CO2
B. CO
C. CaO
D. C

[Chemistry | Unit: Industrial Chemistry | Topic: Industrial processes and materials]
Q.126. The calcium sulpho-aluminate is:
A. Co.Al2O3.3CaSO4.6H2O
B. 3Ca.Al2O3.CaSO4.2H2O
C. 3Ca.Al2O3.3CaSO4.2H2O
D. 3Ca.Al2O3.3CaSO4.6H2O

[Chemistry | Unit: Industrial Chemistry | Topic: Industrial processes and materials]
Q.127. The coagulant used in raw water to precipitate suspended impurities is:
A. Caustic soda
B. Lime water
C. Alum
D. Soda ash

[Chemistry | Unit: Industrial Chemistry | Topic: Industrial processes and materials]
Q.128. The whiteness of the recycled newspaper is improved by treating it with:
A. Sodium hydroxide
B. Per oxides
C. Super oxides
D. Normal oxides

[Chemistry | Unit: Introduction to Chemistry | Topic: Stoichiometry and mole concept]
Q.129. One mole of any gas at standard temperature and pressure (STP) occupies a volume of:
A. 20.414 dm3
B. 22.414 dm3
C. 22.414 cm3
D. 23.414 dm3

[Chemistry | Unit: Atomic Structure | Topic: Atomic models and electronic configuration]
Q.130. The relative abundance of the isotopes of the elements can be determined by:
A. Mass Spectrometry
B. X-rays
C. Chromatography
D. Solvent Extraction

[Chemistry | Unit: Introduction to Chemistry | Topic: Stoichiometry and mole concept]
Q.131. If we are given the mass of one substance, we can calculate volume of other substances and vice a versa with the help of balanced chemical equation. This is called:
A. Mass-mass relationship
B. Mass-mole relationship
C. Mole-volume relationship
D. Mass-volume relationship

[Chemistry | Unit: Introduction to Chemistry | Topic: Stoichiometry and mole concept]
Q.132. Sublimation is used to purify:
A. Ammonium sulphate
B. Sodium chloride
C. Benzoic acid
D. Lead carbonate

[Chemistry | Unit: Introduction to Chemistry | Topic: Stoichiometry and mole concept]
Q.133. The purity of a substance can be identified by:
A. Sublimation
B. Filtration
C. Chromatography
D. Solvent extraction

[Chemistry | Unit: Introduction to Chemistry | Topic: Stoichiometry and mole concept]
Q.134. Which one of the following mathematical expressions represents the Avogadro’s law?
A. V ∝ n (T, P const)
B. V ∝ T (P const)
C. V ∝ 1/P (T const)
D. PV = k

[Chemistry | Unit: Gases | Topic: Gas laws and kinetic molecular theory]
Q.135. The root mean square velocity of gases is inversely proportional to the square root of their:
A. Molar mass
B. Temperature
C. Pressure
D. Volume

[Chemistry | Unit: Gases | Topic: Gas laws and kinetic molecular theory]
Q.136. Plasma is the ionized gas mixture which consists of:
A. Ions and electrons
B. Electrons and neutral atoms
C. Electrons, ions and neutral atoms
D. Ions and neutral atoms

[Chemistry | Unit: Chemical Bonding | Topic: Bonding and molecular shape]
Q.137. Which type of force is present in gasoline?
A. Dipole-dipole forces
B. Dipole-induced dipole forces
C. London dispersion forces
D. Hydrogen bonding

[Chemistry | Unit: Liquids and Solids | Topic: Intermolecular forces and states of matter]
Q.138. In the structure of NaCl, each Na+ is surrounded by _ Cl- ions.
A. Four
B. Eight
C. Five
D. Six

[Chemistry | Unit: Atomic Structure | Topic: Atomic models and electronic configuration]
Q.139. The charge of one gram of electron is:
A. 1.7588 x 10-11
B. 1.7588 x 1011
C. 1.602 x 10-19
D. 1.7588 x 108

[Chemistry | Unit: S- and P-Block Elements | Topic: Periodic trends and main-group chemistry]
Q.140. The ionization energy of hydrogen atom is :
A. Zero
B. 13.13 kJmol-1
C. 1313.31 kJmol-1
D. 1313.31 k2Jmol

[Chemistry | Unit: Atomic Structure | Topic: Atomic models and electronic configuration]
Q.141. Which quantum number helps to study the orientation of an orbital in space?
A. Principal Quantum Number
B. Spin Quantum Number
C. Magnetic Quantum Number
D. Azimuthal Quantum Number

[Chemistry | Unit: Liquids and Solids | Topic: Intermolecular forces and states of matter]
Q.142. The inter-ionic distance in a crystal lattice of KCl is:
A. 314 pm
B. 181 pm
C. 95 pm
D. 300 pm

[Chemistry | Unit: Chemical Bonding | Topic: Bonding and molecular shape]
Q.143. The number of bonds in nitrogen molecule is:
A. One σ and three π
B. Three σ bonds only
C. One σ and two π
D. Two σ and one π

[Chemistry | Unit: Chemical Bonding | Topic: Bonding and molecular shape]
Q.144. Which one of the following molecules has zero dipole moment?
A. NH3
B. CHCl3
C. BF3
D. H2O

[Chemistry | Unit: Thermochemistry and Energetics | Topic: Heat, enthalpy and thermodynamics]
Q.145. A spontaneous process is:
A. Unidirectional and irreversible
B. Irreversible and a real process
C. Unidirectional and a real process
D. All of the above

[Chemistry | Unit: Thermochemistry and Energetics | Topic: Heat, enthalpy and thermodynamics]
Q.146. The standard enthalpy of solution of NH4Cl is _ kJmol-1.
A. +16.2
B. -25.0
C. +4.98
D. +26.0

[Chemistry | Unit: Chemical Equilibrium | Topic: Equilibrium and buffers]
Q.147. The Kc has following units for the reaction H2(g) + I2(g) ⇋ 2HI (g)
A. mol3dm-6
B. moldm-3
C. mol-3dm6
D. No unit

[Chemistry | Unit: Introduction to Chemistry | Topic: Stoichiometry and mole concept]
Q.148. 0.1 mole of acetic acid has been dissolved per dm3 of the solution, the percentage ionization of acetic acid will be
A. 13
B. 15
C. 1.3
D. 0.1

[Chemistry | Unit: Liquids and Solids | Topic: Intermolecular forces and states of matter]
Q.149. Solubility of Ce2(SO4)3.
A. Increases with temperature
B. Decreases with temperature
C. Shows exceptional behavior
D. Remains constant

[Chemistry | Unit: Introduction to Chemistry | Topic: Stoichiometry and mole concept]
Q.150. Seawater has 5.65 x 10-3 g of dissolved oxygen in one kilogram of water. Concentration of O2 in parts per million is
A. 5.65
B. 7.69
C. 5.20
D. 4.11

[Chemistry | Unit: Liquids and Solids | Topic: Intermolecular forces and states of matter]
Q.151. Metallic conduction involves the relatively free movement of their _ throughout the metallic lattice.
A. Atoms
B. Molecules
C. Electrons
D. Ions

[Physics | Unit: Work and Energy | Topic: Work, power and energy]
Q.152. Which one is the highest power multiple?
A. Giga
B. Tera
C. Mega
D. Deca

[Physics | Unit: Electrostatics | Topic: Electric field, potential and capacitance]
Q.153. SI unit of charge is _.
A. Ampere
B. Volt
C. Coulomb
D. Calorie

[Physics | Unit: Current Electricity | Topic: Circuits and resistance]
Q.154. The electrical analog of mass in electricity is _.
A. Capacitance
B. Inductance
C. Charge
D. Resistance

[Physics | Unit: Electromagnetism | Topic: Magnetic fields and force]
Q.155. Which one of the following relations is correct?
A. 1 Wb m-2 = N m-1 A-1
B. 1 Tesla = 104 Gauss
C. 1 Wb m-2 = 1 Tesla
D. All of these

[Physics | Unit: Waves | Topic: Waves, sound and SHM]
Q.156. Life time of electron in metastable state is about _.
A. 10-5 sec
B. 10-3 sec
C. 10-8 sec
D. 10-2 sec

[Physics | Unit: Rotational and Circular Motion | Topic: Angular motion and torque]
Q.157. The torque acting on a current carrying coil is given by _.
A. τ = NIAB cos α
B. τ = BIL sin α
C. τ = NIAB sin α
D. τ = BIL cos α

[Physics | Unit: Electronics | Topic: Semiconductors and electronic devices]
Q.158. The grid in the cathode ray oscilloscope _.
A. Controls the number of waves
B. Controls the brightness of the spot formed
C. Accelerates electrons
D. Has positive potential with respect to the cathode

[Physics | Unit: Force and Motion | Topic: Kinematics, Newton laws and momentum]
Q.159. The horizontal range of a projectile, at a certain place, is completely determined by:
A. The angle of projection
B. The initial velocity of projection
C. The mass of the projectile
D. Speed and mass of the projectile

[Physics | Unit: Force and Motion | Topic: Kinematics, Newton laws and momentum]
Q.160. If velocity is double, then:
A. Momentum increases 4 times and K.E increases 2 times
B. Momentum and K.E remain the same
C. Momentum increases 2 times and K.E increases constantly
D. Momentum increases 2 times and K.E increases 4 times

[Physics | Unit: Work and Energy | Topic: Work, power and energy]
Q.161. The consumption of energy by 60-watt bulb in 2 seconds is:
A. 20 J
B. 120 J
C. 30 J
D. 0.02 J

[Physics | Unit: Electronics | Topic: Semiconductors and electronic devices]
Q.162. In transistors, the base region is very thin of the order of:
A. 10-5 cm
B. 10-6 m
C. 10-6 mm
D. 10-6 µm

[Physics | Unit: Electronics | Topic: Semiconductors and electronic devices]
Q.163. The closed loop gain of OP-AMP depends on:
A. Internal structure of OP-AMP
B. Externally connected resistance
C. Voltage of power supplies
D. Input resistance

[Physics | Unit: Electronics | Topic: Semiconductors and electronic devices]
Q.164. The net charge on an N-type substance is:
A. Neutral (0)
B. Positive
C. Negative
D. Variable

[Physics | Unit: Thermodynamics | Topic: Heat and thermal physics]
Q.165. The value of Wien’s constant is:
A. 2.90 x 10-3 mK
B. 3.34 x 10-4 mK
C. 4.22 x 10-7 mK
D. 3.42 x 10-8 mK

[Physics | Unit: Waves | Topic: Waves, sound and SHM]
Q.166. The minimum frequency below which no electron is emitted from the metal surface is called:
A. High frequency
B. Low frequency
C. Threshold frequency
D. Resonance frequency

[Physics | Unit: Dawn of Modern Physics | Topic: Photon and quantum physics]
Q.167. In pair production, the type of photon used:
A. α-particle
B. β-particle
C. X-rays
D. γ-radiations

[Physics | Unit: Dawn of Modern Physics | Topic: Photon and quantum physics]
Q.168. The life time of an electron in an excited state is about 10-8 s. What is its uncertainty in energy during this time?
A. 1.05 x 10-41 J
B. 1.05 x 10-26 J
C. 1.15 x 1010 J
D. 2.19 x 10-40 J

[Physics | Unit: Atomic Spectra | Topic: Atomic spectra]
Q.169. Velocity of electron moving in first orbit of hydrogen is:
A. 2.19 x 107 m/sec
B. 2.18 x 107 m/sec
C. 2.2 x 108 m/sec
D. 2.19 x 106 m/sec

[Physics | Unit: Waves | Topic: Waves, sound and SHM]
Q.170. Laser is a potential energy source for inducing which type of reaction?
A. Radioactive
B. Fission
C. Ionization
D. Fusion

[Physics | Unit: Nuclear Physics | Topic: Radioactivity and nuclear decay]
Q.171. In the half-life of an element, the equation for the number of decaying atoms is given by:
A. ΔN ∝ -NΔt
B. ΔN = KNΔt
C. ΔN ∝ -nΔt
D. ΔN = -ΔNΔt

[Physics | Unit: Nuclear Physics | Topic: Radioactivity and nuclear decay]
Q.172. Decay constant ‘λ’ is given as:
A. λ = ln(2)/T1/2
B. λ = N/t
C. λ = dN/dt
D. λ = A/N

[Physics | Unit: Nuclear Physics | Topic: Radioactivity and nuclear decay]
Q.173. The SI unit of absorbed dose ‘D’ i.e. radiation effect is Gray and one Gray is equal to:
A. kJ / mol
B. J / mol
C. kg / J
D. J / kg

[Physics | Unit: Force and Motion | Topic: Kinematics, Newton laws and momentum]
Q.174. The principle of homogeneity of dimensions determines:
A. Only the variables in the equation
B. Only the constants in the equation
C. The correctness of an equation
D. Both constants and variables in the equation

[Physics | Unit: Vectors and Equilibrium | Topic: Vectors and vector products]
Q.175. For a body to be in complete equilibrium:
A. Linear acceleration is zero
B. Angular acceleration is zero
C. Linear acceleration is zero but angular acceleration is not zero
D. Linear acceleration and angular acceleration both should be zero

[Physics | Unit: Rotational and Circular Motion | Topic: Angular motion and torque]
Q.176. If length of a spanner is ‘I’ and a force ‘F’ is applied on it to tighten a nut such that it passes through the pivot point, then torque is:
A. Zero
B. Fl
C. Fl sin θ
D. Fl sin θλ

[Physics | Unit: Vectors and Equilibrium | Topic: Vectors and vector products]
Q.177. If a force of magnitude 8 N acts on a body in direction making an angle 30, its x and y components will be:
A. Fx = 4√3 and Fy = 8
B. Fx = 8 and Fy = 4√3
C. Fx = 4√3 and Fy = 4
D. Fx = 8√3 and Fy = 4

[Physics | Unit: Vectors and Equilibrium | Topic: Vectors and vector products]
Q.178. The difference of a vector B and its negative vector –B is:
A. A null vector
B. Equal to magnitude of vector B
C. Twice the magnitude of vector B
D. Smaller than magnitude of vector B

[Physics | Unit: Force and Motion | Topic: Kinematics, Newton laws and momentum]
Q.179. Time of projectile’s flight is:
A. v0 sin(θ) / g
B. 2v0 sin(θ) / g
C. v0 cos(θ) / g
D. 2v0 cos(θ) / g

[Physics | Unit: Force and Motion | Topic: Kinematics, Newton laws and momentum]
Q.180. If the velocity of the body changes by equal amount in equal intervals of time, the body is said to have:
A. Variable acceleration
B. Uniform acceleration
C. Uniform velocity
D. Negative acceleration

[Physics | Unit: Force and Motion | Topic: Kinematics, Newton laws and momentum]
Q.181. In order to determine the maximum height of the projectile, the equation of motion used is:
A. aS = vf2 - vi2
B. 2aS = vf2 - vi2
C. 2S = a(vf2 - vi2)
D. aS = 2(vf2 - vi2)

[Physics | Unit: Force and Motion | Topic: Kinematics, Newton laws and momentum]
Q.182. If a force of 12 N acts on a car and changes its momentum from 36 kgm/sec to 60 kgm/sec, the time during which this change occurs will be
A. 24 sec
B. 2 sec
C. 12 sec
D. 8 sec

[Physics | Unit: Work and Energy | Topic: Work, power and energy]
Q.183. Which one of the following is a non-conservative force?
A. Electric force
B. Elastic spring force
C. Gravitational force
D. Frictional force

[Physics | Unit: Force and Motion | Topic: Kinematics, Newton laws and momentum]
Q.184. Value of escape velocity for the surface of the earth is 11 km/sec. Its value for surface of the moon is:
A. 11 km/sec
B. 10.4 km/sec
C. 2.4 km/sec
D. 4.3 km/sec

[Physics | Unit: Thermodynamics | Topic: Heat and thermal physics]
Q.185. On a clear day at noon, the intensity of solar energy reaching the earth’s surface is about:
A. 1.0 kWm-2
B. 1.4 kWm-2
C. 1.0 Wm-2
D. 1.4 Wm-2

[Physics | Unit: Force and Motion | Topic: Kinematics, Newton laws and momentum]
Q.186. When a lift is accelerated upward, the apparent weight of an object in it will be:
A. Equal to its real weight
B. Less than its real weight
C. Zero
D. Greater than its real weight

[Physics | Unit: Rotational and Circular Motion | Topic: Angular motion and torque]
Q.187. The moment of inertial of a thin rod is:
A. 1/2 mL2
B. 1/4 m3L
C. 1/12 mL
D. 1/12 mL2

[Physics | Unit: Force and Motion | Topic: Kinematics, Newton laws and momentum]
Q.188. A wheel of radius 1m covers an angular displacement of 180.Its linear displacement is:
A. 3.14 m
B. π rad
C. 6.28 m
D. 0.157 m

[Physics | Unit: Fluid Dynamics | Topic: Fluid flow and Bernoulli principle]
Q.189. Conservation of mass of fluid flow leads to:
A. Bernoulli’s equation
B. Venturi meter
C. Equation of motion
D. Equation of continuity

[Physics | Unit: Fluid Dynamics | Topic: Fluid flow and Bernoulli principle]
Q.190. The blood vessels collapse when:
A. External pressure applied becomes greater than the systolic pressure
B. External pressure applied is equal to systolic pressure
C. External pressure applied is less than the systolic pressure
D. External pressure applied is zero

[Physics | Unit: Waves | Topic: Waves, sound and SHM]
Q.191. An oscillating body is at mean position at t = 0. At t = T/4 it will be at:
A. Extreme position
B. Mean position
C. Between extreme and mean position
D. Beyond extreme position

[Physics | Unit: Waves | Topic: Waves, sound and SHM]
Q.192. In a simple pendulum, the tension of the string is:
A. T = g cos θ
B. T = mg sin θ
C. T = mg cos θ
D. T = mg

[Physics | Unit: Waves | Topic: Waves, sound and SHM]
Q.193. Two sound waves having the same amplitudes are moving in the same direction are out of phase. The amplitude of the resultant wave is:
A. Zero amplitude
B. The sum of the amplitudes of the two waves
C. Difference of the amplitudes of the two waves
D. Double the amplitude of either wave

[Physics | Unit: Waves | Topic: Waves, sound and SHM]
Q.194. A source ‘Y’ of unknown frequency produces 4 beats with a source of 240 Hz and 8 beats with a sound of 252 Hz. Frequency of the source ‘Y’ is:
A. 244 Hz
B. 236 Hz
C. 248 Hz
D. 246 Hz

[Physics | Unit: Waves | Topic: Waves, sound and SHM]
Q.195. An organ pipe closed at one end has a length of 25 cm. Wavelength of the fundamental note is:
A. 25 cm
B. 50 cm
C. 100 cm
D. 75 cm

[Physics | Unit: Waves | Topic: Waves, sound and SHM]
Q.196. In Newton ring apparatus, at the point of contact of the lens and glass plate, the additional path difference introduced is:
A. λ/4
B. λ/2
C. λ
D. λ/3

[Physics | Unit: Waves | Topic: Waves, sound and SHM]
Q.197. The path difference ‘BD’ for destructive interference is:
A. (m + ½) λ
B. mλ
C. d sin θ
D. 3λ

[Physics | Unit: Waves | Topic: Waves, sound and SHM]
Q.198. In the case of a grafting spectrometer, the resolving power ‘R’ of the grating is defined as:
A. λ / Δλ
B. λ / D
C. λ / λ1
D. N x m

[Physics | Unit: Waves | Topic: Waves, sound and SHM]
Q.199. Which one of the following lights travels fastest in optical fibers?
A. Visible light
B. Ultraviolet light
C. Ordinary light
D. Invisible infrared light

[Physics | Unit: Thermodynamics | Topic: Heat and thermal physics]
Q.200. The value of universal gas constant is:
A. 8.314 Jmol-1K-1
B. 8.324 Jmol-1K-1
C. 7.23 Jmol-1K-1
D. 1.00 Jmol-1K-1

[Physics | Unit: Thermodynamics | Topic: Heat and thermal physics]
Q.201. The turbine in a steam power plant takes steam from a boiler at 427 °C and exhausts into a low temperature reservoir at 77 °C. What is the maximum possible efficiency?
A. 50%
B. 40%
C. 60%
D. 70%

[Physics | Unit: Thermodynamics | Topic: Heat and thermal physics]
Q.202. Which one of the following is a postulate of kinetic theory of gases?
A. Molecules do not exert any force on each other
B. The size of molecules is much larger than the separation between the molecules
C. A finite volume of gas consists of a very small number of molecules
D. The gas molecules are not in random motion

[Physics | Unit: Thermodynamics | Topic: Heat and thermal physics]
Q.203. Which one is not an irreversible process?
A. Slow compression of a gas into a cylinder
B. Changes due to friction
C. Explosion
D. Dissipation of energy

[Physics | Unit: Electrostatics | Topic: Electric field, potential and capacitance]
Q.204. Electric intensity is a vector quantity and its direction is:
A. Perpendicular to the direction of field
B. Opposite to the direction of force
C. At a certain angle
D. Along the direction of force

[Physics | Unit: Electrostatics | Topic: Electric field, potential and capacitance]
Q.205. The magnitude of an electric field between two separated plates can be calculated by the relation:
A. ΔV = Ed
B. ΔV = E/d
C. ΔV = E/qo
D. E = d/ΔV

[Physics | Unit: Electrostatics | Topic: Electric field, potential and capacitance]
Q.206. SI unit of electric flux is:
A. NmC-1
B. Nm-2C-2
C. Nm2C-1
D. Nm2C-2

[Physics | Unit: Current Electricity | Topic: Circuits and resistance]
Q.207. The equivalent current which passes from a point at higher potential to a point at a lower potential as if it represented a movement of positive charges is:
A. Electronic current
B. Electric current
C. Magnetic lines
D. Conventional current

[Physics | Unit: Current Electricity | Topic: Circuits and resistance]
Q.208. If ‘V’ is applied potential difference across a resistance ‘R’, then loss in potential energy per unit time is:
A. VI
B. I2R
C. V2/R
D. All of the above

[Physics | Unit: Current Electricity | Topic: Circuits and resistance]
Q.209. The substances like germanium and silicon have:
A. Negative temperature coefficients
B. Positive temperature coefficients
C. Both A and B
D. None of the above

[Physics | Unit: Electromagnetism | Topic: Magnetic fields and force]
Q.210. The sensitivity of a galvanometer can be decreased by:
A. Increasing magnetic field
B. Increasing the number of turns of the coil
C. Increasing the c/BAN ratio
D. Decreasing the length of couple 'c'

[Physics | Unit: Electromagnetism | Topic: Magnetic fields and force]
Q.211. Force on a current carrying conductor in a uniform magnetic field is:
A. F = NIA cos α
B. F = μnI
C. F = ILB sin α
D. F = ILA cos α

[English | Unit: Reading and Thinking Skills | Topic: Grammar, vocabulary, comprehension]
Q.212. Fill in the blank with appropriate option.There is nothing interesting in mathematics. I _ read grammar.
A. Could
B. Can
C. Might as well
D. Must

[English | Unit: Reading and Thinking Skills | Topic: Grammar, vocabulary, comprehension]
Q.213. Fill in the blank with appropriate option.You _ reduce the speed. There is a speed limit.
A. Need to
B. Ought to
C. Must
D. Will

[English | Unit: Reading and Thinking Skills | Topic: Grammar, vocabulary, comprehension]
Q.214. Fill in the blank with appropriate option.You _ drive fast. We have plenty of time.
A. Will not
B. Shall not
C. Must not
D. Need not

[English | Unit: Reading and Thinking Skills | Topic: Grammar, vocabulary, comprehension]
Q.215. Spot the error.The teacher made all the students to rewrite their papers because the first drafts were not acceptable.
A. All the
B. To rewrite
C. The first
D. Were

[English | Unit: Reading and Thinking Skills | Topic: Grammar, vocabulary, comprehension]
Q.216. Fill in the blank with appropriate option.When I was young, I _ run very fast.
A. Can
B. Could
C. Could have
D. Must

[English | Unit: Reading and Thinking Skills | Topic: Grammar, vocabulary, comprehension]
Q.217. Fill in the blank with appropriate option.She has a driving license. She _ drive the car on the motorway.
A. Must
B. May
C. Can
D. Could

[English | Unit: Reading and Thinking Skills | Topic: Grammar, vocabulary, comprehension]
Q.218. Fill in the blank with appropriate option._ you turn down the music a bit, please?
A. Might
B. Can
C. Could
D. Would

[English | Unit: Reading and Thinking Skills | Topic: Grammar, vocabulary, comprehension]
Q.219. Fill in the blank with appropriate option.The old garage suddenly collapsed one day. Luckily, the owner wasn’t there or he _ received serious injuries.
A. Might as well
B. Could have
C. Have to
D. Would
"""

q2010 = parse_year_text(2010, RAW_2010)
save_year_json(2010, q2010)
print("2010 saved:", len(q2010))
