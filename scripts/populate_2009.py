import os
import sys
sys.path.append(os.path.dirname(__file__))
from parser_helper import parse_year_text, save_year_json

RAW_2009 = """
[English | Unit: Formal and Lexical Skills | Topic: Vocabulary, sentence correction and usage]
Q.001. The traveler _ a long detour to water the camels.
A. Took
B. Sought
C. Saw
D. Made

[English | Unit: Formal and Lexical Skills | Topic: Vocabulary, sentence correction and usage]
Q.002. Shah Jahan _ the great mosque at Delhi.
A. Founded
B. Created
C. Raised
D. Established

[English | Unit: Formal and Lexical Skills | Topic: Vocabulary, sentence correction and usage]
Q.003. He was _ of theft in the court.
A. Charged
B. Blamed
C. Reported
D. Accused

[English | Unit: Formal and Lexical Skills | Topic: Vocabulary, sentence correction and usage]
Q.004. He _on a very extraordinary ambition.
A. Arrived
B. Came
C. Decided
D. Hit

[English | Unit: Formal and Lexical Skills | Topic: Vocabulary, sentence correction and usage]
Q.005. SPOT THE ERROR: In the following sentences, some segments of each sentence are underlined. Your task is to identify that underlined segment of the sentence, which contains the mistake that needs to be corrected. Fill the Circle corresponding to that letter under the segment in the MCQ Response From.He is better than all the boys in the class, in studies as well as in sports, and bags big prizes in various field.
A. Better than
B. As well as
C. Bags
D. Various

[English | Unit: Formal and Lexical Skills | Topic: Vocabulary, sentence correction and usage]
Q.006. SPOT THE ERROR: In the following sentences, some segments of each sentence are underlined. Your task is to identify that underlined segment of the sentence, which contains the mistake that needs to be corrected. Fill the Circle corresponding to that letter under the segment in the MCQ Response From.One must not depend too much upon one’s hard work, as provident also plays its part.
A. Too much
B. One’s hard work
C. Provident
D. Plays its part

[English | Unit: Formal and Lexical Skills | Topic: Vocabulary, sentence correction and usage]
Q.007. SPOT THE ERROR: In the following sentences, some segments of each sentence are underlined. Your task is to identify that underlined segment of the sentence, which contains the mistake that needs to be corrected. Fill the Circle corresponding to that letter under the segment in the MCQ Response From.His first adventure was to go round through the world at minimum cost.
A. First adventure
B. Go round
C. Through
D. Minimum cost

[English | Unit: Formal and Lexical Skills | Topic: Vocabulary, sentence correction and usage]
Q.008. SPOT THE ERROR: In the following sentences, some segments of each sentence are underlined. Your task is to identify that underlined segment of the sentence, which contains the mistake that needs to be corrected. Fill the Circle corresponding to that letter under the segment in the MCQ Response From.He has been working in this department since the last five years without any break.
A. Has been working
B. Since
C. Last five years
D. Break

[English | Unit: Formal and Lexical Skills | Topic: Vocabulary, sentence correction and usage]
Q.009. SPOT THE ERROR: In the following sentences, some segments of each sentence are underlined. Your task is to identify that underlined segment of the sentence, which contains the mistake that needs to be corrected. Fill the Circle corresponding to that letter under the segment in the MCQ Response From.He reached at Lahore only a few days ago, on last Friday, to be exact, and is going to stay here for some time
A. Reached at
B. A few
C. To be exact,
D. Is going to stay

[English | Unit: Formal and Lexical Skills | Topic: Vocabulary, sentence correction and usage]
Q.010. SPOT THE ERROR: In the following sentences, some segments of each sentence are underlined. Your task is to identify that underlined segment of the sentence, which contains the mistake that needs to be corrected. Fill the Circle corresponding to that letter under the segment in the MCQ Response From.There was a big rally on the Mall, but as the crowd disintegrated, chaos and confusion ruled everywhere.
A. A big rally
B. Disintegrated
C. Chaos
D. Ruled

[English | Unit: Formal and Lexical Skills | Topic: Vocabulary, sentence correction and usage]
Q.011. In each of the following question, four alternative sentences are given. Choose the CORRECT one and fill the Circle corresponding to that letter in the MCQ Response Form.
A. E-mail is a relatively new mean of communication.
B. E-mail is a relatively new means of communication.
C. E-mail is a relatively new mean to communication.
D. E-mail is a relatively new means to communication.

[English | Unit: Formal and Lexical Skills | Topic: Vocabulary, sentence correction and usage]
Q.012. In each of the following question, four alternative sentences are given. Choose the CORRECT one and fill the Circle corresponding to that letter in the MCQ Responsen Form.
A. As she said the computer was programmed by Mona.
B. Just like she said the computer was programmed by Mona.
C. As like she said the computer was programmed by Mona.
D. Just like she had she said the computer was programmed by Mona.

[English | Unit: Formal and Lexical Skills | Topic: Vocabulary, sentence correction and usage]
Q.013. In each of the following question, four alternative sentences are given. Choose the CORRECT one and fill the Circle corresponding to that letter in the MCQ Response Form
A. We will discuss your problem as soon as the committee will leave.
B. We will discuss your problem as soon as the committee left.
C. We will discuss your problem as soon as the committee may leave.
D. We will discuss your problem as soon as the committee leaves.

[English | Unit: Formal and Lexical Skills | Topic: Vocabulary, sentence correction and usage]
Q.014. In each of the following question, four alternative sentences are given. Choose the CORRECT one and fill the Circle corresponding to that letter in the MCQ Response Form.
A. Masood told me that he would hire more salesmen if he is in my position.
B. Masood told me that he would hire more salesmen if he has been in my position.
C. Masood told me that he would hire more salesmen if he has my position.
D. Masood told me that he would hire more salesmen if he had been in my position.

[English | Unit: Formal and Lexical Skills | Topic: Vocabulary, sentence correction and usage]
Q.015. In each of the following questions, four alternative sentences are given. Choose the CORRECT one and fill in the Circle corresponding to that letter in the MCQ Response Form.
A. They felt bad while leaving their friends.
B. They felt very badly about leaving their friends.
C. They felt badly about leaving their friends.
D. They felt badly while teaving their friends.

[English | Unit: Formal and Lexical Skills | Topic: Vocabulary, sentence correction and usage]
Q.016. In each of the following question, four alternative meanings of a word are given. You have to select the NEAREST CORRECT MEANING of the given word and fill the appropriate Circle on the MCQ Response Form.AGHAST
A. Critical
B. Reluctant
C. Happy
D. Horrified

[English | Unit: Formal and Lexical Skills | Topic: Vocabulary, sentence correction and usage]
Q.017. In each of the following question, four alternative meanings of a word are given. You have to select the NEAREST CORRECT MEANING of the given word and fill the appropriate Circle on the MCQ Response Form.INVIDIOUS
A. Unbreakable
B. Interesting
C. Unpleasant
D. Fair

[English | Unit: Formal and Lexical Skills | Topic: Vocabulary, sentence correction and usage]
Q.018. In each of the following question, four alternative meanings of a word are given. You have to select the NEAREST CORRECT MEANING of the given word and fill the appropriate Circle on the MCQ Response Form.IMPROMPTU
A. Arriving at the right time
B. Showing signs of being good
C. Done without preparation
D. Wretched

[English | Unit: Formal and Lexical Skills | Topic: Vocabulary, sentence correction and usage]
Q.019. In each of the following question, four alternative meanings of a word are given. You have to select the NEAREST CORRECT MEANING of the given word and fill the appropriate Circle on the MCQ Response Form.DISCERNMENT
A. A system of controfling a country
B. The ability to show good judgement
C. The act of encouraging somebody
D. The ability to show no concern

[English | Unit: Formal and Lexical Skills | Topic: Vocabulary, sentence correction and usage]
Q.020. In each of the following question, four alternative meanings of a word are given. You have to select the NEAREST CORRECT MEANING of the given word and fill the appropriate Circle on the MCQ Response Form.NEOLOGISM
A. A new word
B. Pleasant remark
C. Brief summary
D. Archaic expression

[English | Unit: Formal and Lexical Skills | Topic: Vocabulary, sentence correction and usage]
Q.021. In each of the following question, four alternative meanings of a word are given. You have to select the nearest correct meaning of the given word and fill the appropriate circle on the mcq Response Form.Perish
A. Furious
B. Come to death
C. Secret
D. Frustrated

[English | Unit: Formal and Lexical Skills | Topic: Vocabulary, sentence correction and usage]
Q.022. Select the nearest correct meaning of the word given.BOURGEOIS
A. Belonging to the bureaucratic class
B. Belonging to the middle class
C. Belonging to the upper class
D. Belonging to the lower class

[English | Unit: Formal and Lexical Skills | Topic: Vocabulary, sentence correction and usage]
Q.023. In each of the following question, four alternative meanings of a word are given. You have to select the NEAREST CORRECT MEANING of the given word and fill the appropriate Circle on the MCQ Response Form.RUMINATE
A. Eat greedily
B. Think deeply
C. Work lazily
D. Run fast

[English | Unit: Formal and Lexical Skills | Topic: Vocabulary, sentence correction and usage]
Q.024. In each of the following question, four alternative meanings of a word are given. You have to select the NEAREST CORRECT MEANING of the given word and fill the appropriate Circle on the MCQ Response Form.EMBELLISH
A. Beautify
B. Nominate
C. Finish
D. Weaken

[English | Unit: Formal and Lexical Skills | Topic: Vocabulary, sentence correction and usage]
Q.025. In each of the following question, four alternative meanings of a word are given. You have to select the NEAREST CORRECT MEANING of the given word and fill the appropriate Circle on the MCQ Response Form.PARABLE
A. Impossible
B. Sociable
C. Allegory
D. Suitable

[Biology | Unit: Biological Molecules | Topic: Carbohydrates, proteins, lipids and nucleic acids]
Q.026. If DNA strand is GCTATGG, then mRNA strand synthesized from it would be:
A. CGAUACC
B. CGTATGC
C. CGATACC
D. CGUTCC

[Biology | Unit: Coordination and Control | Topic: Nervous system and receptors]
Q.027. Which one of the following conditions best describes active membrane potential:
A. Depolarization with influx of sodium ions
B. Hyperpolarization with efflux of potassium ions
C. Resting state with high potassium inside
D. Influx of chloride ions

[Biology | Unit: Immunity | Topic: Immune response and vaccination]
Q.028. Tissue rejection is executed by:
A. Both B and T lymphocytes
B. Monocytes
C. B-lymphocytes
D. T-lymphocytes

[Biology | Unit: Circulation | Topic: Heart, blood and vessels]
Q.029. Which of the following statement best describes the function of sinoatrial node?
A. It sends out electrical impulses to ventrictes to contract.
B. It is present at upper end of the left atrium
C. It consists of small number of diffusely oriented cardiac fibers
D. It sends out electrical impulses to atrial muscles causing both atria to contract.

[Biology | Unit: Homeostasis | Topic: Kidney and osmoregulation]
Q.030. A central cavity of the kidney where urine is collected after filtration is known as:
A. Ureter
B. Urethra
C. Pelvis
D. Urinary Bladder

[Biology | Unit: Homeostasis | Topic: Kidney and osmoregulation]
Q.031. Aldosterone plays role in:
A. Transport of water
B. Uptake of sodium in loop of Henle
C. Transport of K* ions into kidney
D. Reabsorption of water

[Biology | Unit: Homeostasis | Topic: Kidney and osmoregulation]
Q.032. Technique used for non-surgical removal of kidney stone is called:
A. Ultrasound
B. Dialysis
C. Lithotripsy
D. X-ray

[Biology | Unit: Support and Movement | Topic: Skeleton, muscles and joints]
Q.033. Microcephaly, the small sized skull is due to:
A. Nutritional Cause
B. Hormonal Causes
C. Skeleton Damage
D. Genetic Defect

[Biology | Unit: Support and Movement | Topic: Skeleton, muscles and joints]
Q.034. The joints that allow movements in several directions are:
A. Hinge Joints
B. Fibrous Joints
C. Ball and Socket Joints
D. Cartilaginous Joints

[Biology | Unit: Support and Movement | Topic: Skeleton, muscles and joints]
Q.035. The collagen fibers of bone are hardened by deposit of:
A. Calcium phosphate
B. Calcium carbonate
C. Calcium oxalate
D. Calcium bicarbonate

[Biology | Unit: Coordination and Control | Topic: Nervous system and receptors]
Q.036. Which of the following neurotransmitters lies outside the central nervous system?
A. Serotonin
B. Acetylcholine
C. Dopamine
D. Adrenaline

[Biology | Unit: Coordination and Control | Topic: Nervous system and receptors]
Q.037. Which hormonal pair shares a common hypothalamic releasing factor?
A. STH and LH
B. FSH and STH
C. ACTH and LH
D. FSH and LH

[Biology | Unit: Reproduction | Topic: Human reproduction and menstrual cycle]
Q.038. Which of the following will happen if fertilization does not occur?
A. Menopause starts
B. FSH secretion is increased
C. Corpus luteum degenerates
D. Progesterone secretion is increased

[Biology | Unit: Acellular Life | Topic: Viruses and HIV/AIDS]
Q.039. Newborn infant may acquire serious eye infections, if his/her mother has:
A. Genital herpes
B. Gonorrhea
C. AIDS
D. Syphilis

[Biology | Unit: Reproduction | Topic: Human reproduction and menstrual cycle]
Q.040. At the cephalic end of primitive streak, closely packed cells form a loci thickening known as:
A. Hensen's Node
B. Primitive Ridge
C. Gastrocoel
D. Primitive Gut

[Biology | Unit: Coordination and Control | Topic: Nervous system and receptors]
Q.041. In plants, the red light favours:
A. Enhancement of cell differentiation
B. Maturation of the cells
C. Elongation of cells
D. Enhancement of cell division

[Biology | Unit: Biological Molecules | Topic: Carbohydrates, proteins, lipids and nucleic acids]
Q.042. The reaction between the phosphate group of one nucleotide and hydroxyl group of another is a synthesis in DNA molecule.
A. Dehydration
B. Oxidation
C. Rehydration
D. Reduction

[Biology | Unit: Biological Molecules | Topic: Carbohydrates, proteins, lipids and nucleic acids]
Q.043. Enzyme which attaches the Okazaki fragments in lagging strand is called:
A. Restriction endonuclease
B. DNA helicase
C. Primase
D. DNA ligase

[Biology | Unit: Enzymes | Topic: Enzymes and inhibition]
Q.044. In phenylketonuria, phenylalanine is not degraded because of defective enzyme:
A. Phenylalanine hydroxylase
B. Phenylalanine oxidase
C. Phenylalanine phosphate
D. None of these

[Biology | Unit: Cell Structure and Function | Topic: Cells, organelles and chromosomes]
Q.045. Males with XXY chromosomes suffer from:
A. Klinefelter’s Syndrome
B. Down's Syndrome
C. Jacob's Syndrome
D. Edward’s Syndrome

[Biology | Unit: Cell Structure and Function | Topic: Cells, organelles and chromosomes]
Q.046. Internal program of events and sequences of morphological changes by which cell commit a suicide is collectively called:
A. Necrosis
B. Metastasis
C. Epistasis
D. Apoptosis

[Biology | Unit: Cell Structure and Function | Topic: Cells, organelles and chromosomes]
Q.047. Phragmoplast is formed from vesicle which originates from:
A. Smooth Endoplasmic Reticulum
B. Ribosome
C. Golgi Complex
D. Rough Endoplasmic Reticulum

[Biology | Unit: Inheritance | Topic: Mendelian and sex-linked inheritance]
Q.048. When phenotype of a heterozygote is in between the phenotypes of both the homozygous parents, it is called:
A. Incomplete dominance
B. Pleiotropy
C. Epistasis
D. Codominance

[Biology | Unit: Circulation | Topic: Heart, blood and vessels]
Q.049. Which one is correct about blood?
A. Will produce anti-Rh antibodies if given Rh* blood
B. Rh* antigens are present on RBCs
C. Cannot produce anti-Rh antibodies in any case
D. Rh* antibodies are present in blood

[Biology | Unit: Biotechnology | Topic: Genetic engineering and applications]
Q.050. Temperature-insensitive (thermostable) enzyme used in PCR is:
A. DNA polymerase I
B. DNA ligase
C. DNA polymerase ITI
D. Taq polymerase

[Biology | Unit: Biotechnology | Topic: Genetic engineering and applications]
Q.051. Cloning is a form of:
A. Parthenogenesis
B. Apomixis
C. Sexual Reproduction
D. Asexual Reproduction

[Biology | Unit: Biotechnology | Topic: Genetic engineering and applications]
Q.052. Antigens to treat Non-Hodgkin’s lymphoma are produced by:
A. Wheat Plant
B. Tobacco Plant
C. Rice Plant
D. Corn Plant

[Biology | Unit: Evolution | Topic: Evolution and natural selection]
Q.053. The survival of an organism during the struggle for existence is not random, but depends on:
A. Its genetic constitution
B. Its ability to over-produce
C. Its ability to acquire characters
D. Its ability to over-eat

[Biology | Unit: Evolution | Topic: Evolution and natural selection]
Q.054. Evolutionary relationships amongst species are reflected in their:
A. DNA and proteins
B. DNA and gene
C. RNAs and proteins
D. DNA and RNAs

[Biology | Unit: Inheritance | Topic: Mendelian and sex-linked inheritance]
Q.055. If all the members of a population are homozygous for the same allele, that allele is said to be:
A. Random in population’s pool
B. Random in a species
C. Fixed in population's pool
D. Fixed in the gene pool

[Biology | Unit: Acellular Life | Topic: Viruses and HIV/AIDS]
Q.056. Diseases in living organisms which are caused by parasites are called:
A. Disinfestations
B. Infections
C. Antisepsis
D. Infestations

[Biology | Unit: Bioenergetics | Topic: Cellular respiration and photosynthesis]
Q.057. The nutrient cycles are also called:
A. Biogeochemical cycles
B. Bioelement cycles
C. Biochemical cycles
D. Geochemical cycles

[Biology | Unit: Bioenergetics | Topic: Cellular respiration and photosynthesis]
Q.058. The productivity of aquatic ecosystem is determined by:
A. Water
B. Light
C. Light and nutrients
D. Nutrients

[Biology | Unit: Bioenergetics | Topic: Cellular respiration and photosynthesis]
Q.059. What is the drawback of nuclear energy?
A. It causes radiation pollution
B. It is very expensive
C. It is not long lasting
D. It pollutes the air

[Biology | Unit: Circulation | Topic: Heart, blood and vessels]
Q.060. Arteriosclerosis is:
A. A metabolic disorder
B. A degenerative disorder
C. An infectious disorder
D. A genetic disorder

[Biology | Unit: Acellular Life | Topic: Viruses and HIV/AIDS]
Q.061. Antibiotics act against:
A. Bacterial diseases
B. Allergies
C. Viral Diseases
D. Bacterial and Viral Diseases

[Biology | Unit: Bioenergetics | Topic: Cellular respiration and photosynthesis]
Q.062. The immediate source of energy for cellular metabolism is
A. Lipids
B. Carbohydrates
C. ATP
D. Proteins

[Biology | Unit: Biological Molecules | Topic: Carbohydrates, proteins, lipids and nucleic acids]
Q.063. Haemoglobin exhibits:
A. Secondary Structure
B. Quaternary Structure
C. Primary Structure
D. Tertiary Structure

[Biology | Unit: Enzymes | Topic: Enzymes and inhibition]
Q.064. Pepsin enzyme is produced in an inactive form and is activated in situation when it is required because:
A. Not produced in complete form
B. It does not work efficiently at that time
C. Quite capable of destroying cells internal structure
D. None of the above

[Biology | Unit: Enzymes | Topic: Enzymes and inhibition]
Q.065. Enzyme, after catalysis, detaches itself from the product:
A. Completely
B. Changed
C. Incompletely
D. Unchanged

[Biology | Unit: Cell Structure and Function | Topic: Cells, organelles and chromosomes]
Q.066. A group of ribosomes attached to messenger RNA is known as:
A. Ribosome
B. Nucleosome
C. Lysosome
D. Polysome

[Biology | Unit: Cell Structure and Function | Topic: Cells, organelles and chromosomes]
Q.067. Detoxification of harmful drugs within the cell is done by:
A. Nucleolus
B. Smooth surface endoplasmic reticulum
C. Ribosomes
D. Food vacuoles

[Biology | Unit: Enzymes | Topic: Enzymes and inhibition]
Q.068. Tay-Sach's disease is due to the presence of an enzyme that is inverted in the catabolism of:
A. Proteins
B. Ascorbic Acid
C. Carbohydrates.
D. Lipids

[Biology | Unit: Inheritance | Topic: Mendelian and sex-linked inheritance]
Q.069. What is true about pattern baldness?
A. It is autosomal recessive disease in males
B. It is X-linked disease
C. It is autosomal dominant disease in males
D. It is Y-linked disease

[Biology | Unit: Immunity | Topic: Immune response and vaccination]
Q.070. Symptoms of Herpes Simplex is:
A. Abdominal Pain
B. Vesicular lesions in the epithelial layer
C. Fever
D. Failure of immune system

[Biology | Unit: Acellular Life | Topic: Viruses and HIV/AIDS]
Q.071. The major cell infected by HIV is
A. Leukocyte
B. Monocyte
C. Helper T-lymphocyte
D. B-lymphocyte

[Biology | Unit: Biotechnology | Topic: Genetic engineering and applications]
Q.072. ._ are used as important vectors in genetic engineering.
A. Ribosomes
B. Plasmids
C. Nucleoids
D. Mesosomes

[Biology | Unit: Acellular Life | Topic: Viruses and HIV/AIDS]
Q.073. Which of the following is aerobic bacterium?
A. Spirochete
B. E. coli
C. Cyanobacteria
D. Pseudomonas

[Biology | Unit: Cell Structure and Function | Topic: Cells, organelles and chromosomes]
Q.074. The giant amoebas inhabit mud at the bottom of freshwater ponds and obtain energy from:
A. Microscopic bacteria
B. Anaerobic bacteria
C. Aerobic bacteria
D. Methanogenic bacteria

[Biology | Unit: Acellular Life | Topic: Viruses and HIV/AIDS]
Q.075. A large group of parasitic protozoa, some of which causes various diseases such as malaria to humans, are:
A. Apicomplexans
B. Annelida
C. Platyhelminthes
D. Arthropods

[Biology | Unit: Biological Molecules | Topic: Carbohydrates, proteins, lipids and nucleic acids]
Q.076. Penicillin is obtained from:
A. Penicillium notatum
B. Aspergillus fumigatus
C. Aspergillus flavus
D. Penicillium chrysogenum

[Biology | Unit: Biological Molecules | Topic: Carbohydrates, proteins, lipids and nucleic acids]
Q.077. Which of the following components is less resistant to decay?
A. Lignin
B. Starch
C. Chitin
D. Cellulose

[Biology | Unit: Bioenergetics | Topic: Cellular respiration and photosynthesis]
Q.078. _ are bioindicators of air pollution.
A. Cyanobacteria
B. Mycorrhizae
C. Fungi
D. Lichens

[Biology | Unit: Reproduction | Topic: Human reproduction and menstrual cycle]
Q.079. The gymnosperms are called ‘Naked Seeded’ plants because they bear naked:
A. Antheridia
B. Ovules
C. Fruits
D. Archegonia

[Biology | Unit: Reproduction | Topic: Human reproduction and menstrual cycle]
Q.080. The integumented indehiscent megasporangium is called:
A. Seed
B. Archegonium
C. Megagametophyte
D. Ovule

[Biology | Unit: Biological Molecules | Topic: Carbohydrates, proteins, lipids and nucleic acids]
Q.081. Pulses are present in the family:
A. Caesalpiniaceae
B. Fabaceae
C. Gramineae
D. Mimosaceae

[Biology | Unit: Digestion | Topic: Human digestive system]
Q.082. It is an endoparasite of humans, cattle and pig that completes its life cycle in two hosts:
A. Stingray
B. Liver fluke (Fasciola)
C. Aurelia
D. Schistosoma

[Biology | Unit: Acellular Life | Topic: Viruses and HIV/AIDS]
Q.083. Tse-tse fly causes the sleeping sickness and skin diseases by transmitting:
A. Plasmodium
B. Trypanosoma
C. Anopheles
D. Insects

[Biology | Unit: Support and Movement | Topic: Skeleton, muscles and joints]
Q.084. Coelom is a cavity lined by:
A. Mesoderm
B. Epiderm
C. Endoderm
D. Ectoderm

[Biology | Unit: Bioenergetics | Topic: Cellular respiration and photosynthesis]
Q.085. Which of the following molecules is reduced by accepting hydrogen in the Calvin cycle?
A. 1,3-Bisphosphoglycerate
B. Ribulose-1,5-bisphosphate
C. 3-phosphoglycerate
D. Glyceraldehyde-3-phosphate

[Biology | Unit: Bioenergetics | Topic: Cellular respiration and photosynthesis]
Q.086. The molecule formed after first phosphorylation during glycolysis is:
A. Fructose-6-phosphate
B. Glucose-1-phosphate
C. Fructose-1, 6-bisphosphate
D. Glucose-6-phosphate

[Biology | Unit: Bioenergetics | Topic: Cellular respiration and photosynthesis]
Q.087. Krebs Cycle in mitochondria takes place in:
A. Cytosol
B. Matrix
C. Outer Membrane
D. Inner Membrane

[Biology | Unit: Circulation | Topic: Heart, blood and vessels]
Q.088. At the junction between esophagus and the stomach there is a special ring of muscles called:
A. Cardiac Sphincter
B. Esophageal Sphincter
C. Ileocolic Sphincter
D. Pyloric Sphincter

[Biology | Unit: Coordination and Control | Topic: Nervous system and receptors]
Q.089. Hepatic and pancreatic secretions are also stimulated by a hormone called:
A. Gastrin
B. Secretin
C. HCl
D. Enterokinase

[Biology | Unit: Digestion | Topic: Human digestive system]
Q.090. Like pepsin, trypsin is also secreted as inactive trypsinogen, which is activated by:
A. Enterokinase
B. Chyme
C. Lipase
D. Erypsin

[Biology | Unit: Cell Structure and Function | Topic: Cells, organelles and chromosomes]
Q.091. During photorespiration, the glycolate is converted into glycine in a structure of ceil called:
A. Golgi Bodies
B. Mitochondria
C. Glyoxysome
D. Peroxisome

[Biology | Unit: Circulation | Topic: Heart, blood and vessels]
Q.092. The respiratory pigment, which has much higher affinity to combine with oxygen, is:
A. Myoglobin
B. Haemoglobin
C. Globin
D. Hemocyanin

[Biology | Unit: Biological Molecules | Topic: Carbohydrates, proteins, lipids and nucleic acids]
Q.093. Most of the carbon dioxide is carried in the blood in the form of
A. Bicarbonate
B. COz
C. Carboxyhemoglobin
D. Blood plasma protein

[Biology | Unit: Immunity | Topic: Immune response and vaccination]
Q.094. Antibiotics are actually:
A. Globular proteins
B. Fibrous proteins
C. Glycoproteins
D. Glycolipids

[Biology | Unit: Circulation | Topic: Heart, blood and vessels]
Q.095. Heparin prevents blood clots and is released by:
A. Eosinophils
B. Neutrophils
C. Monocytes
D. Basophils

[Chemistry | Unit: Thermochemistry and Energetics | Topic: Heat, enthalpy and thermodynamics]
Q.096. Which of the following is an exothermic reaction?
A. H+(aq) + OH−(aq) -> H2O(l)
B. 1/2 H2(g) -> H(g)
C. Na(g) -> Na+(g) + 1e−
D. 1/2 Cl2(g) -> Cl(g)

[Chemistry | Unit: Reaction Kinetics | Topic: Rate and activation energy]
Q.097. The rate equation determined experimentally for this reaction: (CH3)3―C―Br + H2O → (CH3)3―C―OH + HBr, is Rate = k[(CH3)3CBr] Hence it is which of the follwing?
A. Fractional Order
B. Pseudo First Order
C. First Order
D. Second Order

[Chemistry | Unit: Chemical Equilibrium | Topic: Equilibrium and buffers]
Q.098. Equilibrium constant Kc for H2O ----> H+ + OH− can be written as follows:
A. [H+][OH-]/[H2O]
B. [H2O]/[H+][OH-]
C. [H+][OH-]
D. [H+]2[OH-]

[Chemistry | Unit: Carboxylic Acids | Topic: Carboxylic acids and derivatives]
Q.099. The protonation of carboxylic acid is:
A. Addition of H+ to carbonyl oxygen
B. Addition of H+ to OH group
C. Removal of H+
D. Formation of salt

[Chemistry | Unit: Introduction to Chemistry | Topic: Stoichiometry and mole concept]
Q.100. Each molecule of haemoglobin is made up of nearly:
A. 11000 atoms
B. 10000 atoms
C. 6600 atoms
D. 6800 atoms

[Chemistry | Unit: Introduction to Chemistry | Topic: Stoichiometry and mole concept]
Q.101. A limiting reactant is the one which:
A. Is mostly a cheaper substance and taken in larger quantity
B. Is consumed earlier and controls the amount of product formed in a chemical reaction
C. Gives greatest number of moles of products
D. Is left behind after the completion of reaction

[Chemistry | Unit: Atomic Structure | Topic: Atomic models and electronic configuration]
Q.102. During isotopic analysis, the pressure of the vapours of the ions maintained in the ionization chamber of mass spectrometer Is:
A. Around 10-7 torr
B. 1 torr
C. Around 10-3 torr
D. 10-7 torr

[Chemistry | Unit: Carboxylic Acids | Topic: Carboxylic acids and derivatives]
Q.103. The acid which can be purified by the sublimation is:
A. Acetic Acid
B. Oxalic Acid
C. Benzoic Acid
D. Citric Acid

[Chemistry | Unit: Introduction to Chemistry | Topic: Stoichiometry and mole concept]
Q.104. Paper chromatography is used for:
A. Elemental Analysis
B. Qualitative Analysis
C. Industrial Purification
D. Structural Analysis

[Chemistry | Unit: Gases | Topic: Gas laws and kinetic molecular theory]
Q.105. In the process of respiration, there is application of:
A. Dalton’s Law
B. Charles’s Law
C. Boyle’s Law
D. Graham’s Law

[Chemistry | Unit: Chemistry of Hydrocarbons | Topic: Alkanes, alkenes, alkynes and benzene]
Q.106. The formula of acrylonitrile is:
A. CH2=CH―CN
B. CH3―CH2―CH2―CN
C. CH3―CH2―CN
D. CH3―CN

[Chemistry | Unit: Chemistry of Hydrocarbons | Topic: Alkanes, alkenes, alkynes and benzene]
Q.107. During nitration of benzene, the active nitrating agent is:
A. NO2-
B. HNO2
C. NO3-
D. NO2+

[Chemistry | Unit: Chemistry of Hydrocarbons | Topic: Alkanes, alkenes, alkynes and benzene]
Q.108. Which compound is the most reactive one?
A. Ethyne
B. Ethane
C. Benzene
D. Ethene

[Chemistry | Unit: Alcohols and Phenols | Topic: Alcohol and phenol reactions]
Q.109. Grignard reagents are prepared by the reaction of magnesium metal with alkyl halides in the presence of:
A. Dry Ether
B. Alcohol
C. CS2
D. CCl4

[Chemistry | Unit: Chemistry of Hydrocarbons | Topic: Alkanes, alkenes, alkynes and benzene]
Q.110. When n-butyl magnesium iodide is treated with water, the product is:
A. n-butane
B. Propane
C. Iso-butane
D. Alcohol

[Physics | Unit: Nuclear Physics | Topic: Radioactivity and nuclear decay]
Q.111. Two radioactive elements X and Y have half-lives of 25 minutes and 75 minutes respectively. Sample of X and Y initially contain equal number of atoms. After 150 minutes, what is the value of the following fraction?No. of nuclei of X unchanged/No. of nuclei of Y unchanged
A. 1: 16
B. 16: 1
C. 1: 8
D. 8: 1

[Chemistry | Unit: Chemistry of Hydrocarbons | Topic: Alkanes, alkenes, alkynes and benzene]
Q.112. Phenol reacts with concentrated H2SO4 to give:
A. Ortho hydroxy benzene sulphonic acid
B. Meta hydroxy benzene sulphonic acid
C. Ortho and para hydroxy benzene sulphonic acid
D. Para hydroxy benzene sulphonic acid

[Chemistry | Unit: Alcohols and Phenols | Topic: Alcohol and phenol reactions]
Q.113. Phenol can be distinguished from alcohol by adding:
A. Br2/H2O
B. FeSO4
C. Cl2/H2O
D. FeCl3

[Chemistry | Unit: Reaction Kinetics | Topic: Rate and activation energy]
Q.114. In the conversion of ethylene into acetaldehyde, cupric chloride acts as:
A. Initiator
B. Promoter
C. Catalyst
D. Reactant

[Chemistry | Unit: Carboxylic Acids | Topic: Carboxylic acids and derivatives]
Q.115. When acetone is heated in the presence of K2Cr2O7/H2SO4, the products formed are:
A. Maleic Acid and Fumaric Acid
B. Acetic Acid and Formic Acid
C. Formic Acid and Oxalic Acid
D. Oxalic Acid and Acetic Acid

[Chemistry | Unit: Carboxylic Acids | Topic: Carboxylic acids and derivatives]
Q.116. Which acid is used in the manufacture of plastics?
A. Carbolic Acid
B. Acetic Acid
C. Carbonic Acid
D. Oxalic Acid

[Chemistry | Unit: Aldehydes and Ketones | Topic: Carbonyl compounds]
Q.117. Which of the following compounds will react with Tollen’s Reagent?
A. Formic acid
B. Acetone
C. Acetaldehyde
D. Butanone

[Chemistry | Unit: Macromolecules | Topic: Polymers and biomolecules]
Q.118. In conjugated protein molecules, the protein is attached or conjugated to some non-protein group which are called:
A. Prosthetic Group
B. Hydrogen Bonding
C. Aldehyde Group
D. Peptide Linkage

[Chemistry | Unit: Industrial Chemistry | Topic: Industrial processes and materials]
Q.119. Micronutrients are required in quantity ranging from:
A. 6 — 200 g per acre
B. 4-40 g per acre
C. 6 — 200 kg per acre
D. 4 - 40 kg per acre

[Chemistry | Unit: Industrial Chemistry | Topic: Industrial processes and materials]
Q.120. Potassium fertilizers are especially useful for:
A. Mango
B. Tobacco
C. Wheat
D. Rice

[Chemistry | Unit: Industrial Chemistry | Topic: Industrial processes and materials]
Q.121. The yellowish colour of photochemical smog is due to the presence of:
A. Nitrogen dioxide
B. Dinitrogen trioxide
C. Nitrous oxide
D. Nitric oxide

[Chemistry | Unit: Industrial Chemistry | Topic: Industrial processes and materials]
Q.122. The incarnation process can reduce the volume of the water by:
A. One half
B. Not affected
C. One third
D. Two third

[Chemistry | Unit: Liquids and Solids | Topic: Intermolecular forces and states of matter]
Q.123. _ % of the known universe is in the plasma state.
A. 30
B. 99
C. 50
D. 80

[Chemistry | Unit: Gases | Topic: Gas laws and kinetic molecular theory]
Q.124. Absolute zero is unattainable. Current attempts have resulted in temperature as low as:
A. 10-4 K
B. 10-2 K
C. 10-1 K
D. 10-5 K

[Chemistry | Unit: Chemical Bonding | Topic: Bonding and molecular shape]
Q.125. Electron gas theory was proposed to explain the bonding in solids:
A. Molecular
B. Ionic
C. Covalent
D. Metallic

[Chemistry | Unit: Macromolecules | Topic: Polymers and biomolecules]
Q.126. In proteins, there are on the average _ amino acid units for each turn in helix:
A. 25
B. 27
C. 21
D. 23

[Chemistry | Unit: Atomic Structure | Topic: Atomic models and electronic configuration]
Q.127. In atomic particles:
A. Mass of neutron is almost equal to mass of electron
B. e/m of a proton is almost equal to e/m of electron
C. Mass of proton is almost equal to mass of electron
D. Charge of proton is almost equal to charge of electron

[Chemistry | Unit: Atomic Structure | Topic: Atomic models and electronic configuration]
Q.128. The extent of bonding of a light ray after passing through prism depends upon:
A. Wavelength of photons
B. Wave number of photons
C. Energy of photons
D. Frequency of photons

[Chemistry | Unit: Atomic Structure | Topic: Atomic models and electronic configuration]
Q.129. Splitting of spectral lines in closely spaced lines in presence of magnetic field is called:
A. Stark Effect
B. Zeeman Effect
C. Photoelectric Effect
D. Compton Effect

[Chemistry | Unit: Chemical Bonding | Topic: Bonding and molecular shape]
Q.130. A bond is not formed:
A. When both attractive and repulsive forces are balanced
B. When attractive forces overcome repulsive forces
C. When repulsive forces are negligible
D. When repulsive forces exceed attractive forces

[Chemistry | Unit: Chemical Bonding | Topic: Bonding and molecular shape]
Q.131. If the electronegativity difference between bonded atoms is zero, the bond between the two atoms is:
A. Polar
B. Partially Ionic
C. Non-polar
D. Both B and C

[Chemistry | Unit: Chemical Bonding | Topic: Bonding and molecular shape]
Q.132. VSEPR theory helps in explaining:
A. Attraction between atoms
B. Size of molecule
C. Nature of bond
D. Shape of molecule

[Chemistry | Unit: Thermochemistry and Energetics | Topic: Heat, enthalpy and thermodynamics]
Q.133. Which of the following formations is an endothermic reaction?
A. C(g) + O2(g) → CO2(g)
B. N2(g) + 3H2(g) → 2NH3(g)
C. 2H2O(l) → 2H2(g) + O2(g)
D. None of the above

[Chemistry | Unit: Chemical Equilibrium | Topic: Equilibrium and buffers]
Q.134. Solubility of KCIO; can be decreased in H2O by:
A. Removing K+ ions from the solution
B. Removing ClO3- ions from the solution
C. Adding KCl from outside
D. Adding NaNO3 from outside

[Chemistry | Unit: Introduction to Chemistry | Topic: Stoichiometry and mole concept]
Q.135. 36 g of HCl dissolves in 100 g of solution. The density of HCl is 1.19 gcm-3. The molar mass of the HCl solution will be:
A. 36.5 g/mol
B. 38.0 g/mol
C. 100 g/mol
D. 11.73 g/mol

[Chemistry | Unit: Thermochemistry and Energetics | Topic: Heat, enthalpy and thermodynamics]
Q.136. The heat of hydration decreases with the increase in:
A. Number of neutrons
B. Size of cations
C. Size of atomic radii
D. Number of electrons

[Chemistry | Unit: Electrochemistry | Topic: Redox and electrochemical cells]
Q.137. Stronger the oxidizing agent, greater is the:
A. Redox Potential
B. Oxidation Potential
C. EMF of the cell
D. Reduction Potential

[Chemistry | Unit: Electrochemistry | Topic: Redox and electrochemical cells]
Q.138. The emf produced by Galvanic Cell is known as:
A. Redox Potential
B. Cell Potential
C. Oxidation Potential
D. None of the above

[Chemistry | Unit: Electrochemistry | Topic: Redox and electrochemical cells]
Q.139. In nickel-cadmium battery, the cathode is composed of:
A. Cd
B. Ni(OH)2
C. Ni
D. NiO2

[Chemistry | Unit: Macromolecules | Topic: Polymers and biomolecules]
Q.140. Concentrated sugar solution undergoes hydrolysis into glucose and fructose by enzyme called:
A. Zymase
B. Invertase
C. Cellulose
D. Urease

[Chemistry | Unit: S- and P-Block Elements | Topic: Periodic trends and main-group chemistry]
Q.141. In Modern Periodic Table, the elements in Group II-B are:
A. Zn, Cd, Pb
B. Zn, Cd, Hg
C. Zn, Cd, Ba
D. Zn, Cd, Bi

[Chemistry | Unit: S- and P-Block Elements | Topic: Periodic trends and main-group chemistry]
Q.142. Hydrogen loses an electron to form:
A. H+
B. H2−2
C. H
D. H−

[Chemistry | Unit: S- and P-Block Elements | Topic: Periodic trends and main-group chemistry]
Q.143. Which metal occurs as skeletal material in egg shells?
A. Calcium
B. Barium
C. Beryllium
D. Strontium

[Chemistry | Unit: S- and P-Block Elements | Topic: Periodic trends and main-group chemistry]
Q.144. At which condition are hydrides of alkaline earth metals formed:
A. At high pressure
B. At room temperature
C. At high temperature
D. None of the above

[Chemistry | Unit: S- and P-Block Elements | Topic: Periodic trends and main-group chemistry]
Q.145. Which metal carbide is formed readily by the direct reaction?
A. Rubidium
B. Potassium
C. Sodium
D. Lithium

[Chemistry | Unit: S- and P-Block Elements | Topic: Periodic trends and main-group chemistry]
Q.146. Asbestos is hydrated _ magnesium silicate.
A. Calcium
B. Aluminium
C. Barium
D. Iron

[Chemistry | Unit: S- and P-Block Elements | Topic: Periodic trends and main-group chemistry]
Q.147. Formula of lead suboxide is:
A. Pb2O3
B. Pb2O
C. PbO
D. Pb3O4

[Chemistry | Unit: Electrochemistry | Topic: Redox and electrochemical cells]
Q.148. Phosphine can be produced by _ of phosphorous acid.
A. Hydration
B. Hydrolysis
C. Oxidation
D. Reduction

[Chemistry | Unit: S- and P-Block Elements | Topic: Periodic trends and main-group chemistry]
Q.149. Which Noble Gas is used in bacterial lamps?
A. Xenon
B. Radon
C. Argon
D. Krypton

[Chemistry | Unit: Electrochemistry | Topic: Redox and electrochemical cells]
Q.150. The most durable metal plating on iron to protect against corrosion is:
A. Tin plating
B. Zinc plating
C. Nickel plating
D. Copper plating

[Chemistry | Unit: Atomic Structure | Topic: Atomic models and electronic configuration]
Q.151. Colour of the transition metal ions/compounds is due to the electrons present in:
A. d-orbital
B. s-orbital
C. p-orbital
D. None of the above

[Chemistry | Unit: S- and P-Block Elements | Topic: Periodic trends and main-group chemistry]
Q.152. Chromyl Test is performed to confirm:
A. Cl− ions
B. SO4−2 ions
C. PO4−3 ions
D. Cr+3 ions

[Chemistry | Unit: Chemical Bonding | Topic: Bonding and molecular shape]
Q.153. Linear shape is associated with a set of hybrid orbitals?
A. sp2
B. sp3
C. dsp2
D. sp

[Chemistry | Unit: Fundamental Principles of Organic Chemistry | Topic: Organic nomenclature and isomerism]
Q.154. Which one of the following compounds show cis-trans isomerism?
A. 1-butene
B. 1-hexene
C. 1-bromo-2-chloropropene
D. Propene

[Chemistry | Unit: Alkyl Halides | Topic: Nucleophilic substitution]
Q.155. CH3―CH2―MgBr + H2O -> Br-Mg-OH + X , Where ‘X’ is:
A. Propane
B. Butane
C. Methane
D. Ethane

[Physics | Unit: Electronics | Topic: Semiconductors and electronic devices]
Q.156. If R1 = 10 kΩ and R2 = 100 kΩ then the gain of op-amplifier as inverting amplifier is:
A. –1
B. 10
C. –10
D. 1

[Physics | Unit: Electronics | Topic: Semiconductors and electronic devices]
Q.157. If inputs A = 1, B = 0 and output X = 1, then it corresponds to the operation of a:
A. AND Gate
B. XNOR Gate
C. NAND Gate
D. NOR Gate

[Physics | Unit: Thermodynamics | Topic: Heat and thermal physics]
Q.158. The value of Stefan’s Boltzmann Constant is:
A. 4.28 x 10-7 Wm-2K-4
B. 4.28 x 10-4 Wm-2K-4
C. 3.62 x 10-4 Wm-2K-4
D. 5.67 x 10-8 Wm-2K-4

[Physics | Unit: Dawn of Modern Physics | Topic: Photon and quantum physics]
Q.159. Einstein’s photoelectric equation is given by:
A. hf - ϕ = ½ mv2
B. E = hc2
C. E = mc2
D. hf = ½ mv2

[Physics | Unit: Dawn of Modern Physics | Topic: Photon and quantum physics]
Q.160. In Compton Effect, the value of h/moc is given by:
A. 1.43 x 10-11 m
B. 2.43 x 10-12 m
C. 2.56 x 10-12 m
D. 3.46 x 10-6 m

[Physics | Unit: Waves | Topic: Waves, sound and SHM]
Q.161. If a particle of mass 5.0 mg moves with the speed of 8.0 m/sec, then the de-Broglle’s wavelength will be:
A. 1.68 x 10-27 m
B. 1.65 x 10-29 m
C. 1.70 x 10-25 m
D. 1.66 x 10-29 m

[Physics | Unit: Waves | Topic: Waves, sound and SHM]
Q.162. LASER is a device which can produce:
A. Intense beam of light
B. Coherent beam of light
C. Intense, Coherent, Monochromatic beam of light
D. Monochromatic beam of light

[Physics | Unit: Waves | Topic: Waves, sound and SHM]
Q.163. A crack allows greater amount of X-rays to pass, which appears on photographic film as:
A. Blurry Area
B. Bright Area
C. Dark Area
D. Red Area

[Physics | Unit: Nuclear Physics | Topic: Radioactivity and nuclear decay]
Q.164. The emission of γ-radiations from the nucleus is generally represented by the equation:
A. A*Z -> AZ + γ
B. AZ -> (A-4)(Z-2) + γ
C. AZ -> A(Z+1) + γ
D. None of these

[Physics | Unit: Dawn of Modern Physics | Topic: Photon and quantum physics]
Q.165. For intermediate energy of radiations, the dormant process is:
A. Compton Effect
B. Photoelectric Effect
C. Nuclear Effect
D. Pair Production

[Physics | Unit: Force and Motion | Topic: Kinematics, Newton laws and momentum]
Q.166. The dimensions of gravitational constant “G” are:
A. [ML-2T-1]
B. [ML-2T-2]
C. [M2L-2T-1]
D. [M-1L3T-2]

[Physics | Unit: Waves | Topic: Waves, sound and SHM]
Q.167. Ultraviolet radiations cause:
A. Severe Crop Damage
B. Decay of Microorganisms
C. Sunburn, Blindness, Skin Cancer
D. All of the above

[Physics | Unit: Vectors and Equilibrium | Topic: Vectors and vector products]
Q.168. Unit vector in the direction of vector 2i - 4j will be:
A. 2i − 4j / √6
B. 4i − 2j / √10
C. i − 2j / √5
D. i − 2j / √7

[Physics | Unit: Vectors and Equilibrium | Topic: Vectors and vector products]
Q.169. If the force of magnitude 8 N acts on a body in direction making an angle 30, its X and Y components will be:
A. Fx = 3√3 Fy = 4
B. Fx = 4√3 Fy = 8
C. Fx = 4√3 Fy = 4
D. Fx = 8 Fy = 4√3

[Physics | Unit: Waves | Topic: Waves, sound and SHM]
Q.170. Two waves of slightly different frequencies and travelling in the same direction lead to:
A. Stationary Waves
B. Beats
C. Interference
D. Both B and C

[Physics | Unit: Waves | Topic: Waves, sound and SHM]
Q.171. What is it that we use to calculate the speeds of distant stars and galaxies?
A. Doppler Effect
B. Beats
C. Interference
D. All of the above

[Physics | Unit: Waves | Topic: Waves, sound and SHM]
Q.172. In Young’s Double Slit Experiment, if the distance between slits and screen is doubled, then fringe spacing becomes:
A. Zero
B. Double the original value
C. One
D. Half of the original value

[Physics | Unit: Waves | Topic: Waves, sound and SHM]
Q.173. In Michelson’s interferometer 792 bright fringes pass across the field of view when its movable mirror is displaced through 0.233 mm using the equation l = m λ / 2 the wavelength of light used is:
A. 588 nm
B. 348 nm
C. 620 nm
D. 400 nm

[Physics | Unit: Waves | Topic: Waves, sound and SHM]
Q.174. In Michelson‘s Experiment, the formula to calculate the speed of light is:
A. c = 2 fd
B. c = 2π f / d
C. c = 16 f / d
D. c = 16 fd

[Physics | Unit: Waves | Topic: Waves, sound and SHM]
Q.175. The information received at the other end of a fibre can be inaccurate due to of the light signal.
A. Longer wavelengths
B. Frequency
C. Intensity
D. Dispersion or Spreading

[Physics | Unit: Fluid Dynamics | Topic: Fluid flow and Bernoulli principle]
Q.176. The pressure on the other sides and everywhere inside the vessel will be according to the:
A. Pascal's Law
B. Hooke's Law
C. Boyle’s Law
D. Charles’s Law

[Physics | Unit: Thermodynamics | Topic: Heat and thermal physics]
Q.177. The value of universal; Gas Constant ‘R’ is:
A. 8.314 Jmol-2K-1
B. 1.38 Jmol-1 K-2
C. 1.38 Jmol-1K-1
D. 8.314 Jmol-1 K-1

[Physics | Unit: Thermodynamics | Topic: Heat and thermal physics]
Q.178. For adiabatic process, the First Law of Thermodynamics is:
A. W = ∆U + Q
B. Q = – W
C. Q = W
D. W = – ∆U

[Physics | Unit: Thermodynamics | Topic: Heat and thermal physics]
Q.179. The entropy of the universe always:
A. Decreases
B. Increases
C. Remains the same
D. Both A and B

[Physics | Unit: Work and Energy | Topic: Work, power and energy]
Q.180. The work done in moving a unit positive charge from one point to another against the electric field is a measure of:
A. Capacitance
B. Potential difference between two points
C. Intensity of electric field
D. Resistance between two points

[Physics | Unit: Fluid Dynamics | Topic: Fluid flow and Bernoulli principle]
Q.181. In Milikan‘s Method, the radius of droplet can be calculated by:
A. r = √qvt / 2ρg
B. r2 = 9ηvt / ρg
C. r2 = 9ηvt / 2ρg
D. r = 9ηvt / 2ρg

[Physics | Unit: Vectors and Equilibrium | Topic: Vectors and vector products]
Q.182. The scalar product of i and k is:
A. Zero
B. 90°
C. 1
D. -1

[Physics | Unit: Force and Motion | Topic: Kinematics, Newton laws and momentum]
Q.183. If the body is rotating with uniform angular velocity, then its torque is:
A. Zero
B. Clockwise
C. Maximum
D. Remains the same

[Physics | Unit: Waves | Topic: Waves, sound and SHM]
Q.184. Speed of light, radio waves and microwaves in vacuum is:
A. 3 x 105 ms-1
B. 3 x 103 ms-1
C. 3 x 106 ms-1
D. 3 x 108 ms-1

[Physics | Unit: Force and Motion | Topic: Kinematics, Newton laws and momentum]
Q.185. A body is moving with an initial velocity of 2 kms-1. After a time of 50 secs its velocity becomes 1.5 kms-1, Its acceleration will be:
A. 30 m/s2
B. 40 m/s2
C. 20 m/s2
D. -10 m/s2

[Physics | Unit: Force and Motion | Topic: Kinematics, Newton laws and momentum]
Q.186. When a car moves with constant acceleration, the velocity-time graph is a:
A. Straight line
B. Parabola
C. Horizontal line
D. Exponential curve

[Physics | Unit: Force and Motion | Topic: Kinematics, Newton laws and momentum]
Q.187. In elastic collision, when a massive body collides with light body at conditions m1 >> m2 and v2 = 0 ms-1, then the change in velocity will be written as:
A. v1’ ≈ −v1 ; v2’ ≈ v1
B. v1’ ≈ v1 ; v2’ ≈ 0
C. v1’ ≈ v1 ; v2’ ≈ 2v1
D. v1’ ≈ −v1 ; v2’ ≈ 0

[Physics | Unit: Work and Energy | Topic: Work, power and energy]
Q.188. If a certain force acts on an object and changes its kinetic energy from 65 J to 130 J, then work done by the force will be:
A. 92.5 J
B. 97.5 J
C. 65 J
D. 130 J

[Physics | Unit: Electromagnetism | Topic: Magnetic fields and force]
Q.189. A bullet train is lifted above the rails due to magnetic effect, thus friction is reduced to minimum and speed can be enhanced up to:
A. 500 Km min-1
B. 500 Km sec-1
C. 1000 Km h-1
D. 500 Km h-1

[Physics | Unit: Current Electricity | Topic: Circuits and resistance]
Q.190. In certain circuit, if the transistor has a collector current of 10 mA and base current of 50 uA, then the current gain of the transistor is:
A. 250
B. 100
C. 150
D. 200

[Physics | Unit: Electronics | Topic: Semiconductors and electronic devices]
Q.191. A signal that is applied at the inverting input terminal of an op-amplifier undergo amplification, at the output terminal with a phase shift of:
A. 0°
B. 270°
C. 360°
D. 180°

[Physics | Unit: Thermodynamics | Topic: Heat and thermal physics]
Q.192. Solar energy at normal incidence outside the earth’s atmosphere is about:
A. 2.5 kWm-2
B. 0.6 kWm-2
C. 1.4 kWm-2
D. 2.0 kWm-2

[Physics | Unit: Force and Motion | Topic: Kinematics, Newton laws and momentum]
Q.193. Linear velocity or tangential velocity of any particle moving in a circular path of radlus 2m with angular velocity 8 rads-1 will be:
A. 16 ms-1
B. 4 ms-1
C. 10 ms-1
D. 6 ms-1

[Physics | Unit: Rotational and Circular Motion | Topic: Angular motion and torque]
Q.194. What is torque ‘τ’ in a circular motion?
A. τ = mr2π
B. τ = mr2α
C. τ = mrα
D. τ = mr2 /α

[Physics | Unit: Waves | Topic: Waves, sound and SHM]
Q.195. If the mass attached with a spring becomes four times, the time period of vibration becomes:
A. One fourth
B. 3/4
C. Half
D. Double

[Physics | Unit: Work and Energy | Topic: Work, power and energy]
Q.196. A body of mass 6 g falls under action of gravity. At initial position ‘A’ its P.E. is 480 J and K.E. is 0 J. During its downward journey at point ‘B’ its energies will be (g = 10 ms-2)
A. P.E. = 300 J and K.E. = 180 J
B. P.E. = 180 J and K.E. = 300 J
C. P.E. = 230 J and K.E. = 250 J
D. P.E. = 250 J and K.E. = 230 J

[Physics | Unit: Fluid Dynamics | Topic: Fluid flow and Bernoulli principle]
Q.197. A tiny droplet of oil of density ‘ρ’ and radius ‘r’ falls through air under force of gravity. If viscosity of air is ‘η’, the terminal velocity acquired by the oil drop is given by:
A. vt = 4gr2ρ / 9η
B. vt = 9ηr2ρ / 4g
C. vt = 2gr2ρ / 9η
D. vt = 9ηr2ρ / 2g

[Physics | Unit: Fluid Dynamics | Topic: Fluid flow and Bernoulli principle]
Q.198. Torricelli’s theorem be written as:
A. v2 = √ 2g (h1 - h2)
B. v2 = √ g (h2 - h1)
C. v2 = √ 2g (h2 - h1)
D. v2 = √ g (h1 - h2)

[Physics | Unit: Waves | Topic: Waves, sound and SHM]
Q.199. When the spaceship rotates with _ frequency, the artificial gravity like earth is produced to inhabitants of the ship
A. 2π √ R / g
B. 2π √ ℓ / g
C. 1 / 2π √ R / g
D. f ≥ √(g / r)

[Physics | Unit: Waves | Topic: Waves, sound and SHM]
Q.200. In a microwave oven, the wave produced has a wavelength of 12 cm at a frequency of:
A. 2.45 GHz
B. 2452 Hz
C. 2456 Hz
D. 2455 Hz

[Physics | Unit: Waves | Topic: Waves, sound and SHM]
Q.201. Speed of the waves is equal to:
A. fλ
B. λ/T
C. Both A and B
D. λT

[Physics | Unit: Electrostatics | Topic: Electric field, potential and capacitance]
Q.202. A particle carrying charge of 2e falls through a potential difference of 3.0 V. Calculate the energy required by it
A. 9.6 x 10-19 J
B. 9.1 x 10-19 J
C. 1.6 x 10-19 J
D. 6.0 x 10-19 J

[Physics | Unit: Current Electricity | Topic: Circuits and resistance]
Q.203. The deviation of I-V graph from the straight line is due to:
A. Decrease in temperature and decrease in resistance
B. Increase in temperature and increase in resistance
C. Decrease in temperature and increase in resistance
D. Increase in temperature and decrease in resistance

[Physics | Unit: Current Electricity | Topic: Circuits and resistance]
Q.204. The fractional change in resistance per Kelvin is known as:
A. Temperature coefficient of resistance
B. Thermal coefficient
C. Linear coefficient of expansion
D. Volumetric coefficient of expansion

[Physics | Unit: Current Electricity | Topic: Circuits and resistance]
Q.205. The energy supplied by the cell to the charge carriers is derived from the conversion of:
A. Heat energy into Electrical energy
B. Chemical energy into Electrical energy
C. Solar energy into Electrical energy
D. Mechanical energy into Electrical energy

[Physics | Unit: Electromagnetism | Topic: Magnetic fields and force]
Q.206. Force experienced by a moving change in a magnetic field is:
A. F = BA cosϴ
B. F = μo NI
C. F = q (v x B)
D. F = I (L x B)

[Physics | Unit: Electromagnetism | Topic: Magnetic fields and force]
Q.207. The value of permeability of free space μo is:
A. 4π x 10-7 WbA-1m-1
B. 4π x 102 WbA-2m-2
C. 4π x 10-7 WbA-2m-1
D. 4π x 102 WbA-1m-2

[Physics | Unit: Current Electricity | Topic: Circuits and resistance]
Q.208. What shunt resistance must be connected across a Galvanometer of 20 Ω resistance which gives full scale deflection with 2.0 A current, so as to convert it into an Ammeter of range 10 A?
A. 5 Ω
B. 2 Ω
C. 3 Ω
D. 4 Ω

[Physics | Unit: Current Electricity | Topic: Circuits and resistance]
Q.209. The current measuring part of the Avometer consists of number of low resistances connected:
A. At an angle of 180° with the galvanometer
B. Parallel with the galvanometer
C. At an angle of 45° with the galvanometer
D. Perpendicular to the galvanometer

[Physics | Unit: Force and Motion | Topic: Kinematics, Newton laws and momentum]
Q.210. A charge of two microcoulombs (2 μC) moves with velocity of two meter per second (2 m/sec) in the direction of two Tesla magnetic field. The force that will act on it will be:
A. 2 N
B. Zero
C. 8 N
D. 4 N

[Physics | Unit: Electromagnetic Induction | Topic: Induction and transformer]
Q.211. We have two coils placed close to each other. When we switch on the battery connected to primary coil while keeping the sliding contact of rheostat at fixed position, the reading of Galvanometer:
A. First increases and then becomes zero
B. First increases and then becomes constant at some value
C. Increases with the passage of time
D. Remains zero

[Physics | Unit: Electromagnetic Induction | Topic: Induction and transformer]
Q.212. Power losses in a transformer can be minimized:
A. By increasing the turn ratio
B. By decreasing the turn ratio
C. By minimizing Eddy currents
D. By selecting core materials with a large hysteresis area

[Physics | Unit: Current Electricity | Topic: Circuits and resistance]
Q.213. In R-L Series circuit, the phase difference between applied voltage and current is given by the angle ϴ which is:
A. ϴ = tan-1 LR / ω
B. ϴ = tan-1 ωLR
C. ϴ = tan-1 ωL / R
D. ϴ = tan-1 ωR / L

[Physics | Unit: Current Electricity | Topic: Circuits and resistance]
Q.214. Frequency of L-C circuit will resonate under the driving action of the antenna by angular value of:
A. Capacitance and inductance
B. Impedance
C. Inductance
D. Resistance

[Physics | Unit: Electronics | Topic: Semiconductors and electronic devices]
Q.215. To convert the Si crystal into p-type semi-conductor, which group element will be doped:
A. Trivalent Element
B. Second Group Element
C. Fourth Group Element
D. Pentavalent Element

[English | Unit: Reading and Thinking Skills | Topic: Grammar, vocabulary, comprehension]
Q.216. Change the voice of the statement;"Do it."
A. Let it be done
B. Let be done it
C. It be done by you
D. Let it be did

[English | Unit: Reading and Thinking Skills | Topic: Grammar, vocabulary, comprehension]
Q.217. Change the voice of the statement;"His position rejoiced me."
A. I was rejoiced at his position
B. I was rejoiced by his position
C. I was rejoice at his position
D. I was rejoiced from his position

[English | Unit: Reading and Thinking Skills | Topic: Grammar, vocabulary, comprehension]
Q.218. Change the voice of the statement;;"Don't tell a lie."
A. Let a lie not be told
B. Don't let a lie not be told
C. Let a lie not be told by
D. Don't a lie not be told

[English | Unit: Reading and Thinking Skills | Topic: Grammar, vocabulary, comprehension]
Q.219. Change the voice of the statement;"Don't break my heart."
A. Don't let my heart broken
B. Let my heart don't be broken
C. Don't let my heart be broken by you
D. Don't let my heart be broken

[English | Unit: Reading and Thinking Skills | Topic: Grammar, vocabulary, comprehension]
Q.220. Change the voice of the statement;;"Will he give her a bracelet?"
A. Will a bracelet be given to her by he?
B. Will she be given a bracelet by him?
C. Will her be given a bracelet by him?
D. Will a bracelet be being given to her by him?
"""

q2009 = parse_year_text(2009, RAW_2009)
save_year_json(2009, q2009)
print("2009 saved, total:", len(q2009))
