import os
import sys
sys.path.append(os.path.dirname(__file__))
from parser_helper import parse_year_text, save_year_json

RAW_2011 = """
[English | Unit: Formal and Lexical Skills | Topic: Vocabulary, sentence correction and usage]
Q.001. She managed to _ a ticket for the cricket match.
A. Procure
B. Obscure
C. Improvise
D. Preclude

[English | Unit: Formal and Lexical Skills | Topic: Vocabulary, sentence correction and usage]
Q.002. Things have got out of hand; we must take steps to _ the situation.
A. Rectify
B. Pacify
C. Purify
D. Testify

[English | Unit: Formal and Lexical Skills | Topic: Vocabulary, sentence correction and usage]
Q.003. George Orwell’s Animal Farm is a stinging _ on the Russian revolution.
A. Myth
B. Satire
C. Fallacy
D. Legend

[English | Unit: Formal and Lexical Skills | Topic: Vocabulary, sentence correction and usage]
Q.004. All the _ and ceremony of the royal wedding were telecast on the national television circuit.
A. Festival
B. Romp
C. Pomp
D. Happiness

[English | Unit: Formal and Lexical Skills | Topic: Vocabulary, sentence correction and usage]
Q.005. Select the incorrect segment:The patient’s blood analysis shows that there is a big number of amorphous cells which are quiet unidentifiable.
A. Patient’s
B. Of
C. Which
D. Quiet

[English | Unit: Formal and Lexical Skills | Topic: Vocabulary, sentence correction and usage]
Q.006. Select the incorrect segment:The police, in their investigation, used coercive measure to get a favorable statement from the accused.
A. Measure
B. To
C. From
D. The accused

[English | Unit: Formal and Lexical Skills | Topic: Vocabulary, sentence correction and usage]
Q.007. Select the incorrect segment:Your argument is simply abstruse as there is no clarity of thought and coherence in ideas and it also lack vision.
A. Is
B. Of
C. In
D. Lack

[English | Unit: Formal and Lexical Skills | Topic: Vocabulary, sentence correction and usage]
Q.008. The workers were raising much hue and cry when their demands were turned away.
A. Raising
B. Much
C. Demands
D. Away

[English | Unit: Formal and Lexical Skills | Topic: Vocabulary, sentence correction and usage]
Q.009. The disease is uncurable without the judicious use of antibiotics.
A. Uncurable
B. Without
C. Judicious
D. Use

[English | Unit: Formal and Lexical Skills | Topic: Vocabulary, sentence correction and usage]
Q.010. The younger sister hopes to emulate her elder sister’s sporting achievement as she is putting up hectic effort.
A. To
B. Sister’s
C. Achievement
D. Up

[English | Unit: Formal and Lexical Skills | Topic: Vocabulary, sentence correction and usage]
Q.011. Choose the correct sentence from the following options:
A. The government should accrue taxes for strengthen the economy of the country.
B. The government should accrue taxes in strengthen the economy of the country
C. The government should accrue taxes to strengthen the economy of the country.
D. The government should accrue taxes by strengthen the economy of the country.

[English | Unit: Formal and Lexical Skills | Topic: Vocabulary, sentence correction and usage]
Q.012. Choose the correct sentence from the following options:
A. I remember going to British Museum one day.
B. I remember to go to British Museum one day.
C. I remember to go to the British Museum one day.
D. I remember going to the British Museum one day.

[English | Unit: Formal and Lexical Skills | Topic: Vocabulary, sentence correction and usage]
Q.013. Select the NEAREST CORRECT MEANING of the given word:MUSE
A. Wander
B. Fonder
C. Robust
D. Ponder

[English | Unit: Formal and Lexical Skills | Topic: Vocabulary, sentence correction and usage]
Q.014. Select the NEAREST CORRECT MEANING of the given word:FECKLESS
A. Useless
B. Careless
C. Dauntless
D. Fearless

[English | Unit: Formal and Lexical Skills | Topic: Vocabulary, sentence correction and usage]
Q.015. Select the NEAREST CORRECT MEANING of the given word:MOSAIC
A. Pattern
B. Mortal
C. Ordinary
D. Musical

[English | Unit: Formal and Lexical Skills | Topic: Vocabulary, sentence correction and usage]
Q.016. Select the NEAREST CORRECT MEANING of the given word:INSCRUTABLE
A. Immoral
B. Unethical
C. Enigmatic
D. Unaccountable

[English | Unit: Formal and Lexical Skills | Topic: Vocabulary, sentence correction and usage]
Q.017. Select the NEAREST CORRECT MEANING of the given word:JUXTAPOSE
A. Justify
B. Compare
C. Expose
D. Jettison

[English | Unit: Formal and Lexical Skills | Topic: Vocabulary, sentence correction and usage]
Q.018. Select the NEAREST CORRECT MEANING of the given word:LACERATING
A. Landing
B. Tearing
C. Flagging
D. Lactating

[English | Unit: Formal and Lexical Skills | Topic: Vocabulary, sentence correction and usage]
Q.019. Select the NEAREST CORRECT MEANING of the given word:EMPATHY
A. Fictitious
B. Facility
C. Ability
D. Felicity

[English | Unit: Formal and Lexical Skills | Topic: Vocabulary, sentence correction and usage]
Q.020. Select the NEAREST CORRECT MEANING of the given word:EVANESCENT
A. Evident
B. Permanent
C. Event
D. Transitory

[English | Unit: Formal and Lexical Skills | Topic: Vocabulary, sentence correction and usage]
Q.021. Select the NEAREST CORRECT MEANING of the given word: SIDLE
A. Sneak
B. Sift
C. Siege
D. Sieve

[English | Unit: Formal and Lexical Skills | Topic: Vocabulary, sentence correction and usage]
Q.022. Select the NEAREST CORRECT MEANING of the given word:DISSONANCE
A. Inconsistency
B. Expansion
C. Perceptible
D. Rapport

[Biology | Unit: Biological Molecules | Topic: Carbohydrates, proteins, lipids and nucleic acids]
Q.023. An association between two organisms benefiting both is called:
A. Commensalism
B. Parasitism
C. Predation
D. Symbiosis

[Biology | Unit: Bioenergetics | Topic: Cellular respiration and photosynthesis]
Q.024. In aquatic ecosystem, human activities may accelerate the process of:
A. Eutrophication
B. Photosynthesis
C. Decomposition
D. Recycling

[Biology | Unit: Biological Molecules | Topic: Carbohydrates, proteins, lipids and nucleic acids]
Q.025. Beri Beri is due to:
A. Metabolic disorder
B. Chemical causes
C. Nutritional deficiency
D. Mental Illness

[Biology | Unit: Bioenergetics | Topic: Cellular respiration and photosynthesis]
Q.026. The natural heat energy trapped underground is:
A. Geothermal energy
B. Thermal energy
C. Electric energy
D. Solar energy

[Biology | Unit: Biological Molecules | Topic: Carbohydrates, proteins, lipids and nucleic acids]
Q.027. Which of the following is the lowest level of biological organization with respect to others?
A. Multicellular organisms
B. Biosphere
C. Species
D. Population

[Chemistry | Unit: Chemical Bonding | Topic: Bonding and molecular shape]
Q.028. When an electron pair is shared between two atoms:
A. Two covalent bonds are formed
B. Hydrogen bond is formed
C. Single covalent bond is formed
D. Ionic bond is formed

[Biology | Unit: Biological Molecules | Topic: Carbohydrates, proteins, lipids and nucleic acids]
Q.029. The first microbe to have the genome completely sequenced which was published on July 28th, 1995 was:
A. Hyphomicrobium
B. Haemophilus aquaticus
C. Haemophillus malariae
D. Haemophillus infulenzae

[Biology | Unit: Enzymes | Topic: Enzymes and inhibition]
Q.030. An activated enzyme consisting of polypeptide and a cofactor is known as:
A. Amylase
B. Apoenzyme
C. Holoenzyme
D. Coenzyme

[Biology | Unit: Enzymes | Topic: Enzymes and inhibition]
Q.031. _ forms weak linkages with enzymes and their effect can be neutralized completely or partly by an increase in the concentration of the substrate.
A. Only competitive Inhibitors
B. Reversible inhibitors
C. Irreversible inhibitors
D. Both reversible and irreversible inhibitors

[Biology | Unit: Biological Molecules | Topic: Carbohydrates, proteins, lipids and nucleic acids]
Q.032. In prokaryotic cell wall, strengthening material is:
A. Cellulose
B. Silica
C. Chitin
D. Peptidoglycan

[Biology | Unit: Cell Structure and Function | Topic: Cells, organelles and chromosomes]
Q.033. The entire cell wall of bacteria is often regarded as a single huge molecule or molecular complex called_:
A. Capsule
B. Secondary wall
C. Slime capsule
D. Sacculus

[Biology | Unit: Bioenergetics | Topic: Cellular respiration and photosynthesis]
Q.034. Krebs cycle takes place in:
A. Dictyosomes
B. Mitochondrial matrix
C. Lysosomes
D. Vesicles of endoplasmic reticulum

[Biology | Unit: Biological Molecules | Topic: Carbohydrates, proteins, lipids and nucleic acids]
Q.035. Chemically, viruses are made up of
A. Nucleic acid only
B. Protein only
C. Nucleic acid and protein
D. Lipoproteins

[Biology | Unit: Acellular Life | Topic: Viruses and HIV/AIDS]
Q.036. Widespread epidemic disease, influenza is caused by:
A. DNA virus
B. RNA enveloped virus
C. DNA enveloped virus
D. RNA virus

[Biology | Unit: Cell Structure and Function | Topic: Cells, organelles and chromosomes]
Q.037. When the division of cells is in three planes, the arrangement is known as:
A. Diplococcus
B. Sarcina
C. Streptococcus
D. Staphylococcus

[Biology | Unit: Cell Structure and Function | Topic: Cells, organelles and chromosomes]
Q.038. Bacterial ‘death rate’ is equal to ‘birth rate; in:
A. Lag phase
B. Log phase
C. Death phase
D. Stationary phase

[Biology | Unit: Acellular Life | Topic: Viruses and HIV/AIDS]
Q.039. Trypanosoma is a human parasite causing:
A. African sleeping sickness
B. European sleeping sickness
C. Indonesian sleeping sickness
D. American sleeping sickness

[Biology | Unit: Cell Structure and Function | Topic: Cells, organelles and chromosomes]
Q.040. The feeding stage of slime mold is a:
A. Gastrozoid
B. Sporozoite
C. Plasmodium
D. Merozote

[Biology | Unit: Biological Molecules | Topic: Carbohydrates, proteins, lipids and nucleic acids]
Q.041. Drug obtained from fungus used for lowing blood cholesterol is:
A. Lovastatin
B. Cyclosporin
C. Ergotin
D. Griseofulvin

[Biology | Unit: Biological Molecules | Topic: Carbohydrates, proteins, lipids and nucleic acids]
Q.042. Fungi store surplus food in the form of:
A. Cellulose
B. Glycogen
C. Starch
D. Both B and C

[Biology | Unit: Biological Molecules | Topic: Carbohydrates, proteins, lipids and nucleic acids]
Q.043. The ecological role of fungi as decomposers is paralleled only by:
A. Prions
B. Algae
C. Bacteria
D. Viruses

[Biology | Unit: Inheritance | Topic: Mendelian and sex-linked inheritance]
Q.044. “Vascular System absent"; gametophyte dominant, sporophyte attached to gametophyte; "homosporous” are distinguishing characters of:
A. Psilopsida
B. Pteropsida
C. Angiosperms
D. Bryophyta

[Biology | Unit: Reproduction | Topic: Human reproduction and menstrual cycle]
Q.045. Which of the following features differentiate angiosperms from gymnosperms?
A. Pollens disperse by air
B. Haploid microspores
C. Ovaries
D. Pollen tubes

[Biology | Unit: Biological Molecules | Topic: Carbohydrates, proteins, lipids and nucleic acids]
Q.046. In Pakistan, the furniture wood is mainly obtained from the members of family:
A. Rosaceae
B. Solanaceae
C. Minosaceae
D. Fabaceae

[Biology | Unit: Circulation | Topic: Heart, blood and vessels]
Q.047. Which of the following is the exclusive character of mammals?
A. Homeothermic
B. Poikilothermic
C. Hair
D. Four chambered heart

[Biology | Unit: Circulation | Topic: Heart, blood and vessels]
Q.048. Overactivity of the sympathetic nervous system causes:
A. Disturbance of Vision
B. Constipation
C. Decrease in Blood Pressure
D. Increase in Heart Rate

[Biology | Unit: Coordination and Control | Topic: Nervous system and receptors]
Q.049. Which structures respond when they are stimulated by an impulse coming through the motor neuron?
A. Receptors
B. Responses
C. Effectors
D. Transduction

[Biology | Unit: Coordination and Control | Topic: Nervous system and receptors]
Q.050. Respiratory centre is located in:
A. Cerebrum
B. Cerebellum
C. Medulla
D. Hypothalamus

[Biology | Unit: Coordination and Control | Topic: Nervous system and receptors]
Q.051. A neurological condition characterised by involuntary tremors, diminished motor activity, and rigidity is called:
A. Epilepsy
B. Parkinson’s Disease
C. Alzheimer’s Disease
D. Cerebellar Tumours

[Biology | Unit: Reproduction | Topic: Human reproduction and menstrual cycle]
Q.052. A type of cell in human testes which produces testosterone is called:
A. Interstitial Cells
B. Germ Cells
C. Sertoli Cells
D. Spermatocytes

[Biology | Unit: Reproduction | Topic: Human reproduction and menstrual cycle]
Q.053. Breakdown of the endometrium during menstruation is due to:
A. Increase in the level of LH
B. Decrease in the level of progesterone
C. Increase in the level of FSH
D. Increase in the level of estrogen

[Biology | Unit: Reproduction | Topic: Human reproduction and menstrual cycle]
Q.054. Oogonia are produced in the germ cells of:
A. Both Uterus and Cervix
B. Cervix
C. Uterus
D. Ovary

[Biology | Unit: Acellular Life | Topic: Viruses and HIV/AIDS]
Q.055. Which of the following diseases can be prevented through vaccination?
A. AIDS and Cancer
B. Malaria and AIDS
C. Typhoid and Cancer
D. Measles and Mumps

[Biology | Unit: Biotechnology | Topic: Genetic engineering and applications]
Q.056. Newly produced cells/individuals which are identical in each other are known as:
A. Genetically Modified
B. Transgenic Animals
C. Transgenic Bacteria
D. Clones

[Biology | Unit: Acellular Life | Topic: Viruses and HIV/AIDS]
Q.057. Which of the following is a blood borne disease?
A. Hepatitis
B. Cholera
C. Influenza
D. Candidiasis

[Biology | Unit: Evolution | Topic: Evolution and natural selection]
Q.058. The control of pests has traditionally meant regulation by natural enemies, predators, parasites and pathogens. This type of control is known as:
A. Cultural Control
B. Biological Control
C. Pesticides Control
D. Insecticides Control

[Biology | Unit: Cell Structure and Function | Topic: Cells, organelles and chromosomes]
Q.059. Which of the following organelles is concerned with the cell secretion?
A. Ribosomes
B. Golgi Apparatus
C. Lysosomes
D. Mitochondria

[Biology | Unit: Cell Structure and Function | Topic: Cells, organelles and chromosomes]
Q.060. Which of the following contains peptidoglycan cell wall?
A. Penicillium
B. Bacterium
C. Adiantum
D. Polytrichum

[Biology | Unit: Cell Structure and Function | Topic: Cells, organelles and chromosomes]
Q.061. The inner membrane of mitochondria is folded to form finger like structure called:
A. Cristae
B. Vesicle
C. Matrix
D. Cisternae

[Biology | Unit: Cell Structure and Function | Topic: Cells, organelles and chromosomes]
Q.062. Interior of chloroplast is divided into the heterogeneous structure, embedded in the stroma known as:
A. Grana
B. Thylakoids
C. Stroma
D. Cisternae

[Biology | Unit: Cell Structure and Function | Topic: Cells, organelles and chromosomes]
Q.063. In which phase of the cell division is the metabolic activity of the nucleus is high?
A. Mitosis
B. Interphase
C. Meiosis
D. Cell Cycle

[Biology | Unit: Coordination and Control | Topic: Nervous system and receptors]
Q.064. Luteinizing hormone triggers:
A. Cessation of oogenesis
B. Breakdown of oocytes
C. Ovulation
D. Development of zygote

[Biology | Unit: Acellular Life | Topic: Viruses and HIV/AIDS]
Q.065. Syphilis is a sexually transmitted disease which is caused by:
A. HIV / AIDS
B. Pseudomonas Pyogenes
C. Treponema Pallidum
D. Neisseria

[Biology | Unit: Support and Movement | Topic: Skeleton, muscles and joints]
Q.066. Muscle is made up of many cells, which are referred to as:
A. Myofilaments
B. Myofibrils
C. Sarcolemma
D. Muscle Fibers

[Biology | Unit: Support and Movement | Topic: Skeleton, muscles and joints]
Q.067. The length of myofibril from one Z-band to the next is known as:
A. Sarcomere
B. Sarcolemma
C. Sarcoplasm
D. Muscle Fiber

[Biology | Unit: Support and Movement | Topic: Skeleton, muscles and joints]
Q.068. The Ca++ ions released during a muscle fiber contraction attach with:
A. Myosin
B. Actin
C. Troponin
D. Tropomyosin

[Biology | Unit: Support and Movement | Topic: Skeleton, muscles and joints]
Q.069. A muscle condition resulting from the accumulation of lactic acid and ionic imbalance is:
A. Tetany
B. Muscle Fatigue
C. Cramp
D. Tetanus

[Biology | Unit: Support and Movement | Topic: Skeleton, muscles and joints]
Q.070. The pigment which stores oxygen in muscles is:
A. Hemoglobin
B. Myoglobin
C. Myosin
D. Actinomyosin

[Biology | Unit: Coordination and Control | Topic: Nervous system and receptors]
Q.071. Neurosecretory cells are present in which part of brain:
A. Hypothalamus
B. Midbrain
C. Pons
D. Cerebellum

[Biology | Unit: Biological Molecules | Topic: Carbohydrates, proteins, lipids and nucleic acids]
Q.072. Which of the following is the function of glucagon hormone?
A. Glycogen to Glucose
B. Glucose to Glycogen
C. Glucose to Lipids
D. Glucose to Proteins

[Biology | Unit: Coordination and Control | Topic: Nervous system and receptors]
Q.073. Addison’s disease is caused due to destruction of:
A. Adrenal Cortex
B. Pituitary Adrenal Axis
C. Adrenal Medulla
D. Hypothalamus

[Biology | Unit: Homeostasis | Topic: Kidney and osmoregulation]
Q.074. Which group of hormones is made up of amino acids and their derivatives?
A. Vasopressin and ADH
B. Epinephrine and Norepinephrine
C. Estrogen and Testosterone
D. Insulin and Glucagon

[Biology | Unit: Immunity | Topic: Immune response and vaccination]
Q.075. The thymus gland is involved in the maturation of:
A. Platelets
B. B-Lymphocytes
C. Eosinophils
D. T-Lymphocytes

[Biology | Unit: Immunity | Topic: Immune response and vaccination]
Q.076. In passive immunity which of the following component are injected into blood?
A. Antigens
B. Immunogens
C. Serum
D. Immunoglobulins

[Biology | Unit: Immunity | Topic: Immune response and vaccination]
Q.077. Mucous membranes are part of body defense system and they offer:
A. Physical Barriers
B. Mechanical Barriers
C. Chemical Barriers
D. Biological Barriers

[Biology | Unit: Immunity | Topic: Immune response and vaccination]
Q.078. Immediate protection is obtained from:
A. Passive Immunity
B. Active Immunity
C. Vaccination
D. Natural Activity Immunity

[Biology | Unit: Immunity | Topic: Immune response and vaccination]
Q.079. The immunity in which T-cells recognize the antigens or micro-organisms is known as;
A. Tissue Grafting
B. Phagocytosis
C. Cell Mediated Immunity / Response
D. Hormonal Immunity / Response

[Biology | Unit: Cell Structure and Function | Topic: Cells, organelles and chromosomes]
Q.080. Oxidative phosphorylation, the synthesis of ATP in the presence of O₂, occurs in:
A. Mitochondrial inner membrane
B. Cytoplasm
C. Outer membrane of mitochondria
D. Stroma of the chloroplast

[Biology | Unit: Bioenergetics | Topic: Cellular respiration and photosynthesis]
Q.081. Glycolysis is the breakdown of glucose into two molecules of:
A. Glycerate
B. Lactic Acid
C. Pyruvate
D. Succinic Acid

[Biology | Unit: Bioenergetics | Topic: Cellular respiration and photosynthesis]
Q.082. Before entering the Krebs cycle, the pyruvate is first decarboxylated and oxidized into:
A. Acetyl-CoA
B. Oxaloacetate
C. Lactic acid
D. Citric acid

[Biology | Unit: Bioenergetics | Topic: Cellular respiration and photosynthesis]
Q.083. Some electron from the second primary acceptor may pass back to chlorophyll molecules by electron carrier system, yielding ATP. This process is called:
A. Phosphorylation
B. Photophosphorylation
C. Non-Cyclic Phosphorylation
D. Cyclic Phosphorylation

[Biology | Unit: Bioenergetics | Topic: Cellular respiration and photosynthesis]
Q.084. Z-scheme is used for:
A. Non-Cyclic Photophosphorylation
B. Cyclic Photophosphorylation
C. Both Cyclic and Non-Cyclic Photophosphorylation
D. Oxidative Phosphorylation

[Biology | Unit: Biological Molecules | Topic: Carbohydrates, proteins, lipids and nucleic acids]
Q.085. The common vectors used in recombinant DNA technology are:
A. Probes
B. Palindromes
C. Plasmids
D. Prions

[Biology | Unit: Biological Molecules | Topic: Carbohydrates, proteins, lipids and nucleic acids]
Q.086. The enzyme used to isolate gene from DNA is:
A. Helicase
B. Reverse Transcriptase
C. Restriction Enzyme
D. DNA Polymerase

[Biology | Unit: Biological Molecules | Topic: Carbohydrates, proteins, lipids and nucleic acids]
Q.087. Which one of the following enzymes is temperature insensitive?
A. DNA Polymerase I
B. Taq Polymerase
C. DNA Polymerase III
D. RNA Polymerase

[Biology | Unit: Cell Structure and Function | Topic: Cells, organelles and chromosomes]
Q.088. When chromosomes uncoil, the nucleoli are reformed and two nuclei are the two poles of the cell; stage is known as:
A. Prophase
B. Metaphase
C. Telophase
D. Anaphase

[Biology | Unit: Inheritance | Topic: Mendelian and sex-linked inheritance]
Q.089. Mental retardation, short stature, broad face and squint eyes are the symptoms of:
A. Down’s syndrome
B. Klinefelter’s syndrome
C. Turner’s syndrome
D. XYZ syndrome

[Biology | Unit: Inheritance | Topic: Mendelian and sex-linked inheritance]
Q.090. Chiasmata formation takes place during the process which is known as:
A. Crossing Over
B. Attachment
C. Pairing
D. Leptotene

[Biology | Unit: Cell Structure and Function | Topic: Cells, organelles and chromosomes]
Q.091. Healing of a wound and repair is the phenomenon which takes place by the process of:
A. Mitosis
B. Meiosis
C. Cell Growth
D. Mitosis & Meiosis

[Biology | Unit: Cell Structure and Function | Topic: Cells, organelles and chromosomes]
Q.092. Which one of the following is the main cause of cancer?
A. Mutation
B. Controlled cell division
C. Regulated mitosis
D. Haploid division

[Biology | Unit: Biological Molecules | Topic: Carbohydrates, proteins, lipids and nucleic acids]
Q.093. The covalent bond formed between two monosaccharides is called:
A. Glycosidic Bond
B. Hydrogen Bond
C. Peptide Bond
D. Disulphide

[Biology | Unit: Inheritance | Topic: Mendelian and sex-linked inheritance]
Q.094. The bond formed between glucose and fructose form sucrose is:
A. 1,4 Glycosidic Linkage
B. 1,2 Glycosidic Linkage
C. 1,6 Glycosidic Linkage
D. 1,3 Glycosidic Linkage

[Biology | Unit: Biological Molecules | Topic: Carbohydrates, proteins, lipids and nucleic acids]
Q.095. In an amino acid in which the R-group is H, its name will be:
A. Alanine
B. Glycine
C. Leucine
D. Valine

[Biology | Unit: Biological Molecules | Topic: Carbohydrates, proteins, lipids and nucleic acids]
Q.096. Fatty acid are the organic compounds containing hydrogen, oxygen and one of the following are:
A. –COOH
B. –NH2
C. Acyl
D. Sucrose

[Biology | Unit: Circulation | Topic: Heart, blood and vessels]
Q.097. Liposomes are used in gene therapy against:
A. Hypercholesterolemia
B. Coronary Artery Angioplasty
C. Cystic Fibrosis
D. Severe Combined Immunodeficiency Syndrome (SCID)

[Biology | Unit: Support and Movement | Topic: Skeleton, muscles and joints]
Q.098. Genetically engineered cells are introduced into bone marrow cells in the treatment of:
A. Hypercholesterolemia
B. Severe Combined Immunodeficiency Syndrome (SCID)
C. Cystic Fibrosis
D. Coronary Artery Angioplasty

[Biology | Unit: Bioenergetics | Topic: Cellular respiration and photosynthesis]
Q.099. Which one of the following is depleting and causing thinning of ozone?
A. Chlorine
B. Bromine
C. Chlorofluorocarbon
D. Carbon

[Biology | Unit: Evolution | Topic: Evolution and natural selection]
Q.100. The typical environment of a particular organism population community is called:
A. Niche
B. Ecosystem
C. Habitat
D. Biosphere

[Biology | Unit: Biological Molecules | Topic: Carbohydrates, proteins, lipids and nucleic acids]
Q.101. Excessive enrichment of water with nutrients by human activity by which large amount of living organic matter grows is called:
A. Archeotrophication
B. Eutrophication
C. Enrichment
D. Low Trophication

[Biology | Unit: Bioenergetics | Topic: Cellular respiration and photosynthesis]
Q.102. In an ecosystem, mycorrhizae is an example of:
A. Symbiosis
B. Predation
C. Commensalism
D. Parasitism

[Biology | Unit: Bioenergetics | Topic: Cellular respiration and photosynthesis]
Q.103. Successive stages of eating and being eaten by which recycling of materials and flow of energy takes place is called:
A. Food Chain
B. Food Web
C. Trophic Level
D. Food Link

[Biology | Unit: Inheritance | Topic: Mendelian and sex-linked inheritance]
Q.104. The sex of individuals of the generation always depends on one of the parents who is:
A. Heterogametic
B. Homogametic
C. Isogametic
D. Isomorphic

[Biology | Unit: Inheritance | Topic: Mendelian and sex-linked inheritance]
Q.105. Which of the following will be hemophilic?
A. XHXh
B. XHXH
C. XhY
D. XHY

[Biology | Unit: Inheritance | Topic: Mendelian and sex-linked inheritance]
Q.106. Which of the following is an example of an X-linked recessive trait in humans?
A. Hypophospatemic Rickets
B. Color Blindness
C. Baldness
D. Beard Growth

[Biology | Unit: Inheritance | Topic: Mendelian and sex-linked inheritance]
Q.107. Which trait in human in an example of multiple alleles?
A. Eye Colour
B. Skin Colour
C. ABO-Blood Group
D. Rh-Blood Group

[Biology | Unit: Inheritance | Topic: Mendelian and sex-linked inheritance]
Q.108. When a gene pair at one locus interacts with another gene at another locus, the interaction is called:
A. Dominance
B. Multiple Alleles
C. Pleitropy
D. Epistasis

[Biology | Unit: Biological Molecules | Topic: Carbohydrates, proteins, lipids and nucleic acids]
Q.109. The combination of a pentose sugar with a base result in a compound is known as:
A. Nucleotide
B. Nucleoside
C. Nucleic Acid
D. Polynucleotide

[Biology | Unit: Enzymes | Topic: Enzymes and inhibition]
Q.110. An enzyme and substrate react through a special feature or site present in the enzyme:
A. Binding site
B. Active site
C. Catalyst site
D. Inhibition site

[Chemistry | Unit: Atomic Structure | Topic: Atomic models and electronic configuration]
Q.111. In mass spectrometer, detector or collector measures the:
A. Masses of isotopes
B. Percentages of isotopes
C. Relative abundances of isotopes
D. Mass numbers of isotopes

[Chemistry | Unit: Introduction to Chemistry | Topic: Stoichiometry and mole concept]
Q.112. How many 'Cl' (chlorine) molecules are in two moles of chlorine?
A. 2 × 6.02 × 10-23 molecules
B. 35.5 × 6.02 × 1023 molecules
C. 2 × 1023 molecules
D. 2 × 6.02 × 1023 molecules

[Chemistry | Unit: Liquids and Solids | Topic: Intermolecular forces and states of matter]
Q.113. Melting point of water is higher than petrol, because intermolecular forces in water are:
A. Weaker than petrol
B. Stronger than petrol
C. Same as in petrol
D. Negligible

[Chemistry | Unit: Chemical Bonding | Topic: Bonding and molecular shape]
Q.114. DNA molecule is double stranded, in which two chains of DNA are twisted around each other by:
A. Hydrogen bonds
B. Vander Waal's force
C. Covalent bonds
D. Dative bonds

[Chemistry | Unit: S- and P-Block Elements | Topic: Periodic trends and main-group chemistry]
Q.115. The elements for which the value of ionisation energy is low, can:
A. Gain electrons readily
B. Gains electron with difficulty
C. Lose electrons less readily
D. Lose electrons readily

[Chemistry | Unit: Atomic Structure | Topic: Atomic models and electronic configuration]
Q.116. The nature of cathode rays in discharge tube:
A. Depends on the nature of gas taken in the discharge tube
B. Depends upon the nature of cathode in discharge tube
C. Is independent of the nature of the gas in discharge tube
D. Depends upon the nature of anode in the discharge tube

[Chemistry | Unit: Chemical Bonding | Topic: Bonding and molecular shape]
Q.117. The ability of an atom in a covalent bond to attract the bonding electrons is called:
A. Ionization energy
B. Ionic bond energy
C. Electronegativity
D. Electron affinity

[Chemistry | Unit: Chemical Bonding | Topic: Bonding and molecular shape]
Q.118. The paramagnetic character of a substance is due to:
A. Bond pairs of electrons
B. Lone pairs of electrons
C. Unpaired electrons in atom or molecule
D. Paired electrons in valence shells of electrons

[Chemistry | Unit: Liquids and Solids | Topic: Intermolecular forces and states of matter]
Q.119. Lattice energy of an ionic crystal is the enthalpy of:
A. Combustion
B. Dissociation
C. Dissolution
D. Formation

[Chemistry | Unit: Thermochemistry and Energetics | Topic: Heat, enthalpy and thermodynamics]
Q.120. In Standard Enthalpy of Atomization, heat of the surrounding:
A. Remains unchanged
B. Increases
C. Increases than decreases
D. Decreases

[Chemistry | Unit: Introduction to Chemistry | Topic: Stoichiometry and mole concept]
Q.121. Mole fraction of any compound is the ratio of moles of all components in a:
A. Compound
B. Solution
C. Molecule
D. Solid

[Chemistry | Unit: Introduction to Chemistry | Topic: Stoichiometry and mole concept]
Q.122. Molarity is defined as the number of moles of any substance dissolved:
A. Per dm3 of water
B. In one gram of water
C. Per m3 of water
D. In 100 ml of water

[Chemistry | Unit: Electrochemistry | Topic: Redox and electrochemical cells]
Q.123. In an electrolytic cell, a salt bridge is used in order to:
A. Pass the electric current
B. Mix solution of two half-cells
C. Prevent the flow of ions
D. Allow movement of ions between two half-cells

[Chemistry | Unit: Electrochemistry | Topic: Redox and electrochemical cells]
Q.124. In all oxidation reactions, atoms of an element in a chemical species lose electrons and increase their:
A. Oxidation states
B. Reductions
C. Electrode
D. Negative charges

[Chemistry | Unit: Chemical Equilibrium | Topic: Equilibrium and buffers]
Q.125. In 'AgCl' solution, some salt of NaCl is added, 'AgCl' will be precipitated due to:
A. Solubility
B. Electrolyte
C. Unsaturation effect
D. Common ion effect

[Chemistry | Unit: Chemical Equilibrium | Topic: Equilibrium and buffers]
Q.126. ‘Ka’ for an acid is higher, the stronger is the acid; relate the strength of an acid with ‘pKa’:
A. Higher pKa, weaker the acid
B. Lower pKa, stronger the acid
C. pKa has no relation with acid strength
D. Both “Higher pKa, weaker the acid” & “Lower pKa, stronger the acid”

[Chemistry | Unit: Reaction Kinetics | Topic: Rate and activation energy]
Q.127. It is experimentally found that a catalyst is used to:
A. Lower the activation energy
B. Increase the activation energy
C. Lower the pH
D. Decrease the temp of the reaction

[Chemistry | Unit: Reaction Kinetics | Topic: Rate and activation energy]
Q.128. According to collision theory of bimolecular reaction in gas phase, the minimum amount of energy required for an effective collision is known as:
A. Heat of reaction
B. Rate of reaction
C. Has no effect on the reaction
D. Energy of activation

[Chemistry | Unit: S- and P-Block Elements | Topic: Periodic trends and main-group chemistry]
Q.129. Carbon exists as allotropes, which are different crystalline or molecular forms of the same substance. Graphite and diamond are allotropes of carbon. Diamond is a non-conductor whereas graphite is a good conductor because:
A. Graphite has a layered structure
B. In graphite, all valence electrons are tetrahedrally bound
C. In graphite one of valence electron is free to move
D. Graphite is soft and greasy bound

[Chemistry | Unit: S- and P-Block Elements | Topic: Periodic trends and main-group chemistry]
Q.130. The diagram below is a plot of melting points of elements of second period against their atomic numbers. Lithium and fluorine are placed at the extreme ends of the plot, on the basis of melting points where will you place Carbon among the empty slots on the plot?
A. 1
B. 2
C. 4
D. 3

[Chemistry | Unit: S- and P-Block Elements | Topic: Periodic trends and main-group chemistry]
Q.131. When elements of group II-A (alkaline earth metals) are exposed to air, they quickly become coated with a layer of oxide. What is the purpose of this oxide layer?
A. The oxide layer exposes the metal to Atmospheric attack
B. The oxide layer increases the reactivity of metal
C. The oxide layer protects the metal from further atmospheric attack
D. The oxide layer gives the metal a shiny silvery appearance

[Chemistry | Unit: S- and P-Block Elements | Topic: Periodic trends and main-group chemistry]
Q.132. In silicon dioxide each silicon atom is tetrahedrally bonded to four oxygen atoms and each oxygen atom is bonded to two silicon atoms. The ratio of silicon to oxygen atoms is:
A. 2:2
B. 1:2
C. 2:1
D. 1:4

[Chemistry | Unit: Chemistry of Hydrocarbons | Topic: Alkanes, alkenes, alkynes and benzene]
Q.133. Hydrogenation of unsaturated oils is done by using:
A. Finely divided nickel
B. Finely divided iron
C. Vanadium pentaoxide
D. Copper

[Chemistry | Unit: S- and P-Block Elements | Topic: Periodic trends and main-group chemistry]
Q.134. Pick the correct statement:
A. Chelates are usually more stable than ordinary complexes
B. Ordinary complexes are more stable than chelates
C. Monodentate ligands form the chelates complexes
D. Chelates have no ring structures

[Chemistry | Unit: Reaction Kinetics | Topic: Rate and activation energy]
Q.135. In contact process, the catalyst used for the conversion of Sulphur dioxide to Sulphur trioxide is:
A. Magnesium oxide
B. Aluminum oxide
C. Silicon dioxide
D. Vanadium pentoxide

[Chemistry | Unit: Industrial Chemistry | Topic: Industrial processes and materials]
Q.136. The unpolluted natural rainwater is slightly acidic due to the reaction of rain water with:
A. Sulphur dioxide
B. Oxides of nitrogen
C. Carbon dioxide
D. Hydrogen present in air

[Chemistry | Unit: Industrial Chemistry | Topic: Industrial processes and materials]
Q.137. In the Haber process for manufacturing of ammonia, Nitrogen is taken from:
A. Proteins occurring in living bodies
B. Ammonium salts obtained industrially
C. Air
D. Minerals containing nitrates

[Chemistry | Unit: S- and P-Block Elements | Topic: Periodic trends and main-group chemistry]
Q.138. In comparison with oxygen gas, a strong triple bond is present between two nitrogen atoms in a molecule and therefore nitrogen gas is:
A. Highly reactive gas
B. Completely inert like noble gases
C. Very less reactive gas
D. Moderately reactive gas

[Chemistry | Unit: Alkyl Halides | Topic: Nucleophilic substitution]
Q.139. The compound with an atom, which has unshared pair of electrons is called:
A. Nucleophile
B. Electrophile
C. Protophile
D. None of the given options

[Chemistry | Unit: Fundamental Principles of Organic Chemistry | Topic: Organic nomenclature and isomerism]
Q.140. 1-chloropropane and 2-chloropropane are isomers of each other, the type of isomerism in these two is called:
A. Cis-trans isomerism
B. Chain isomerism
C. Position isomerism
D. Functional group isomerism

[Chemistry | Unit: Chemistry of Hydrocarbons | Topic: Alkanes, alkenes, alkynes and benzene]
Q.141. Benzene in the presence of AlCl3 produces acetophenone when reacts with:
A. Acetyl chloride
B. Acetic acid
C. Ethyl benzene
D. Ethanoic acid

[Chemistry | Unit: Chemistry of Hydrocarbons | Topic: Alkanes, alkenes, alkynes and benzene]
Q.142. The substitution of a '-H' by '-NO2' group in benzene is called:
A. Nitration
B. Ammonolysis
C. Sulphonation
D. Reduction of benzene

[Chemistry | Unit: Chemistry of Hydrocarbons | Topic: Alkanes, alkenes, alkynes and benzene]
Q.143. When purely alcoholic solution of sodium/potassium hydroxide and halogenoalkanes are reacted an alkene is formed, what is the mechanism of reaction?
A. Elimination
B. Dehydration
C. Debromination
D. Reduction of benzene

[Chemistry | Unit: Fundamental Principles of Organic Chemistry | Topic: Organic nomenclature and isomerism]
Q.144. The organic compound carbon tetrachloride is used as:
A. Lubricant
B. Solvent
C. Oxidant
D. Plastic

[Chemistry | Unit: Alcohols and Phenols | Topic: Alcohol and phenol reactions]
Q.145. An alcohol is converted to an aldehyde with same number of carbon atoms as that of alcohol in the presence of K2Cr2O7/H2SO4 the alcohol is:
A. CH3Cl(CH)2OH
B. CH3CH2CH2OH
C. (CH3)3COH
D. (CH3)3CHOH

[Chemistry | Unit: Alcohols and Phenols | Topic: Alcohol and phenol reactions]
Q.146. Which of the following is a secondary alcohol?
A. Propan-2-ol
B. Ethanol
C. Methanol
D. 2-methylpropan-2-ol

[Chemistry | Unit: Macromolecules | Topic: Polymers and biomolecules]
Q.147. Which enzyme is involved in the fermentation of glucose:
A. Zymase
B. Invertase
C. Urease
D. Diastase

[Chemistry | Unit: Alcohols and Phenols | Topic: Alcohol and phenol reactions]
Q.148. Relative acidic strength of alcohol, phenol, water and carboxylic acid is:
A. Carboxylic acid > Alcohol > Phenol > Water CH3
B. Carboxylic acid > Phenol > Water > Alcohol
C. Phenol > Carboxylic acid > Alcohol > Water
D. Water > Alcohol > Phenol > Carboxylic acid

[Chemistry | Unit: Aldehydes and Ketones | Topic: Carbonyl compounds]
Q.149. Consider the following reaction:R―CHO + 2[Ag(NH3)2]OH → R―COONH4 + 2Ag + 2NH3 + H2O. This reaction represents one of the following tests?
A. Fehling's test
B. Benedict's test
C. Ninhydrin's test
D. Tollen's test

[Chemistry | Unit: Alkyl Halides | Topic: Nucleophilic substitution]
Q.150. In the below reaction, the nucleophile is:
A. CN-
B. HCl
C. Cl
D. OH

[Chemistry | Unit: Aldehydes and Ketones | Topic: Carbonyl compounds]
Q.151. Which one of the following compounds belongs to the homologous series of aldehydes?
A. Methanal
B. Methanol
C. Methanoic acid
D. Methoxy methane

[Chemistry | Unit: Carboxylic Acids | Topic: Carboxylic acids and derivatives]
Q.152. The products of the reaction given below are:CH3COOH + PCl5 → ?
A. CH3COCl + POCl3 + HCl
B. CH3COCl + POCl2 + HCl
C. CH3Cl + POCl3 + HCl
D. CH3COCl + POCl3 + H2

[Chemistry | Unit: Carboxylic Acids | Topic: Carboxylic acids and derivatives]
Q.153. CH3CN +H2O + HCl → A + B In the reaction given above, A and B are:
A. Acetic acid and acid amide
B. Acetic acid and methyl chloride
C. Acetic acid and ammonia
D. Acetic acid and ammonium chloride

[Chemistry | Unit: Carboxylic Acids | Topic: Carboxylic acids and derivatives]
Q.154. Consider the following reaction:CH3COOH + Mg (metal) → ?What product will form?
A. Magnesium formate
B. Magnesium acetate
C. Magnesium ion
D. Carboxylate ion

[Chemistry | Unit: Macromolecules | Topic: Polymers and biomolecules]
Q.155. The ―NH―CO is called:
A. Amide group
B. Amino group
C. Protein linkage
D. Peptide linkage

[Chemistry | Unit: Macromolecules | Topic: Polymers and biomolecules]
Q.156. Which one of the following is an alpha amino acid?
A. Glycine
B. Serine
C. Glutamine
D. Lysine

[Chemistry | Unit: Macromolecules | Topic: Polymers and biomolecules]
Q.157. Which of the following has an amino R-group?
A. Lysine
B. Proline
C. Valine
D. Alanine

[Chemistry | Unit: Chemical Equilibrium | Topic: Equilibrium and buffers]
Q.158. At intermediate value of pH, amino acids form Zwitter ions containing:
A. ―NH3+ and COO-
B. ―NH3 and COO-
C. ―NH3+ and COOH
D. ―NH3 and COOH

[Chemistry | Unit: Carboxylic Acids | Topic: Carboxylic acids and derivatives]
Q.159. When hexane dioic acid is heated with hexamethylene diamine, the compound formed is:
A. Polypeptide
B. Addition polymer
C. Ester
D. Nylon 6,6

[Chemistry | Unit: Macromolecules | Topic: Polymers and biomolecules]
Q.160. A polymer in which the number of amino acid residue is greater than 100 or molecular mass is greater than 1000, is known as:
A. Protein
B. Polypeptide
C. Dipeptide
D. Tripeptide

[Chemistry | Unit: Macromolecules | Topic: Polymers and biomolecules]
Q.161. Aspartic acid is an acidic amino acid, which has chemical formula:
A. HOOC-CH2-CH(NH2)-COOH
B. H2N-CH2-COOH
C. CH3-CH(NH2)-COOH
D. HOOC-(CH2)2-CH(NH2)-COOH

[Chemistry | Unit: Macromolecules | Topic: Polymers and biomolecules]
Q.162. Glucose and fructose are common examples of:
A. Pentoses
B. Hexoses
C. Heptoses
D. Butoses

[Chemistry | Unit: Macromolecules | Topic: Polymers and biomolecules]
Q.163. The reaction between fats and caustic soda is called:
A. Hydrogenolysis
B. Fermentation
C. Carboxylation
D. Saponification

[Chemistry | Unit: Macromolecules | Topic: Polymers and biomolecules]
Q.164. Macromolecules are described as large molecules built up from small repeating units known as:
A. Monomers
B. Isomers
C. Metameres
D. Tautomer

[Chemistry | Unit: Macromolecules | Topic: Polymers and biomolecules]
Q.165. Polyvinyl chloride is an example of:
A. Addition polymer
B. Condensation polymer
C. Biopolymer
D. Thermosetting polymer

[Chemistry | Unit: Macromolecules | Topic: Polymers and biomolecules]
Q.166. Terylene, a polyester is an example of:
A. Biopolymer
B. Lipids
C. Condensation polymer
D. Addition polymer

[Chemistry | Unit: Industrial Chemistry | Topic: Industrial processes and materials]
Q.167. The suspected liver carcinogen which also has negative reproduction and developmental effects on humans is:
A. Iodoform
B. Bromoform
C. Tropoform
D. Chloroform

[Chemistry | Unit: Industrial Chemistry | Topic: Industrial processes and materials]
Q.168. Peroxyacetyl nitrate is an irritant to human beings and it effects:
A. Nose
B. Stomach
C. Ears
D. Eyes

[Physics | Unit: Force and Motion | Topic: Kinematics, Newton laws and momentum]
Q.169. When the dimensions of both sides of an equation are equal, then the equation is said to be:
A. Simultaneous
B. Homogeneous
C. Instantaneous
D. Quadratic

[Physics | Unit: Force and Motion | Topic: Kinematics, Newton laws and momentum]
Q.170. Radian is a unit of angular displacement that can also be measured in degrees. How many radians are equal to one degree?
A. 180/π
B. π/180
C. 2π/180
D. π/57.3

[Physics | Unit: Force and Motion | Topic: Kinematics, Newton laws and momentum]
Q.171. An elevator is moving upwards with constant velocity of ‘v’. What is the weight of a person of a mass ‘m’ inside the elevator during upward motion?
A. mg + mv
B. mg
C. mg ― mv
D. Zero

[Physics | Unit: Fluid Dynamics | Topic: Fluid flow and Bernoulli principle]
Q.172. An object having spherical shape of radius ‘r’ experiences a retarding force F from a fluid of coefficient of viscosity ‘η’ when moving through the fluid with speed ‘v’. What is the ratio of retarding force to speed?
A. 6πη r2
B. 6πη/r2
C. 6πη r
D. 6πη/r

[Physics | Unit: Force and Motion | Topic: Kinematics, Newton laws and momentum]
Q.173. When the drag force is equal to the weight of the droplet, the droplet will fall with:
A. High Speed
B. Low Speed
C. Certain acceleration
D. Constant Speed

[Physics | Unit: Rotational and Circular Motion | Topic: Angular motion and torque]
Q.174. A simple pendulum length ‘L’ with bob of mass ‘m’ is slightly displaced from its mean position so that it string makes an angle ‘θ’ with vertical line as shown in the figure. Then bob of pendulum released. What will be the expression of torque with which the bob starts to move towards the mean position?
A. mgL
B. mgL sin θ
C. 0
D. mgL cos θ

[Physics | Unit: Fluid Dynamics | Topic: Fluid flow and Bernoulli principle]
Q.175. The density of blood is:
A. Less than water
B. Nearly equal to water
C. Greater than water
D. Three times that of water

[Physics | Unit: Waves | Topic: Waves, sound and SHM]
Q.176. A monochromatic light of wavelength ‘λ’ is used to produce the diffraction pattern through a single slit of width X. Which one of the following represents the intensity distribution across the screen?
A. Central maximum with decreasing secondary maxima
B. Uniform brightness everywhere
C. Alternating dark and bright rings
D. Single bright line only

[Physics | Unit: Waves | Topic: Waves, sound and SHM]
Q.177. For interference of light waves to take place, the required condition is:
A. The path difference of the light waves from the two sources must be large
B. The interfering waves must be non-coherent
C. The light waves may come from different sources
D. The light waves must come from two coherent sources

[Physics | Unit: Waves | Topic: Waves, sound and SHM]
Q.178. The property of bending of light around an obstacle and spreading of light waves into a geometric shadow of an obstacle is called:
A. Diffraction of Light
B. Polarization of Light
C. Quantization of Light
D. Interference of Light

[Physics | Unit: Waves | Topic: Waves, sound and SHM]
Q.179. The normal human eye can focus a sharp image of an object on the eye if the object is located at certain distance called:
A. Least Point
B. Near Point
C. Far Point
D. Distinct Point

[Physics | Unit: Waves | Topic: Waves, sound and SHM]
Q.180. A source of sound wave emits waves of frequency ‘f’. If ‘v’ is speed of sound waves, then what will be the wavelength of the waves:
A. v/f
B. vf
C. (v-uo) / f
D. (v−uo) f

[Physics | Unit: Waves | Topic: Waves, sound and SHM]
Q.181. The spectrum of a star’s light is measured and the wavelength of one of the lines as the sodium’s line is found to be 589 nm. The same line has the wavelength of 497 nm when observed in the laboratory. This means the star is:
A. Moving away from the earth
B. Moving towards the north
C. Stationary
D. Revolving around the planet

[Physics | Unit: Waves | Topic: Waves, sound and SHM]
Q.182. What is the period of the mass-spring system during SHM if the ratio of mass to spring constant is ¼?
A. π
B. 2 π
C. 1/π
D. ½ π

[Physics | Unit: Force and Motion | Topic: Kinematics, Newton laws and momentum]
Q.183. The waveform of SHM is given in the figure. At what time/times displacement is equal to zero?
A. T/4 only
B. 3T/4
C. 0, T/4, 3T/4 and T
D. 0, T/2 and T

[Physics | Unit: Waves | Topic: Waves, sound and SHM]
Q.184. A wire is stretched by a force that causes an extension. The energy is stored in it only when:
A. The extension of wire is proportional to force applied
B. The cross-section area of the wire remains constant
C. The wire is not stretched beyond its elastic limit
D. The weight of wire is negligible

[Physics | Unit: Waves | Topic: Waves, sound and SHM]
Q.185. Which of the following statements is correct:
A. Elasticity is that property of body which enables body to regain its original dimension
B. Elasticity is that property of a body that does not allow it to return to its original shape
C. Elasticity is that property of a body that allows it to retain its original shape and dimension after the stress is removed
D. Elasticity is that property of a body that obeys Hooke’s law

[Physics | Unit: Thermodynamics | Topic: Heat and thermal physics]
Q.186. Which of the following is the expression of root mean square speed of a gas having n number of molecules contained in the container?
A. √(Σv^2 / N)
B. Σv / N
C. (Σv / N)^2
D. √(Σv / N)

[Physics | Unit: Thermodynamics | Topic: Heat and thermal physics]
Q.187. For a gas of volume V in its equilibrium state, if the pressure does change with time then total kinetic energy of gas is constant because:
A. Collisions between gas molecules occur
B. Collisions between gas molecules occur linearly
C. Collisions must be elastic
D. Collisions must be inelastic

[Physics | Unit: Electronics | Topic: Semiconductors and electronic devices]
Q.188. Which of the following is the proper way to study the sinusoidal waveform of the voltage?
A. Voltage is connected to X input and the time base is switched off
B. Voltage is connected to Y input and the time base is switched on
C. Voltage is connected to Y input and the time base is switched off
D. Voltage is connected to X input and the time base is switched on

[Physics | Unit: Electrostatics | Topic: Electric field, potential and capacitance]
Q.189. The electron gun in a cathode ray oscilloscope contains:
A. Filament, cathode, grid, anodes
B. Cathode, anode, capacitor, screen
C. Emitter, base, collector
D. Resistance, capacitor, inductor

[Physics | Unit: Thermodynamics | Topic: Heat and thermal physics]
Q.190. In which of the following, the change in internal energy is more?
A. In system A
B. In system B
C. Cannot be predicted
D. Change is zero in both. (both are cyclic)

[Physics | Unit: Thermodynamics | Topic: Heat and thermal physics]
Q.191. Pressure volume graph of two systems 'A' and 'B' are plotted under isothermal and adiabatic conditions. Which of the following observation of graph represents the two systems?
A. System with steeper slope is adiabatic
B. System with steeper slope is isothermal
C. Both have identical slopes
D. Adiabatic is horizontal

[Physics | Unit: Thermodynamics | Topic: Heat and thermal physics]
Q.192. Which of the following curve is an isotherm?
A. Hyperbolic curve at constant temperature
B. Parabolic curve
C. Straight vertical line
D. Horizontal line

[Physics | Unit: Current Electricity | Topic: Circuits and resistance]
Q.193. If 2 A current passes through a resistor when connected to a certain battery. If the resistance is replaced by double the resistance, then the current will become:
A. 2 A
B. 4 A
C. 6 A
D. 1 A

[Physics | Unit: Waves | Topic: Waves, sound and SHM]
Q.194. In a Helium-Neon laser, population inversion of _ atoms is achieved which emits radiations, when they are stimulated to fall at a lower level.
A. Neon
B. Helium
C. Helium and Neon
D. Chromium

[Physics | Unit: Current Electricity | Topic: Circuits and resistance]
Q.195. Three resistors each having value 'R' are connected as shown in figure. What is the equivalent resistance between 'X' and 'Y'?
A. 3R
B. R
C. R/3
D. R3

[Physics | Unit: Current Electricity | Topic: Circuits and resistance]
Q.196. If the number of turns of a solenoid circular coil is doubled, but the current in the coil and radius of the coil remain the same, then what will be the magnetic flux density produced by the coil?
A. Magnetic flux density will be halved
B. Magnetic flux density increases by different amount at different points
C. Magnetic flux density remains unchanged
D. Magnetic flux density will be doubled

[Physics | Unit: Current Electricity | Topic: Circuits and resistance]
Q.197. Two long parallel wires Wire 1 and Wire 2 repel each other as shown in the figure. What could be the reasons?
A. Both carry current in same direction
B. Both carry current in opposite direction
C. Wire 1 has current, but Wire 2 has no current
D. Wire 2 has current, Wire 1 has no current

[Physics | Unit: Current Electricity | Topic: Circuits and resistance]
Q.198. The diagram shows a wire, carrying a current 'I', placed between the poles of a magnet. In which direction does the force on the wire act?
A. Upwards
B. Downwards
C. Towards the ‘N’ pole of the magnet
D. Towards the ‘S’ pole of the magnet

[Physics | Unit: Waves | Topic: Waves, sound and SHM]
Q.199. Wavelength of X-rays is the order of:
A. 10-6 m
B. 10-10 m
C. 10-13 m
D. 100 m

[Physics | Unit: Waves | Topic: Waves, sound and SHM]
Q.200. Laser beam can be used to generate three-dimensional image of object in a process called:
A. Computed technology
B. Computed tomography
C. Holography
D. Computerized axial tomography

[Physics | Unit: Waves | Topic: Waves, sound and SHM]
Q.201. Which of the following is true for Lasers?
A. Electrons are emitted
B. Stimulated emission of electrons is needed
C. Coherent monochromatic light is emitted
D. There is a population inversion of photons

[Physics | Unit: Current Electricity | Topic: Circuits and resistance]
Q.202. Three resistors of resistance R1, R2, and R3 are connected as shown in the figure.The equivalent resistance is:
A. R1 + R2 + R3
B. (R1R2)/(R1+R2) + R3
C. R1R2R3
D. 1/R1 + 1/R2 + 1/R3

[Physics | Unit: Dawn of Modern Physics | Topic: Photon and quantum physics]
Q.203. What is meant by spontaneous emission of electrons in solids?
A. Electrons being emitted by the solids through photoelectric effect when irradiated with electromagnetic radiation
B. Incident electrons colliding with electrons in solids and releasing doubling the number of incident electrons
C. Electrons in solids are emitted without any external stimulus through radiation
D. Excited electrons going back to lower energy states immediately by releasing energy.

[Physics | Unit: Dawn of Modern Physics | Topic: Photon and quantum physics]
Q.204. When electrons lose all their kinetic energy in the first collision, the entire kinetic appears as an X-ray photon of energy:
A. K.E. = eV
B. K.E. = hλmin/c
C. K.E. = hc/λmin
D. K.E. = h/λmax

[Physics | Unit: Dawn of Modern Physics | Topic: Photon and quantum physics]
Q.205. The characteristic X-ray spectrum is due to:
A. The absorption of neutrons by target material
B. The bombardment of target material by protons
C. The bombardment of target material by electrons
D. The bombardment of target material by alpha particles

[Physics | Unit: Nuclear Physics | Topic: Radioactivity and nuclear decay]
Q.206. The ionizing capability of gamma rays is:
A. Equal to alpha and beta particle
B. Less than alpha but greater than beta particles
C. Less than both alpha and beta particles
D. Less than beta but greater than alpha particles

[Physics | Unit: Nuclear Physics | Topic: Radioactivity and nuclear decay]
Q.207. The half-life of a radioactive element is:
A. Inversely proportional to square of decay constant
B. Directly proportional to square of decay constant
C. Directly proportional to decay constant
D. Inversely proportional to decay constant

[Physics | Unit: Nuclear Physics | Topic: Radioactivity and nuclear decay]
Q.208. The transformation of a neutron into proton in the nucleus, gives rise to emission of:
A. Beta particles
B. Gamma particles
C. Alpha particles
D. X-rays

[Physics | Unit: Nuclear Physics | Topic: Radioactivity and nuclear decay]
Q.209. The ratio of the rate of decay of a parent atom to the number of radioactive nuclei present at that time is equal to:
A. Half-life of radioactive element
B. Mean life
C. Decay constant of radioactive element
D. Activity of radioactive element

[Physics | Unit: Nuclear Physics | Topic: Radioactivity and nuclear decay]
Q.210. Which one of the following particles is emitted as a result of the following nuclear reaction?Ra226 → Rn222
A. Beta
B. Alpha
C. Gamma rays
D. One alpha and one beta

[Physics | Unit: Nuclear Physics | Topic: Radioactivity and nuclear decay]
Q.211. Which of the following is used to estimate the circulation of blood in a patient?
A. Carbon-14
B. Carbon-12
C. Phosphorus-3
D. Sodium-24

[Physics | Unit: Nuclear Physics | Topic: Radioactivity and nuclear decay]
Q.212. For the radiotherapy of a patient, it is required to double the absorbed dose in gray. What step must be taken?
A. Energy must be quadrated
B. Energy must be halved
C. Energy must be raised four times
D. Energy must be doubled

[English | Unit: Reading and Thinking Skills | Topic: Grammar, vocabulary, comprehension]
Q.213. The authorities have _ that the plane to Beirut was hijacked over the Indian Ocean.
A. Assured
B. Confirmed
C. Committed
D. Ensured

[English | Unit: Reading and Thinking Skills | Topic: Grammar, vocabulary, comprehension]
Q.214. She has let _ her house fully furnished to a Korean couple.
A. out
B. at
C. up
D. in

[English | Unit: Reading and Thinking Skills | Topic: Grammar, vocabulary, comprehension]
Q.215. I have no _ to listen to the budget speech.
A. Trouble
B. Convenience
C. Patience
D. Perseverance

[English | Unit: Reading and Thinking Skills | Topic: Grammar, vocabulary, comprehension]
Q.216. Your _ too long you had better go to the hairdresser today:
A. Hair is
B. Hair are
C. Hairs are
D. Hairs is

[English | Unit: Reading and Thinking Skills | Topic: Grammar, vocabulary, comprehension]
Q.217. Change the voice of the statement;"Work hard."
A. Let the work be hard
B. Work be hard
C. Let you work be hard
D. You are advised to work hard

[English | Unit: Reading and Thinking Skills | Topic: Grammar, vocabulary, comprehension]
Q.218. Convert into Passive Voice"She spoke to the official on duty."
A. The official on duty was spoken to by her.
B. The official was spoken to by her on duty.
C. She was spoken to by the official on duty.
D. She was the official to be spoken to on duty.

[English | Unit: Reading and Thinking Skills | Topic: Grammar, vocabulary, comprehension]
Q.219. Convert into Passive Voice;"The doctor advised the patient not to eat rice."
A. The patient was advised by the doctor not to eat rice.
B. The patient was advised by the doctor that he should not eat rice.
C. The patient was being advised by the doctor that he should not rice by the doctor.
D. The patient has been advised not to eat rice by the doctor.

[English | Unit: Reading and Thinking Skills | Topic: Grammar, vocabulary, comprehension]
Q.220. Convert into Passive Voice;''I cannot accept your offer."
A. Your offer cannot be accepted by me.
B. I cannot be accepted by your offer.
C. The offer cannot be accepted by me.
D. Your offer cannot be accepted.
"""

q2011 = parse_year_text(2011, RAW_2011)
save_year_json(2011, q2011)
print("2011 saved:", len(q2011))
