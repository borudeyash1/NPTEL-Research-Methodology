# -*- coding: utf-8 -*-
import json
import os

questions = []

def add_q(mod_id, q_text, options, answer, exp, q_type='single', passage=None):
    questions.append({
        'id': len(questions) + 1,
        'module': mod_id,
        'type': q_type,
        'question': q_text,
        'options': options,
        'answer': answer,
        'explanation': exp,
        'passage': passage
    })

# MODULE 1: Foundations of Research & Research Degrees
add_q(1, 'What fundamentally sets a PhD degree apart from standard taught academic degrees?',
      ['Development of independent critical thinking and rigorous analytical abilities',
       'Preparation and qualification to independently guide others in research',
       'Exclusively memorizing factual textbook descriptions',
       'Completing fixed routine coursework and classroom tests'],
      [0, 1],
      'A PhD is distinguished by developing high-level critical thinking, original research capability, and qualification to mentor future PhD candidates.',
      'multi')

add_q(1, 'Which of the following best defines Research in an academic and scientific context?',
      ['A systematic, methodical investigation into a problem to establish facts and reach new validated conclusions',
       'Compiling popular internet blogs into a summary document',
       'Carrying out unrecorded, unstructured trial-and-error experiments in a laboratory',
       'Collecting personal subjective opinions from friends'],
      0,
      'Research is a systematic, rigorous inquiry designed to discover facts, test theories, and make novel contributions to knowledge.')

add_q(1, 'In a research degree (MS/PhD), who has the primary intellectual ownership of the work and responsibility for defending the thesis?',
      ['The research scholar / student',
       'The thesis supervisor alone',
       'The head of the department',
       'The funding agency representative'],
      0,
      'While the guide provides guidance and mentorship, the scholar has intellectual ownership and must defend the thesis.')

add_q(1, 'What is the core expectation of novelty in a doctoral (PhD) thesis compared to a Master’s thesis?',
      ['An original, peer-defensible contribution that expands the frontier of knowledge in the domain',
       'Merely running existing code on a newer operating system',
       'Submitting an unusually high page count regardless of findings',
       'Eliminating all mathematical equations in favor of descriptive text'],
      0,
      'A PhD requires substantial demonstrable originality and an advance in the state of current knowledge.')

add_q(1, 'State whether True or False: In doctoral research, negative or unexpected experimental results are completely useless and must always be concealed.',
      ['True', 'False'],
      1,
      'False. Rigorously validated negative results prevent dead ends, clarify boundaries of validity, and provide valuable scientific insights.')

add_q(1, 'Which attribute is most critical for a research scholar when navigating open-ended problems with high uncertainty?',
      ['Intellectual resilience and perseverance in the face of setbacks and ambiguous outcomes',
       'Aversion to reading peer-reviewed literature',
       'Demanding instant solutions without testing control parameters',
       'Accepting conventional wisdom uncritically without empirical verification'],
      0,
      'Research deals with uncharted frontiers; resilience, curiosity, and persistence are essential virtues.')

add_q(1, 'What is the primary role of coursework in the early stage of a PhD program?',
      ['To build foundational depth and theoretical tools necessary to formulate research questions',
       'To serve as the sole criterion for granting the doctoral title',
       'To eliminate the need for conducting an independent literature review',
       'To ensure the scholar does not spend time in the laboratory'],
      0,
      'Coursework provides the advanced mathematical, theoretical, and domain foundation required to conduct research.')

add_q(1, 'Which of the following constitute genuine motivations for pursuing a research-based career?',
      ['Desire to solve complex, unsolved scientific or technological challenges',
       'Commitment to advance scholarly knowledge and mentor next-generation researchers',
       'Seeking a career with zero performance metrics or accountability',
       'Belief that research involves no reading or technical writing'],
      [0, 1],
      'Genuine motivations include solving deep problems, intellectual inquiry, and contributing to academia and R&D.',
      'multi')

add_q(1, 'A scientific hypothesis must be "falsifiable". What does falsifiability imply?',
      ['There must exist a conceivable observation or empirical test that could disprove the hypothesis if it is incorrect',
       'The researcher is permitted to alter or falsify laboratory data',
       'The hypothesis is formulated so vaguely that no experiment can ever test it',
       'The hypothesis only applies to idealized numerical simulations'],
      0,
      'Karl Popper established that for a proposition to be scientific, it must be testable and capable of being refuted by empirical evidence.')

add_q(1, 'How does the advisor-student relationship typically evolve during a successful doctoral journey?',
      ['It transitions from close guided mentorship to an independent, peer-level intellectual collaboration',
       'It remains an inflexible top-down boss-subordinate hierarchy throughout',
       'It begins completely detached and becomes strictly micromanaged at the end',
       'It is purely an administrative commercial transaction without academic discussion'],
      0,
      'The PhD journey transitions from initial apprenticeship under guidance to peer-level scientific partnership.')

# MODULE 2: Formulating Research Questions & Problem Definition
add_q(2, 'What is the first and most foundational step in embarking on a research investigation?',
      ['Clearly defining and formulating a specific, meaningful research problem',
       'Purchasing high-end laboratory instruments before reading literature',
       'Drafting the concluding summary of the thesis',
       'Filing commercial trademark applications'],
      0,
      'Formulating a precise problem statement is the essential first step that directs all subsequent methodology.')

add_q(2, 'Which of the following best characterizes an effective research question?',
      ['It is specific, researchable, measurable, and addresses an identified gap in current knowledge',
       'It is broad, vague, and open to endless speculative opinions without metrics',
       'It is an already solved textbook problem whose answer is established',
       'It cannot be validated by any empirical or analytical procedure'],
      0,
      'A sound research question must be focused, feasible, testable, and contribute to knowledge.')

add_q(2, 'What are common pitfalls during the research problem formulation stage?',
      ['Selecting a topic that is either far too broad or trivial and inconsequential',
       'Failing to conduct an exhaustive review of state-of-the-art literature',
       'Specifying testable parameters and measurable success metrics',
       'Comparing proposed ideas against established standard benchmarks'],
      [0, 1],
      'Pitfalls include poor literature survey and picking problems that are overly ambitious or trivial.',
      'multi')

add_q(2, 'What function does the research hypothesis serve in an experimental study?',
      ['It acts as a tentative, testable proposition predicting the relationship between variables',
       'It is an immutable dogma that experiments must be manipulated to prove',
       'It is an optional cosmetic paragraph written after conclusions are finalized',
       'It substitutes for the requirement of collecting empirical data'],
      0,
      'A hypothesis proposes a testable mechanism or relationship that experiments aim to support or refute.')

add_q(2, 'State whether True or False: In engineering research, real-world problems must strictly originate from pure curiosity without consideration of industrial or societal challenges.',
      ['True', 'False'],
      1,
      'False. Engineering research heavily draws problems from industrial bottlenecks, societal needs, and resource limitations.')

add_q(2, 'What is the purpose of defining "delimitations" in a research project?',
      ['To delineate clear boundaries, operational scope, and intentional exclusions of the investigation',
       'To hide procedural flaws or experimental mistakes from reviewers',
       'To prohibit other researchers from publishing in the same area',
       'To guarantee instant acceptance in high-impact journals'],
      0,
      'Delimitations define the boundaries, assumptions, and scope within which the findings are valid.')

add_q(2, 'In the SMART framework for research objectives, what does the "M" stand for?',
      ['Measurable', 'Manipulated', 'Mystical', 'Monotonous'],
      0,
      'SMART stands for Specific, Measurable, Achievable, Relevant, and Time-bound.')

add_q(2, 'How does applied research differ fundamentally from basic (fundamental) research?',
      ['Applied research aims to solve practical, real-world challenges, while basic research expands fundamental scientific principles',
       'Applied research never uses scientific methodology',
       'Basic research does not follow mathematical principles',
       'Basic research can never contribute to future technological innovations'],
      0,
      'Basic research seeks foundational understanding of natural phenomena; applied research addresses practical technical needs.')

add_q(2, 'When surveying the domain, what does identifying a "research gap" imply?',
      ['Discovering an unaddressed question, contradictory findings, or missing mechanism in current literature',
       'Finding an open physical desk in the graduate research laboratory',
       'Finding a spelling mistake in a printed textbook',
       'Noticing that dozens of papers have reached identical conclusions'],
      0,
      'A research gap indicates a missing piece of knowledge, unanswered question, or conflicting results in literature.')

add_q(2, 'Which of the following represents an empirical research question?',
      ['How does increasing sintering temperature from 900°C to 1300°C affect the fracture toughness of zirconia?',
       'What makes abstract sculpture emotionally evocative to ancient philosophers?',
       'What will humanity\'s social structure look like ten thousand years in the future?',
       'Why should people appreciate poetry?'],
      0,
      'Empirical questions involve quantifiable variables that can be verified through observation and testing.')

# MODULE 3: Developing Hypotheses & Research Objectives
add_q(3, 'What is the fundamental difference between a null hypothesis (H0) and an alternative hypothesis (H1)?',
      ['H0 posits no significant effect or difference, whereas H1 posits the presence of an effect or difference',
       'H0 is always assumed to be false prior to collecting data',
       'H1 states that the experiment was improperly executed',
       'H0 can only be formulated for non-numerical qualitative studies'],
      0,
      'In statistical hypothesis testing, H0 assumes no effect or difference, and H1 represents the research claim being tested.')

add_q(3, 'Which of the following is a key requirement of a scientifically sound hypothesis?',
      ['It must be logically consistent and empirically testable using available or designable methods',
       'It must be impossible to disprove under any experimental scenario',
       'It must be stated in poetic language to maintain ambiguity',
       'It must guarantee that the outcome matches the researcher\'s personal preference'],
      0,
      'A valid scientific hypothesis must be testable, logical, and capable of being supported or rejected by data.')

add_q(3, 'In statistical testing, what constitutes a Type I error (alpha error)?',
      ['Rejecting a true null hypothesis (false positive)',
       'Failing to reject a false null hypothesis (false negative)',
       'Entering incorrect digits into a spreadsheet',
       'Selecting an inappropriate graphic format for a chart'],
      0,
      'Type I error occurs when the null hypothesis is true, but is incorrectly rejected.')

add_q(3, 'In statistical testing, what constitutes a Type II error (beta error)?',
      ['Failing to reject a false null hypothesis (false negative)',
       'Rejecting a true null hypothesis (false positive)',
       'Calibrating an instrument with standard weights',
       'Increasing the sample size in an experiment'],
      0,
      'Type II error occurs when the null hypothesis is false, but the test fails to reject it.')

add_q(3, 'State whether True or False: Reducing the significance level alpha from 0.05 to 0.01 reduces the probability of Type I error, but increases the probability of Type II error for a fixed sample size.',
      ['True', 'False'],
      0,
      'True. There is an inherent trade-off between alpha and beta when sample size is held constant.')

add_q(3, 'What is the statistical power of a hypothesis test?',
      ['The probability of correctly rejecting a false null hypothesis (1 - beta)',
       'The electrical wattage consumed by the laboratory computer during testing',
       'The probability of making a Type I error',
       'The ratio of independent variables to dependent variables'],
      0,
      'Statistical power (1 - beta) represents the probability of detecting an effect when a true effect actually exists.')

add_q(3, 'Which factor directly increases the statistical power of an experimental test?',
      ['Increasing the sample size (number of observations)',
       'Reducing the significance level to near zero',
       'Increasing measurement noise and random error',
       'Decreasing the magnitude of the effect size under study'],
      0,
      'Larger sample size reduces standard error, which directly enhances the statistical power of the test.')

add_q(3, 'What is the defining characteristic of a directional (one-tailed) hypothesis compared to a non-directional (two-tailed) hypothesis?',
      ['A directional hypothesis specifies the anticipated direction of the effect (e.g., A is greater than B)',
       'A directional hypothesis can only be tested once in a lifetime',
       'A two-tailed hypothesis does not require any significance threshold',
       'A directional hypothesis never allows calculation of p-values'],
      0,
      'A directional hypothesis explicitly posits whether a parameter will increase or decrease.')

add_q(3, 'What is the role of a pilot study in refining research objectives and hypotheses?',
      ['To test experimental feasibility, assess variability, and identify procedural hurdles on a small scale',
       'To publish the final conclusions of the PhD before starting experiments',
       'To avoid obtaining ethical clearance for human participant testing',
       'To replace the primary thesis experiment entirely'],
      0,
      'A pilot study checks experimental protocol, estimates variance, and evaluates feasibility before committing resources.')

add_q(3, 'Which of the following statements about research objectives is correct?',
      ['Objectives must logically break down the overarching research goal into concrete, actionable milestones',
       'Objectives should be vague statements of general philosophy',
       'A thesis must contain at least 50 distinct objectives to be valid',
       'Objectives must never mention the variables being investigated'],
      0,
      'Research objectives translate the broad research goal into specific, achievable methodological steps.')

# MODULE 4: Theoretical Frameworks & Applied vs Basic Research
add_q(4, 'According to the Stokes model of scientific research (Pasteur’s Quadrant), what defines "Use-Inspired Basic Research"?',
      ['Research that seeks fundamental understanding while being inspired by practical considerations of use (e.g., Louis Pasteur)',
       'Pure basic research with zero regard for practical application (e.g., Niels Bohr)',
       'Pure applied development without seeking general scientific principles (e.g., Thomas Edison)',
       'Routine testing of commercial products without scientific inquiry'],
      0,
      'Pasteur’s Quadrant represents research motivated simultaneously by deep fundamental understanding and real-world practical utility.')

add_q(4, 'In Pasteur’s Quadrant, which quadrant is exemplified by Niels Bohr’s work on atomic structure?',
      ['Pure basic research (quest for fundamental understanding without use considerations)',
       'Pure applied research',
       'Use-inspired basic research',
       'Empirical manufacturing'],
      0,
      'Bohr\'s work exemplifies pure basic research focused entirely on fundamental scientific insight.')

add_q(4, 'In Pasteur’s Quadrant, which quadrant is exemplified by Thomas Edison’s inventions?',
      ['Pure applied research (quest for immediate practical utility without deep fundamental theory)',
       'Pure basic research',
       'Use-inspired basic research',
       'Non-systematic tinkering'],
      0,
      'Edison represents pure applied research aimed directly at commercial and functional utility.')

add_q(4, 'What is the role of a theoretical framework in engineering and scientific research?',
      ['It provides the overarching conceptual structure, governing laws, and assumptions that contextualize the study',
       'It provides a decorative list of equations to impress non-technical readers',
       'It eliminates the need for validating experimental data',
       'It forbids the use of computational simulations'],
      0,
      'A theoretical framework situates the investigation within established laws, principles, and concepts.')

add_q(4, 'State whether True or False: Basic scientific research and applied technological development exist in complete isolation and never influence each other.',
      ['True', 'False'],
      1,
      'False. Basic research reveals principles enabling new technologies, while technological tools stimulate new fundamental questions.')

add_q(4, 'What is meant by an "inductive" approach to research?',
      ['Moving from specific empirical observations to general theories and broader generalizations',
       'Deducing specific testable hypotheses from an existing grand theory',
       'Testing electrical inductance of copper coils in a magnetic field',
       'Assuming that all published theories are permanently infallible'],
      0,
      'Inductive logic reasons from specific observations toward broader generalizations and theories.')

add_q(4, 'What is meant by a "deductive" approach to research?',
      ['Starting from established theory, deriving specific hypotheses, and testing them with empirical data',
       'Formulating a theory only after gathering random unorganized data',
       'Eliminating mathematics from physical models',
       'Translating foreign language papers into English'],
      0,
      'Deductive research flows from general theoretical principles to specific testable hypotheses and empirical validation.')

add_q(4, 'Which of the following is an example of an operational definition of a variable?',
      ['Defining corrosion rate as weight loss per unit surface area per unit time (mg/cm²/day)',
       'Defining corrosion rate as how old metal looks to a passerby',
       'Defining fatigue as a feeling of tiredness in the morning',
       'Defining strength as being emotionally sturdy'],
      0,
      'An operational definition specifies the exact measurement procedure and units used to quantify a variable.')

add_q(4, 'What constitutes a "construct" in scientific research?',
      ['An abstract theoretical concept (e.g., intelligence, turbulence, organizational trust) that cannot be directly observed but is inferred through indicators',
       'A physical concrete building on a university campus',
       'A piece of steel scaffolding used in experimental rigs',
       'A standard software compiler error message'],
      0,
      'A construct is an abstract concept formulated to explain observed phenomena, measured through operational indicators.')

add_q(4, 'Why is understanding the philosophical underpinnings (epistemology and ontology) relevant to research methodology?',
      ['It clarifies assumptions regarding the nature of reality and how valid knowledge can be acquired and justified',
       'It is required by patent offices before filing an engineering claim',
       'It replaces the requirement for data visualization tools',
       'It allows researchers to skip laboratory calibration routines'],
      0,
      'Epistemology and ontology clarify assumptions about what constitutes valid knowledge and guiding methodological choices.')

# MODULE 5: University Ecosystem, Innovation & IITM Research Park
add_q(5, 'What was the foundational vision behind the creation of the IIT Madras Research Park (IITMRP)?',
      ['To foster deep industry-academia collaboration by bringing corporate R&D teams and university researchers into close physical proximity',
       'To build residential housing for undergraduate students away from campus',
       'To isolate university professors from industrial projects and practical applications',
       'To create a retail shopping mall and multiplex for campus residents'],
      0,
      'IITMRP was designed to facilitate synergy between university expertise, student talent, and corporate R&D labs.')

add_q(5, 'In the context of research and cognitive science discussed in Lecture 5, what does the concept of "split-brain creativity" refer to?',
      ['Balancing analytical, logical left-brain thinking with imaginative, lateral right-brain synthesis in problem-solving',
       'Surgically dividing the brain of researchers to increase productivity',
       'Working simultaneously on two completely unrelated dissertations without coordination',
       'Alternating between sleeping and writing code in 10-minute bursts'],
      0,
      'Split-brain thinking emphasizes harmonizing analytical rigor with associative, creative synthesis.')

add_q(5, 'What constitutes the "Triple Helix" model of innovation in regional development?',
      ['The synergistic interaction among University (Academia), Industry, and Government',
       'The combination of Physics, Chemistry, and Mathematics departments',
       'The three-stage progression of Bachelor, Master, and PhD degrees',
       'The interaction between Hardware, Software, and Network infrastructure'],
      0,
      'The Triple Helix model conceptualizes innovation as arising from collaborative interactions between academia, industry, and government.')

add_q(5, 'Which metric indicates successful technology commercialization from an academic research incubator?',
      ['The creation of viable spinoff deep-tech startups, patented technologies licensed, and industry-sponsored R&D projects',
       'The total number of desks occupied in the library during examination week',
       'The number of academic festivals conducted during the academic year',
       'The quantity of promotional brochures printed and distributed'],
      0,
      'Technology transfer success is measured by patent licensing, commercial spinoffs, and industry-sponsored innovation.')

add_q(5, 'State whether True or False: Technology Readiness Levels (TRL) range from TRL 1 (basic principles observed) to TRL 9 (actual system proven in operational environment).',
      ['True', 'False'],
      0,
      'True. NASA and international standards define TRL from 1 (basic principles) up to 9 (proven operational deployment).')

add_q(5, 'Academic research typically focuses most heavily on which stages of the Technology Readiness Level (TRL) scale?',
      ['TRL 1 to TRL 3 (basic principles, technology concept formulated, and experimental proof of concept)',
       'TRL 8 to TRL 9 exclusively (commercial mass manufacturing and distribution)',
       'TRL 9 exclusively',
       'TRL 0 (pre-conceptual daydreaming)'],
      0,
      'University research predominantly pioneers TRL 1 to 3/4, creating discoveries that industry scales up to TRL 7-9.')

add_q(5, 'What is the "Valley of Death" in technology innovation and commercialization?',
      ['The difficult gap between early-stage academic proof-of-concept (TRL 3-4) and commercial industrial deployment (TRL 7-9) where many innovations fail due to lack of funding/scale-up',
       'A geographic depression where university research laboratories are constructed',
       'The drop in academic grades when graduate students begin writing their thesis',
       'The permanent loss of laboratory data caused by hard drive failure'],
      0,
      'The Valley of Death represents the transition barrier between academic prototyping and commercially viable production.')

add_q(5, 'How do university incubation centers mitigate the risks of the innovation "Valley of Death"?',
      ['By providing seed funding, technical mentorship, prototyping facilities, and access to venture networks',
       'By prohibiting startup founders from contacting venture capital firms',
       'By forcing all student innovations to remain unpatented public domain secrets',
       'By requiring startups to pay all profits to the university immediately'],
      0,
      'Incubators provide infrastructure, seed grants, intellectual property advice, and mentorship to de-risk early-stage ventures.')

add_q(5, 'Which factor is critical in managing multidisciplinary innovation teams effectively?',
      ['Clear common vision, shared vocabulary, mutual intellectual respect, and complementary technical expertise',
       'Enforcing rigid departmental silos and forbidding inter-departmental communication',
       'Allowing only one senior member to ever speak or propose ideas',
       'Eliminating written design documentation and review meetings'],
      0,
      'Multidisciplinary success demands cross-disciplinary communication, shared goals, and collaborative integration.')

add_q(5, 'What role does an institutional Office of Industrial Consultancy and Sponsored Research (ICSR) play in a university?',
      ['Facilitating industry partnerships, managing sponsored research contracts, patent filings, and technology licensing',
       'Organizing undergraduate social gatherings and sports events',
       'Conducting semester exams for first-year undergraduate courses',
       'Handling routine campus cafeteria maintenance'],
      0,
      'ICSR offices bridge academia and external industries by administering funded grants, consultancy, and intellectual property.')

# MODULE 6: Overview of Literature Survey & Bibliometrics
add_q(6, 'What is the primary objective of conducting a thorough literature survey before undertaking experimental work?',
      ['To understand existing knowledge, identify gaps, avoid rediscovering known solutions, and contextualize findings',
       'To copy existing text verbatim into one’s own dissertation',
       'To prove that no other researcher in history has ever considered the topic',
       'To fulfill a bureaucratic formality with minimum reading'],
      0,
      'A literature survey ensures the researcher understands the state-of-the-art, avoids redundant efforts, and finds genuine research gaps.')

add_q(6, 'Which of the following distinguishes a "systematic literature review" from a traditional narrative review?',
      ['A transparent, reproducible search protocol with explicit inclusion/exclusion criteria and structured data synthesis',
       'Relying purely on subjective informal searches on general web search engines',
       'Excluding all peer-reviewed journal papers in favor of personal blogs',
       'Having no defined scope or search keywords'],
      0,
      'Systematic literature reviews follow rigorous, pre-defined, and reproducible protocols to minimize selection bias.')

add_q(6, 'What is the definition of a "Primary Source" in scientific literature?',
      ['Original peer-reviewed research papers and conference proceedings presenting new empirical findings or theoretical derivations',
       'Textbooks summarizing established knowledge for undergraduate students',
       'Popular science articles in daily newspapers',
       'An encyclopedia entry summarizing a broad scientific discipline'],
      0,
      'Primary literature comprises first-hand publications of original experimental or theoretical discoveries by the authors.')

add_q(6, 'What is the definition of a "Secondary Source" in scientific literature?',
      ['Review articles, meta-analyses, and textbooks that synthesize, evaluate, and summarize primary research articles',
       'Original laboratory notebook entries recorded during an experiment',
       'Unpublished raw data output files from a mass spectrometer',
       'A preliminary draft manuscript before submission'],
      0,
      'Secondary sources analyze, summarize, and integrate primary scientific contributions.')

add_q(6, 'What does "Bibliometrics" refer to in academic research?',
      ['The quantitative statistical analysis of publications, citations, authors, and academic output patterns',
       'The physical measurement of book weight and binding dimensions',
       'The manual transcription of ancient manuscripts into modern fonts',
       'The classification of library shelving layouts'],
      0,
      'Bibliometrics applies statistical and mathematical methods to analyze books, articles, and citation networks.')

add_q(6, 'Which Boolean operator narrows a literature search query by requiring all terms to be present in the results?',
      ['AND', 'OR', 'NOT', 'XOR'],
      0,
      'The AND operator restricts results to records that contain all specified keywords.')

add_q(6, 'Which Boolean operator expands a literature search query to capture synonyms or related terminology?',
      ['OR', 'AND', 'NOT', 'NAND'],
      0,
      'The OR operator retrieves records containing either of the specified terms, useful for synonyms.')

add_q(6, 'What is "forward citation searching" (forward tracking) in literature review?',
      ['Finding newer articles that have cited a known foundational landmark paper since its publication',
       'Reading the reference list at the back of an existing paper to find older works',
       'Predicting what papers will be published ten years in the future',
       'Translating citations from one language to another'],
      0,
      'Forward tracking identifies newer papers that cite a given work, tracking how the scientific idea has evolved.')

add_q(6, 'What is "backward citation searching" (backward chaining) in literature review?',
      ['Examining the reference list/bibliography of a relevant paper to uncover previous foundational studies',
       'Searching for articles that cite the paper in future years',
       'Deleting references that contradict the researcher’s thesis',
       'Reading papers in reverse order from the conclusion to the abstract'],
      0,
      'Backward chaining examines cited references to find earlier foundational works upon which the study was built.')

add_q(6, 'State whether True or False: Predatory journals perform rigorous, uncompromising double-blind peer review before publication.',
      ['True', 'False'],
      1,
      'False. Predatory journals exploit the open-access model by charging author fees without providing genuine peer review or editorial oversight.')

# MODULE 7: Databases, Search Strategies & Web of Science
add_q(7, 'Which company currently owns and maintains the Web of Science (WoS) citation database?',
      ['Clarivate (formerly Thomson Reuters / ISI)',
       'Elsevier',
       'Google Inc.',
       'Springer Nature'],
      0,
      'Web of Science is maintained and curated by Clarivate.')

add_q(7, 'What was the pioneering historical citation index founded by Eugene Garfield that evolved into Web of Science?',
      ['Science Citation Index (SCI)',
       'Google Scholar Index',
       'Scopus Abstract Network',
       'arXiv Preprint Archive'],
      0,
      'Eugene Garfield founded the Institute for Scientific Information (ISI) and created the Science Citation Index (SCI).')

add_q(7, 'What is the primary function of wildcards such as asterisk (*) in database search queries?',
      ['Truncation: searching for words with different character endings (e.g., nano* matches nanometer, nanoscale, nanotechnology)',
       'Multiplying search terms by a constant integer',
       'Excluding all articles written after the year 2000',
       'Highlighting search terms in red bold font in the browser'],
      0,
      'The asterisk wildcard truncates words to capture root variations and plural forms.')

add_q(7, 'In Web of Science, what does the core index SCIE stand for?',
      ['Science Citation Index Expanded',
       'Scientific Communication and International Education',
       'Scopus Citation Index Electronic',
       'Standard Computing Information Exchange'],
      0,
      'SCIE stands for Science Citation Index Expanded, the core multidisciplinary index in Web of Science.')

add_q(7, 'Which Web of Science collection indexes scholarly contributions in social sciences?',
      ['SSCI (Social Sciences Citation Index)',
       'AHCI (Arts & Humanities Citation Index)',
       'ESCI (Emerging Sources Citation Index)',
       'BKCI (Book Citation Index)'],
      0,
      'SSCI covers journals in anthropology, economics, sociology, and related social science disciplines.')

add_q(7, 'What is the purpose of the Emerging Sources Citation Index (ESCI) in Web of Science?',
      ['To index high-quality peer-reviewed journals of regional importance or emerging fields before possible inclusion in SCIE/SSCI',
       'To archive retracted fraudulent papers',
       'To list non-academic blog articles and social media threads',
       'To track student homework assignments'],
      0,
      'ESCI expands coverage to peer-reviewed publications of regional importance and emerging disciplines.')

add_q(7, 'When conducting a search on Web of Science, what fields are queried when selecting "Topic" (TS)?',
      ['Title, Abstract, Author Keywords, and Keywords Plus',
       'Full body text of the paper including appendixes',
       'Author institutional street addresses only',
       'Journal publisher financial accounts'],
      0,
      'Topic search in Web of Science checks Title, Abstract, Author Keywords, and algorithmically generated Keywords Plus.')

add_q(7, 'What are "Keywords Plus" in Web of Science records?',
      ['Words and phrases frequently appearing in the titles of references cited by the article, generated algorithmically by Clarivate',
       'Keywords chosen manually by the journal editor',
       'Words added by readers through online comments',
       'Keywords generated by translating foreign titles'],
      0,
      'Keywords Plus are algorithmically extracted terms from the titles of articles cited by the paper.')

add_q(7, 'In a database search string, what does enclosing terms in quotation marks (e.g., "fuel cell") ensure?',
      ['Exact phrase matching: the terms must appear together in the exact specified order',
       'The database ignores both words during the search',
       'The database treats the quotation marks as mathematical division symbols',
       'The query will only search in patent databases'],
      0,
      'Quotation marks enforce phrase searching, ensuring words appear consecutively rather than scattered across the document.')

add_q(7, 'What does the proximity operator NEAR/n in Web of Science specify?',
      ['The search terms must appear within n words of each other, in any order',
       'The search terms must appear in adjacent paragraphs',
       'The search terms must be written by authors living in adjacent cities',
       'The publication year must be within n years of the current date'],
      0,
      'NEAR/n finds records where the two terms are separated by at most n words, regardless of sequence.')

# MODULE 8: Scientific Literature Classification & Scopus
add_q(8, 'Which publishing enterprise owns and manages the Scopus abstract and citation database?',
      ['Elsevier',
       'Clarivate',
       'IEEE',
       'Springer Nature'],
      0,
      'Scopus is the flagship abstract and citation database developed and maintained by Elsevier.')

add_q(8, 'Which metric developed for Scopus measures journal citation impact normalized for subject field differences?',
      ['SNIP (Source Normalized Impact per Paper)',
       'Journal Impact Factor (JIF)',
       'Article Influence Score',
       'Immediacy Index'],
      0,
      'SNIP, developed by Henk Moed at CWTS Leiden, corrects for differences in citation practices between scientific fields.')

add_q(8, 'What is the SCImago Journal Rank (SJR) metric based upon?',
      ['A PageRank-style algorithm where citations are weighted based on the prestige and quality of the citing journal',
       'The total physical page count of all articles published in a calendar year',
       'The subscription price charged by the journal publisher',
       'The total number of authors per published article'],
      0,
      'SJR uses an eigenvector centrality algorithm (similar to Google PageRank) to transfer prestige from citing journals.')

add_q(8, 'What is CiteScore, and how is it calculated in Scopus?',
      ['The ratio of citations received over a 4-year window to peer-reviewed documents published in that same 4-year window',
       'The number of downloads of an article divided by the number of views',
       'The total number of citations received in the first 24 hours of publication',
       'The number of typos corrected in errata notices'],
      0,
      'CiteScore tracks citations over a 4-year period to publications from those same 4 years.')

add_q(8, 'How does the document coverage of Scopus generally compare with Web of Science Core Collection?',
      ['Scopus has a broader, larger title count and higher coverage of non-English/international and conference papers',
       'Web of Science indexes ten times more journals than Scopus',
       'Scopus indexes exclusively medical journals and zero engineering journals',
       'Scopus does not track citations or author affiliations'],
      0,
      'Scopus provides broader indexing across conference proceedings, applied engineering, and international titles.')

add_q(8, 'What is the primary purpose of an author identifier such as ORCID (Open Researcher and Contributor ID)?',
      ['To provide a persistent, unique digital identifier that distinguishes individual researchers unambiguously despite name changes or homonyms',
       'To assign credit scores for bank loan approvals to graduate students',
       'To replace the researcher’s passport when traveling to conferences',
       'To encrypt the text of research papers to prevent downloading'],
      0,
      'ORCID uniquely identifies scholars, preventing confusion arising from shared names, transliteration differences, or institutional moves.')

add_q(8, 'What is the Elsevier Scopus Author ID?',
      ['An automatically generated profile identifier assigned by Scopus algorithms grouping an author’s publications based on affiliation and co-authors',
       'A secret password required to read open-access papers',
       'A government social security number for scientists',
       'An ID given only to Nobel Prize recipients'],
      0,
      'Scopus assigns an automated Author ID to cluster publications by the same author using algorithmic matching.')

add_q(8, 'Which of the following is a preprint repository predominantly used in physics, mathematics, and computer science?',
      ['arXiv', 'PubMed', 'ERIC', 'LexisNexis'],
      0,
      'arXiv, hosted by Cornell University, is the leading open-access preprint server for physics, math, and computer science.')

add_q(8, 'State whether True or False: Preprints on arXiv have already undergone rigorous, formal double-blind peer review before posting.',
      ['True', 'False'],
      1,
      'False. Preprints are shared prior to formal peer review, allowing rapid dissemination and community feedback.')

add_q(8, 'What is a key risk of citing non-peer-reviewed preprints in a doctoral dissertation?',
      ['The methodologies or findings may contain uncorrected errors, false claims, or invalid data that have not been vetted by experts',
       'Preprints are illegal to download under copyright law',
       'Preprints can only be read on specialized supercomputers',
       'Preprint servers delete all papers after thirty days'],
      0,
      'Because preprints lack formal peer review, their experimental protocols and findings must be evaluated with caution.')

# MODULE 9: Citation Management & Introduction to LaTeX
add_q(9, 'What is the file extension of a BibTeX database file used in LaTeX document preparation?',
      ['.bib', '.tex', '.bbl', '.aux'],
      0,
      'BibTeX databases are stored as plain text files with the .bib extension.')

add_q(9, 'Which LaTeX environment is used to produce numbered mathematical equations on their own dedicated line?',
      ['\\begin{equation} ... \\end{equation}',
       '\\begin{math} ... \\end{math}',
       '\\begin{center} ... \\end{center}',
       '\\begin{figure} ... \\end{figure}'],
      0,
      'The equation environment creates a centered, numbered mathematical formula.')

add_q(9, 'In a BibTeX entry, what is the identifier called that immediately follows the entry type (e.g., @article{smith2021, ...)?',
      ['Citation key (cite key)',
       'Digital Object Identifier (DOI)',
       'ISSN number',
       'Macro variable'],
      0,
      'The citation key is the unique tag used in the LaTeX source text (e.g., \\cite{smith2021}) to link the reference.')

add_q(9, 'What is the correct LaTeX syntax to cite a reference in the text when using standard BibTeX?',
      ['\\cite{key}',
       '\\reference{key}',
       '\\include{key}',
       '\\biblink{key}'],
      0,
      'The standard command to insert an in-text citation in LaTeX is \\cite{key}.')

add_q(9, 'In LaTeX, what is the purpose of the natbib package?',
      ['To enable flexible author-year and customized numeric citation formatting and rich citation commands like \\citep and \\citet',
       'To compute high-precision differential equations numerically',
       'To translate English text into other languages automatically',
       'To design graphical user interfaces in C++'],
      0,
      'natbib provides advanced author-year and numerical citation styles, including parenthetical (\\citep) and textual (\\citet) citations.')

add_q(9, 'When compiling a LaTeX document with BibTeX bibliography from the command line, what is the standard execution sequence?',
      ['pdflatex -> bibtex -> pdflatex -> pdflatex',
       'bibtex -> pdflatex',
       'pdflatex only once',
       'bibtex -> bibtex -> pdflatex'],
      0,
      'The 4-step sequence writes citation requests to .aux, generates .bbl with bibtex, incorporates citations, and resolves cross-references.')

add_q(9, 'What command in LaTeX specifies the name of the BibTeX file containing bibliographic entries?',
      ['\\bibliography{filename} (without .bib extension)',
       '\\bibliographystyle{filename.bib}',
       '\\inputbib{filename.bib}',
       '\\openfile{filename}'],
      0,
      '\\bibliography{filename} links the database, and the .bib extension must be omitted in standard usage.')

add_q(9, 'In LaTeX, what symbol denotes a line comment that is ignored by the compiler?',
      ['%', '#', '//', '/*'],
      0,
      'The percent sign (%) denotes a comment in LaTeX source code.')

add_q(9, 'What is the difference between inline math mode and display math mode in LaTeX?',
      ['Inline math ($...$) formats formulas within running text; display math (\\[...\\] or equation) formats formulas on a separate centered line',
       'Inline math is only for addition, while display math is for division',
       'Display math cannot render Greek letters',
       'Inline math requires purchasing a commercial license'],
      0,
      'Inline math sits inside regular text paragraphs, whereas display math isolates formulas on distinct lines for prominence.')

add_q(9, 'Why is LaTeX preferred over WYSIWYG word processors for complex scientific dissertations?',
      ['Superior mathematical typesetting, automated cross-referencing, robust bibliographic management, and stable handling of massive documents',
       'LaTeX does not require typing text on a keyboard',
       'LaTeX automatically runs experiments in the background',
       'LaTeX documents can only be opened by university professors'],
      0,
      'LaTeX excels in mathematical typesetting, precise layout control, automated numbering, and handling large manuscripts.')

# MODULE 10: Advanced Bibliometrics, h-index & Journal Metrics
add_q(10, 'How is the h-index of a researcher formally defined (introduced by J.E. Hirsch in 2005)?',
      ['A researcher has index h if h of their N papers have at least h citations each, and the other papers have fewer than or equal to h citations',
       'The total number of papers published divided by the researcher’s age',
       'The total citation count divided by the number of years since PhD',
       'The number of papers published in journals with impact factor greater than 10'],
      0,
      'A scientist has index h if h of their papers have at least h citations each, balancing productivity with citation impact.')

add_q(10, 'If a researcher has published 5 papers with citation counts [15, 12, 8, 4, 1], what is the researcher’s h-index?',
      ['3', '4', '5', '8'],
      1,
      'Rank 1: 15 (>=1), Rank 2: 12 (>=2), Rank 3: 8 (>=3), Rank 4: 4 (>=4), Rank 5: 1 (<5). Exactly 4 papers have at least 4 citations, so h = 4.')

add_q(10, 'What is a major limitation of the h-index?',
      ['It cannot decrease over time, disadvantages early-career researchers, and is insensitive to highly cited breakthrough blockbuster papers',
       'It fluctuates wildly depending on the day of the week',
       'It cannot be computed for scientists working outside the United States',
       'It requires running complex non-linear simulations to evaluate'],
      0,
      'Limitations include favoring senior researchers with long careers and ignoring citation counts beyond h (the tail effect).')

add_q(10, 'What is the g-index proposed by Leo Egghe as an improvement over the h-index?',
      ['The largest number g such that the top g articles together have accumulated at least g^2 citations',
       'The geometric mean of all citations received by the author',
       'The total number of grants awarded divided by publications',
       'The total number of citations divided by total co-authors'],
      0,
      'The g-index gives more weight to highly cited benchmark articles by requiring the top g papers to have >= g^2 total citations.')

add_q(10, 'How is the 2-year Journal Impact Factor (JIF) calculated by Clarivate Journal Citation Reports (JCR)?',
      ['Citations in year Y to items published in the journal during years (Y-1) and (Y-2), divided by total citable items published in (Y-1) and (Y-2)',
       'Total citations received since the founding of the journal divided by total issues published',
       'Number of articles accepted divided by number of articles rejected in year Y',
       'Average number of pages per published paper in the last two years'],
      0,
      'JIF equals citations in year Y to items from the preceding two years, divided by the number of citable items in those two years.')

add_q(10, 'What constitutes a "citable item" in the denominator of the Journal Impact Factor?',
      ['Original research articles and review papers',
       'Editorials, letters to the editor, corrections, and obituaries',
       'Conference advertisement flyers printed in the back of the issue',
       'Table of contents and cover page graphics'],
      0,
      'Clarivate defines citable items primarily as substantive scholarly contributions: research articles and reviews.')

add_q(10, 'What is the "i10-index" popularized by Google Scholar?',
      ['The number of academic publications by an author with at least 10 citations each',
       'The number of papers published in the last 10 months',
       'The number of publications with more than 10 co-authors',
       'The researcher\'s h-index multiplied by 10'],
      0,
      'Google Scholar defines i10-index as the number of publications with at least 10 citations.')

add_q(10, 'What is the primary objective of "Altmetrics" in assessing research impact?',
      ['To capture non-traditional, real-time attention and engagement across online platforms (policy documents, news outlets, social media, Mendeley)',
       'To compute alternative font metrics in LaTeX typography',
       'To calculate the physical mass of printed research journals',
       'To replace peer-reviewed publication with personal video streams'],
      0,
      'Altmetrics track mentions across mainstream media, policy briefs, blog posts, Wikipedia, and social networks.')

add_q(10, 'State whether True or False: Cross-field comparisons of raw Journal Impact Factors (e.g., comparing Mathematics to Molecular Oncology) are scientifically valid without normalization.',
      ['True', 'False'],
      1,
      'False. Citation rates and publication volumes vary enormously across disciplines; raw impact factors cannot be directly compared without normalization.')

add_q(10, 'What is the San Francisco Declaration on Research Assessment (DORA)?',
      ['A global initiative advocating that journal-based metrics like JIF should not be used as surrogate measures of the quality of individual research articles or individual researchers',
       'A military treaty governing scientific satellite navigation',
       'A declaration mandating that all scientific papers be written in French',
       'A standard specifying minimum paper page lengths for PhD theses'],
      0,
      'DORA emphasizes evaluating scientific work on its own merits rather than through journal impact factor proxies.')

out_path = r'd:\Interview\SAA\NPTEL\quiz_data\m01_10.json'
with open(out_path, 'w', encoding='utf-8') as f:
    json.dump(questions, f, indent=2)

print(f'Successfully generated {len(questions)} questions for Modules 1 to 10 in {out_path}')
