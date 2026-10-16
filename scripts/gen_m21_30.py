# -*- coding: utf-8 -*-
import json
import os

questions = []

def add_q(mod_id, q_text, options, answer, exp, q_type='single', passage=None):
    questions.append({
        'id': 200 + len(questions) + 1,
        'module': mod_id,
        'type': q_type,
        'question': q_text,
        'options': options,
        'answer': answer,
        'explanation': exp,
        'passage': passage
    })

# MODULE 21: Safety in the Laboratory & Hazard Protocols (Lecture 21)
add_q(21, 'What is the primary document containing essential safety, handling, health hazard, and emergency spill procedures for any chemical reagent used in a research lab?',
      ['Safety Data Sheet (SDS) / Material Safety Data Sheet (MSDS)',
       'The vendor’s commercial sales invoice',
       'The user’s personal laboratory notebook',
       'A standard university examination syllabus'],
      0,
      'The SDS (or MSDS) provides comprehensive hazard ratings, toxicity data, first-aid measures, protective gear guidelines, and disposal protocols.')

add_q(21, 'When handling compressed gas cylinders in a laboratory, what is the single most critical safety requirement regarding their physical restraint?',
      ['They must always be securely chained or strapped to a wall or dedicated cylinder rack at all times, whether full or empty',
       'They should be freely rolled horizontally across the laboratory floor',
       'They should be balanced vertically on wooden chairs near doorways',
       'They must be left unstrapped to allow rapid evacuation during an earthquake'],
      0,
      'High-pressure gas cylinders can become dangerous projectile missiles if knocked over and their valve shears; secure chaining is mandatory.')

add_q(21, 'Which class of Personal Protective Equipment (PPE) is non-negotiable for anyone entering a wet chemical or experimental synthesis laboratory?',
      ['Safety glasses/goggles, lab coat, closed-toe shoes, and appropriate chemical-resistant gloves',
       'Open-toed sandals and shorts for rapid heat dissipation',
       'Cloth sunglasses and baseball caps',
       'Loose synthetic scarves and jewelry'],
      0,
      'Standard PPE includes eye protection, splash-resistant lab coats, closed-toe footwear, and application-specific protective gloves.')

add_q(21, 'What is the golden rule for diluting concentrated acid with water?',
      ['Always add acid to water slowly with constant stirring (AAA: Always Add Acid); NEVER add water to concentrated acid',
       'Always pour water rapidly into concentrated acid to quench the heat immediately',
       'Boil the acid first before mixing it with cold water',
       'Pour both liquids simultaneously from equal heights into a narrow flask'],
      0,
      'Adding water to concentrated acid generates violent exothermic boiling and localized steam explosions that splatter corrosive acid.')

add_q(21, 'State whether True or False: In a research laboratory, it is perfectly acceptable to store personal lunch boxes and drinks inside a chemical refrigerator as long as food is placed in sealed plastic containers.',
      ['True', 'False'],
      1,
      'False. Storing food or beverages in laboratory chemical refrigerators is strictly prohibited due to severe risks of toxic contamination and chemical vapor absorption.')

add_q(21, 'What is the primary operational purpose of a chemical fume hood?',
      ['To capture, contain, and exhaust hazardous, toxic, or volatile chemical fumes and vapors away from the researcher\'s breathing zone',
       'To serve as permanent long-term storage shelving for empty glass beakers',
       'To dry wet clothing and umbrellas after raining',
       'To heat the laboratory room during winter months'],
      0,
      'Fume hoods maintain inward aerodynamic airflow to exhaust toxic vapors, aerosols, and volatile chemicals safely away from laboratory workers.')

add_q(21, 'What does the acronym PASS stand for when operating a portable fire extinguisher?',
      ['Pull the pin, Aim at the base of the fire, Squeeze the lever, Sweep from side to side',
       'Push the button, Activate alarm, Shout loudly, Step back',
       'Point at flames, Apply pressure, Spray upward, Stop breathing',
       'Prepare water, Alert supervisor, Shut doors, Seek cover'],
      0,
      'PASS is the standard fire safety acronym: Pull pin, Aim at base, Squeeze trigger, and Sweep across fire.')

add_q(21, 'Which fire extinguisher type is appropriate for extinguishing an electrical equipment fire (Class C) in an electronics or computer research laboratory?',
      ['Carbon Dioxide (CO2) or Clean Agent / Dry Chemical extinguisher',
       'Pressurized water stream extinguisher',
       'Wet chemical foam bucket',
       'Sand bucket filled with wet garden soil'],
      0,
      'CO2 or clean gas agents extinguish electrical fires without conducting electric current or damaging sensitive electronic circuits.')

add_q(21, 'What is the standard emergency action if a hazardous corrosive chemical splashes directly into a researcher’s eyes?',
      ['Immediately flush eyes at an emergency eyewash station for at least 15 continuous minutes with eyelids held wide open, then seek emergency medical care',
       'Gently rub eyes with paper towels and wait 10 minutes to see if irritation stops',
       'Apply commercial eye cosmetics to neutralize the chemical',
       'Blow hot air from a hairdryer into the face'],
      0,
      'Immediate continuous flushing with clean water for a minimum of 15 minutes is vital to prevent irreversible corneal and ocular chemical burns.')

add_q(21, 'What is the purpose of an institutional Chemical Hygiene Plan (CHP)?',
      ['A comprehensive written program outlining standard laboratory operating procedures, hazard identification, waste disposal, and emergency responses',
       'A schedule for cleaning dormitory bathrooms on campus',
       'A list of prices for purchasing chemical reagents from international suppliers',
       'A commercial brochure advertising university chemistry degrees to high school students'],
      0,
      'The Chemical Hygiene Plan defines institutional policies, procedures, and responsibilities for protecting personnel from lab chemical hazards.')

# MODULE 22: Technical Presentations & Scientific Slides (Lecture 22)
add_q(22, 'According to guidelines for effective scientific slide presentations, what is the recommended rule of thumb regarding text density on a slide?',
      ['Keep slides uncluttered: follow the "6x6 rule" (around 6 bullet points, max 6 words per line) and prioritize high-quality diagrams over text walls',
       'Copy complete paragraphs from your published paper word-for-word onto every slide in 10pt font',
       'Use at least 15 different bright rainbow text colors to keep the audience entertained',
       'Fill every square inch of slide background with intricate animated textures'],
      0,
      'Effective technical presentations prioritize legibility, visual diagrams, and concise key phrases over dense blocks of text.')

add_q(22, 'What is the primary role of the speaker during a conference slide presentation?',
      ['To explain, contextualize, and tell the compelling scientific story behind the visuals, rather than merely reading text off the screen',
       'To turn their back to the audience and read every word directly from the projection screen',
       'To speak as quickly as possible to pack 80 slides into a 10-minute slot',
       'To recite textbook definitions without mentioning the paper’s new findings'],
      0,
      'Slides are visual aids; the speaker’s role is to engage the audience, highlight key insights, and explain the significance of the data.')

add_q(22, 'When presenting graphs and charts on slides, what is an essential requirement for clarity?',
      ['Large, legible axis labels, clearly defined units, distinguishable data curves, and explicit legend/callouts',
       'Removing all numbers and axis labels to keep the graph aesthetically minimalist',
       'Using 3D tilted pie charts with reflective shadows for 2-variable linear datasets',
       'Displaying raw, unformatted Excel spreadsheets containing hundreds of unrounded decimals'],
      0,
      'Scientific graphs must have clear labels, legible font sizes readable from the back of the auditorium, and explicitly indicated measurement units.')

add_q(22, 'What is the recommended average presentation pace for a technical research conference talk?',
      ['Approximately 1 to 1.5 minutes per slide (e.g., 10 to 14 slides for a 15-minute presentation)',
       '10 seconds per slide (presenting 90 slides in 15 minutes)',
       '10 minutes per slide (presenting only 1 slide for an entire keynote lecture)',
       'Pace does not matter as long as animations trigger sound effects'],
      0,
      'A steady pace of 1 to 1.5 minutes per slide ensures sufficient time to explain context, methodology, data, and conclusions without rushing.')

add_q(22, 'State whether True or False: In a technical presentation, using elaborate animated slide transitions and flying text effects enhances scientific credibility.',
      ['True', 'False'],
      1,
      'False. Flamboyant animations and noisy transitions distract audiences and are widely considered unprofessional in scientific conferences.')

add_q(22, 'What is the function of the "Take-Home Message" or Conclusion slide at the end of a research presentation?',
      ['To clearly articulate 2 to 3 main conclusions, practical implications, and the broader significance of the research',
       'To display a generic clipart image saying "Thank You" with no scientific content',
       'To list every single measurement point collected over five years of laboratory work',
       'To provide an unformatted list of 50 literature references cited in the introduction'],
      0,
      'The conclusion slide should leave the audience with a memorable, concise summary of the key findings and their broader impact.')

add_q(22, 'How should a researcher prepare for the Question & Answer (Q&A) session following a conference presentation?',
      ['Anticipate tough methodological questions, prepare supplementary backup slides with extra details, and listen carefully before answering politely',
       'Argue aggressively with any audience member who asks for clarification',
       'Pretend not to hear questions from renowned senior professors',
       'Leave the auditorium immediately as soon as the final slide finishes'],
      0,
      'Preparing backup slides with detailed parameter tables, sensitivity analyses, or calibration plots enables confident, constructive Q&A handling.')

add_q(22, 'Why is high color contrast (e.g., dark text on a light background or clean light text on a dark background) crucial for slides?',
      ['Conference projectors often have lower contrast and brightness than laptop screens, making low-contrast text (e.g., yellow on white) unreadable',
       'High contrast reduces the file size of PowerPoint presentations',
       'Conference organizers automatically disqualify presentations that use dark text',
       'High contrast speeds up the refresh rate of liquid crystal displays'],
      0,
      'Auditorium projectors frequently wash out colors; robust contrast ensures readability under varying ambient room lighting.')

add_q(22, 'What is the "Rule of Thirds" or visual hierarchy in slide design?',
      ['Structuring elements logically so that the audience’s eye naturally focuses on the most critical message, title, or graphic first',
       'Dividing the slide into three equal paragraphs of text',
       'Giving three copies of the presentation slides to the session chair',
       'Inviting three co-authors to speak simultaneously at the podium'],
      0,
      'Visual hierarchy uses font scale, placement, and whitespace to guide viewer attention directly to primary findings.')

add_q(22, 'When citing prior works or comparative data on presentation slides, how should citations be formatted?',
      ['Brief in-text attribution at the bottom corner of the slide (e.g., Smith et al., ACS Nano 2023)',
       'Full 5-line bibliographic citations including complete abstract and author addresses across the center of the slide',
       'No citation should ever be shown because conference slides do not require attribution',
       'Citations should be read aloud in their entirety by the speaker for 3 minutes'],
      0,
      'Slide citations should be concise bottom-corner references providing sufficient details for interested listeners to locate the paper.')

# MODULE 23: Technical Writing: Structure of Journal Articles (Lecture 23)
add_q(23, 'What does the standard IMRAD structure in scientific journal articles stand for?',
      ['Introduction, Methods, Results, And Discussion',
       'Index, Manuscript, Review, Appendix, Document',
       'Investigation, Measurement, Reasoning, Analysis, Deduction',
       'Initial Model, Realization, Algorithm, Demonstration'],
      0,
      'IMRAD is the universally recognized organizational framework for empirical research manuscripts across science and engineering.')

add_q(23, 'What is the primary rhetorical goal of the "Introduction" section in an IMRAD paper?',
      ['To establish the broad problem context, review relevant literature, identify a specific gap, and clearly state the study’s objective or hypothesis',
       'To present all raw numerical measurement tables collected during experiments',
       'To thank funding agencies and acknowledge lab technicians',
       'To describe the personal biography and career journey of the primary author'],
      0,
      'The Introduction moves from a general domain problem to previous findings, identifies a knowledge gap, and states the research objective.')

add_q(23, 'What is the primary requirement for the "Methods" (or Materials and Methods) section of a scientific manuscript?',
      ['Reproducibility: providing sufficient operational detail that an independent competent researcher could replicate the study exactly',
       'Writing in rhyming verse to make technical protocols entertaining',
       'Concealing critical reagent concentrations and furnace temperatures as proprietary secrets',
       'Describing only the experiments that yielded perfectly expected results'],
      0,
      'The Methods section must provide complete, rigorous procedural specifications to guarantee scientific reproducibility.')

add_q(23, 'What is the crucial difference between the "Results" section and the "Discussion" section in a journal paper?',
      ['Results objectively present the observed data, trends, and statistical findings; Discussion interprets the meaning, mechanisms, limitations, and significance of those findings',
       'Results contain equations; Discussion contains only photographs',
       'Results are written by students; Discussion is written by the journal editor',
       'Results must be speculative; Discussion must be purely factual tables'],
      0,
      'Results state what was observed without editorial spin; Discussion explains why it happened, links data to existing literature, and explores implications.')

add_q(23, 'State whether True or False: In the "Results" section of an IMRAD paper, you should duplicate every single numerical value from a large table into the running text body.',
      ['True', 'False'],
      1,
      'False. Text should highlight overarching trends, major anomalies, and significant comparisons, referring the reader to tables/figures for comprehensive details.')

add_q(23, 'What is an "Abstract" in a scientific paper, and what is its typical word count limit?',
      ['A standalone, comprehensive summary of the problem, methodology, major results, and primary conclusion, typically restricted to 150 to 250 words',
       'An introductory greeting letter addressed to the journal’s Editor-in-Chief',
       'A 10-page detailed mathematical derivation appended to the manuscript',
       'An alphabetical glossary defining standard engineering terms'],
      0,
      'The Abstract provides a concise, standalone synopsis covering background, problem, approach, key findings, and significance.')

add_q(23, 'Which of the following is considered best practice when composing the "Title" of a scientific research paper?',
      ['Informative, specific, concise, and accurately reflecting the primary finding or subject of the study without unnecessary fluff',
       'Extremely generic and ambiguous, such as "Studies on Some Interesting Properties of Materials"',
       'Over 50 words in length containing jokes and colloquial slang',
       'Formulated to mislead readers into thinking the paper addresses an entirely different scientific field'],
      0,
      'A strong title is concise, descriptive, includes relevant keywords for search indexing, and accurately captures the central discovery.')

add_q(23, 'What information must be included in the "Acknowledgements" section of a journal publication?',
      ['Funding grants (with exact grant numbers), non-author technical/facility assistance, and institutional infrastructural support',
       'The names of all high school teachers the author ever had',
       'Complaints regarding laboratory maintenance delays',
       'Personal advertisements for selling second-hand textbooks'],
      0,
      'Acknowledgements formally credit funding agencies, grant numbers, shared instrumentation facilities, and individuals providing technical assistance.')

add_q(23, 'What is the role of the "Literature Review" subsection within the Introduction of an article?',
      ['To critically synthesize prior work, establish the historical context, and justify why the current research is necessary and novel',
       'To list every paper ever written on the topic without any critical commentary',
       'To insult previous researchers for having inferior equipment',
       'To fill extra pages to meet minimum publisher thickness requirements'],
      0,
      'The literature review synthesizes prior achievements, illustrates limitations in current understanding, and motivates the present study.')

add_q(23, 'In scientific prose, which style characteristic is prized above all others?',
      ['Clarity, precision, conciseness, and logical coherence',
       'Flowery, metaphorical, and highly emotional vocabulary',
       'Excessive use of passive voice and confusing run-on sentences',
       'Ambiguity so that multiple contradictory interpretations remain valid'],
      0,
      'Scientific writing prioritizes utmost clarity, objective precision, logical structure, and parsimonious language.')

# MODULE 24: Creativity in Research: Lateral Thinking (Part 1 - Lecture 24)
add_q(24, 'Who coined the term "Lateral Thinking" to describe solving problems through an indirect and creative approach?',
      ['Edward de Bono', 'Karl Popper', 'Thomas Kuhn', 'Isaac Newton'],
      0,
      'Edward de Bono introduced Lateral Thinking in 1967, contrasting it with traditional step-by-step vertical thinking.')

add_q(24, 'How does "Lateral Thinking" differ fundamentally from "Vertical (Linear) Thinking"?',
      ['Vertical thinking is analytical, sequential, and moves only in directionally proven paths; Lateral thinking explores multiple unconventional pathways and rearranges patterns',
       'Vertical thinking is only used for building skyscrapers; lateral thinking is used for digging tunnels',
       'Vertical thinking does not involve logic; lateral thinking involves only mathematics',
       'Lateral thinking requires computer algorithms; vertical thinking is done on paper'],
      0,
      'Vertical thinking develops established ideas logically step-by-step; lateral thinking deliberately restructures concepts to uncover new perspectives.')

add_q(24, 'In creative research, what is a "Paradigm Shift" as described by Thomas Kuhn in scientific philosophy?',
      ['A fundamental change in the basic concepts and experimental practices of a scientific discipline (e.g., Newtonian mechanics to Quantum relativity)',
       'Moving laboratory desks from one side of the room to the other',
       'Switching from blue pens to black pens when writing equations',
       'A regular annual revision of university tuition fees'],
      0,
      'Kuhn described paradigm shifts as scientific revolutions where an existing foundational worldview is overturned by a radically new framework.')

add_q(24, 'What is "Functional Fixedness" in experimental problem solving, and why is it an obstacle to innovation?',
      ['A cognitive bias that limits a person to using an object or tool only in the traditional way it is conventionally used',
       'A mechanical failure of a motor due to lack of lubricating oil',
       'The permanent setting of concrete after 24 hours of curing',
       'A rigid rule that laboratory safety glasses must always be worn'],
      0,
      'Functional fixedness blinds researchers to alternative applications of tools, mechanisms, or materials beyond their conventional roles.')

add_q(24, 'State whether True or False: In the creative ideation phase of research, premature critical judgment and immediate dismissal of unusual ideas stimulates breakthrough thinking.',
      ['True', 'False'],
      1,
      'False. Premature evaluation suppresses creative risk-taking; effective ideation separates divergent idea generation from convergent critical filtering.')

add_q(24, 'What is "Divergent Thinking" in the creative process?',
      ['Generating a broad range of diverse, novel ideas, possibilities, and hypotheses for an open-ended problem',
       'Narrowing down a list of options to select the single mathematically optimal solution',
       'Thinking about mathematical divergence in vector calculus exclusively',
       'Disagreeing aggressively with thesis committee members during an oral defense'],
      0,
      'Divergent thinking expands outward to produce numerous varied possibilities, while convergent thinking narrows down to the best solution.')

add_q(24, 'What does the term "Serendipity" mean in scientific discovery (e.g., Alexander Fleming discovering penicillin)?',
      ['Finding valuable or agreeable discoveries not sought for, made by a prepared mind observing accidental or unexpected phenomena',
       'Systematically executing a 10-step protocol without any deviations',
       'Fabricating experimental data to match published theory',
       'Applying for government research grants using commercial software'],
      0,
      'Pasteur noted: "Chance favors the prepared mind." Serendipity is capitalizing on unexpected accidental anomalies through insightful observation.')

add_q(24, 'Which creative problem-solving technique involves identifying analogies between biological systems and engineering challenges (e.g., designing aerodynamic bullet trains based on the kingfisher’s beak)?',
      ['Biomimetics / Biomimicry',
       'Synthetic organic chemistry',
       'Finite element stress analysis',
       'Thermodynamic cycle analysis'],
      0,
      'Biomimetics studies nature\'s time-tested designs, mechanisms, and biological systems to inspire innovative engineering solutions.')

add_q(24, 'What is the role of "Incubation" in the four-stage model of creativity (Preparation, Incubation, Illumination, Verification)?',
      ['A period where the unconscious mind processes problems and associations while the researcher is engaged in other unrelated activities or rest',
       'Keeping bacterial cultures in a heated laboratory oven at 37°C',
       'Writing the introduction section of a PhD thesis within 24 hours',
       'Purchasing experimental glassware from chemical supply warehouses'],
      0,
      'Wallas’s creativity model identifies incubation as a period where unconscious cognitive processing allows latent connections to emerge.')

add_q(24, 'What is the technique of "Provocation and Movement" (PO) in lateral thinking?',
      ['Introducing a deliberately absurd, impossible, or provocative statement to jolt thought out of established patterns and discover new avenues',
       'Physically pushing colleagues in the hallway to make them walk faster',
       'Challenging the university president to an athletic contest',
       'Setting off the laboratory fire alarm to test evacuation readiness'],
      0,
      'De Bono’s PO (Provocative Operation) uses intentional conceptual disruptions to bypass entrenched mental models and generate innovative alternatives.')

# MODULE 25: Creativity in Research: TRIZ & Problem Solving (Part 2 - Lecture 25)
add_q(25, 'What does the Russian acronym TRIZ stand for in engineering innovation methodology (developed by Genrich Altshuller)?',
      ['Teoriya Resheniya Izobretatelskikh Zadatch (Theory of Inventive Problem Solving)',
       'Technical Research and Industrial Zoning',
       'Total Reliability in Zero-defect Manufacturing',
       'Thermal Radiation and Ionization Zone'],
      0,
      'TRIZ was developed by Altshuller based on analyzing hundreds of thousands of patents to extract universal principles of invention.')

add_q(25, 'According to TRIZ philosophy, what is the core source of an engineering challenge that requires an inventive solution rather than a trade-off compromise?',
      ['A Contradiction (technical or physical contradiction where improving one parameter worsens another)',
       'A lack of sufficient research funding from government sponsors',
       'A breakdown of the computer operating system during data processing',
       'A disagreement between the student and the laboratory technician'],
      0,
      'TRIZ identifies contradictions as the heart of inventive challenges: resolving contradictions without compromising yields breakthrough inventions.')

add_q(25, 'In TRIZ, how many "Inventive Principles" were distilled by Altshuller from historical patent patterns to resolve technical contradictions?',
      ['40 Inventive Principles', '7 Habits of Innovation', '10 Commandments of Design', '100 Golden Rules'],
      0,
      'Altshuller identified 40 fundamental inventive principles (e.g., Segmentation, Taking Out, Asymmetry, Cushion in Advance).')

add_q(25, 'What is the "Ideality" or "Ideal Final Result" (IFR) in TRIZ methodology?',
      ['A system that delivers all useful functions with zero cost, zero space, and zero harmful side-effects (Ideality = Benefits / (Costs + Harm))',
       'A finished PhD dissertation bound in dark blue leather with gold lettering',
       'An experiment that runs in zero seconds without consuming electricity',
       'A conference paper accepted without any revisions by reviewers'],
      0,
      'The Ideal Final Result is a theoretical target where system benefits are maximized while costs and harmful elements vanish toward zero.')

add_q(25, 'Which TRIZ Inventive Principle is illustrated by replacing a solid uniform drill bit with a hollow coring bit that extracts only the outer circumference?',
      ['Principle 1: Segmentation (or Taking Out / Void)',
       'Principle 35: Parameter Changes',
       'Principle 18: Mechanical Vibration',
       'Principle 28: Replacement of Mechanical System'],
      0,
      'Segmentation and Taking Out extract only the functional material or divide structures to achieve functions with minimal mass and friction.')

add_q(25, 'State whether True or False: In TRIZ, a "Physical Contradiction" occurs when a single parameter must simultaneously possess two mutually opposing physical states (e.g., a tool must be hot to melt solder, but cold to avoid burning components).',
      ['True', 'False'],
      0,
      'True. Physical contradictions require an attribute to be both A and non-A; TRIZ resolves them through separation in time, space, condition, or scale.')

add_q(25, 'How does TRIZ recommend resolving a physical contradiction where a material must be flexible during assembly but rigid during operation?',
      ['Separation in Time (flexible at time t1, rigid at operational time t2, such as UV-cured polymers)',
       'Accepting a permanent compromise where the material is semi-flexible and performs both poorly',
       'Scrapping the engineering project and firing the design team',
       'Increasing the thickness until the assembly line jams'],
      0,
      'Separation principles (in time, space, or condition) eliminate physical contradictions without compromising functional performance.')

add_q(25, 'What is the "Contradiction Matrix" in classical TRIZ?',
      ['A 39x39 matrix mapping 39 engineering parameters against each other to identify which of the 40 inventive principles historically solved that conflict',
       'A matrix multiplying 3D stress tensors in finite element software',
       'A table listing contradictory statements made by peer reviewers',
       'A calendar grid tracking missed laboratory project deadlines'],
      0,
      'The Altshuller Contradiction Matrix cross-references 39 engineering parameters to suggest the most successful inventive principles.')

add_q(25, 'Which TRIZ principle involves performing required actions or changes to an object in advance before it is needed (e.g., pre-stressing rebar in reinforced concrete)?',
      ['Principle 10: Prior Action (Preliminary Action)',
       'Principle 2: Taking Out',
       'Principle 13: The Other Way Round',
       'Principle 29: Pneumatics and Hydraulics'],
      0,
      'Prior Action introduces pre-stressing, pre-heating, or preliminary conditioning before operational loads occur.')

add_q(25, 'What is the "S-Curve" analysis in technology evolution and TRIZ forecasting?',
      ['A model describing the lifecycle of a technology system through stages: birth, rapid growth, maturity, and eventual physical/economic limit',
       'A graphical plot of snake movement across desert sand',
       'A diagram showing the curvature of human spine while sitting at an office desk',
       'A curve depicting student exam score distributions over 12 weeks'],
      0,
      'S-curves map performance against time/investment, signaling when a technology reaches performance limits and demands a paradigm shift.')

# MODULE 26: Developing Creative Engineering Solutions
add_q(26, 'What is the primary objective of "Morphological Analysis" (developed by Fritz Zwicky) in engineering design?',
      ['Systematically exploring all possible combinations of multidimensional parameters and sub-solutions to generate novel system configurations',
       'Analyzing the external biological morphology of insects under a microscope',
       'Checking grammatical morphology and sentence syntax in a thesis draft',
       'Measuring the physical dimensions of laboratory workbenches'],
      0,
      'Morphological analysis breaks a complex system into dimensions/parameters and systematically explores the matrix of all combinations.')

add_q(26, 'In the design thinking process, what is the significance of the "Empathize" stage?',
      ['Deeply understanding the real needs, pain points, and behavioral contexts of end-users before defining solutions',
       'Expressing emotional sympathy to colleagues who failed their PhD qualifying exams',
       'Writing letters of apology to journal editors after missing revision deadlines',
       'Allowing lab equipment to rest during weekends to prevent wear'],
      0,
      'Empathize is the user-centric foundation of design thinking, ensuring engineers solve the right human problem.')

add_q(26, 'What does the SCAMPER creative brainstorming checklist acronym represent?',
      ['Substitute, Combine, Adapt, Modify/Magnify, Put to another use, Eliminate, Reverse/Rearrange',
       'Systematic Calculation And Mathematical Processing of Experimental Results',
       'Scientific Classification And Measurement of Physical Engineering Resources',
       'Standard Calibration And Maintenance Procedure for Electronic Radiometers'],
      0,
      'SCAMPER is an actionable ideation checklist developed by Bob Eberle to systematically prompt creative variations.')

add_q(26, 'What is "Root Cause Analysis" (RCA) using the "5 Whys" technique?',
      ['Iteratively asking "Why?" five times to drill past superficial symptoms to uncover the foundational cause of an engineering or system failure',
       'Asking five different professors the same question until one gives an easy answer',
       'Selecting five random components from a machine and replacing them',
       'Writing five paragraphs explaining why laboratory measurements were inaccurate'],
      0,
      'Sakichi Toyoda\'s 5 Whys technique drills past surface-level symptoms to reveal and fix systemic root causes.')

add_q(26, 'State whether True or False: In rapid prototyping, creating high-fidelity, expensive prototypes too early in the ideation cycle can stifle creative exploration and increase resistance to discarding flawed ideas.',
      ['True', 'False'],
      0,
      'True. Low-fidelity rapid prototypes encourage rapid learning, fearless iteration, and cheap failures before heavy capital investment.')

add_q(26, 'What is "Axiomatic Design" (introduced by Nam P. Suh) in engineering methodology?',
      ['A structured design framework based on two fundamental axioms: the Independence Axiom (maintain function independence) and the Information Axiom (minimize information content)',
       'A philosophy stating that all engineering designs must be derived from religious texts',
       'A design method where components are assembled without any fasteners or glue',
       'A software package used exclusively for drawing architectural blueprints'],
      0,
      'Axiomatic design uses the Independence Axiom (FRs remain independent) and Information Axiom (simplest design with maximum success probability).')

add_q(26, 'What is a "Coupled Design" in Suh’s Axiomatic Design framework?',
      ['A problematic design where modifying one design parameter unintentionally alters multiple functional requirements, violating the Independence Axiom',
       'A mechanical coupling connecting an electric motor shaft to a water pump',
       'A design produced collaboratively by two researchers working as a pair',
       'A system that operates only when two computers are linked via Wi-Fi'],
      0,
      'Coupled designs violate the Independence Axiom because adjusting one parameter disrupts other functions, leading to complex tuning difficulties.')

add_q(26, 'What is "Design for Six Sigma" (DFSS)?',
      ['A methodology for designing products and processes that achieve ultra-low defect rates (< 3.4 defects per million opportunities) from initial launch',
       'A requirement that all research teams must consist of exactly six graduate students',
       'A software tool that draws six concentric circles on engineering graphs',
       'A standard that limits laboratory work to six hours per day'],
      0,
      'DFSS designs quality directly into systems upfront using rigorous statistical tools to minimize variance and defects.')

add_q(26, 'What is the role of "Failure Mode and Effects Analysis" (FMEA) in creative engineering design?',
      ['A structured inductive procedure to identify potential failure modes, evaluate their severity, occurrence, and detectability, and prioritize corrective actions',
       'A method for celebrating project failures with laboratory pizza parties',
       'A post-mortem legal investigation conducted after a factory burns down',
       'A tool for calculating financial compensation for dismissed employees'],
      0,
      'FMEA calculates Risk Priority Numbers (RPN = Severity x Occurrence x Detection) to proactively engineer out vulnerabilities.')

add_q(26, 'How does "Cross-Pollination" of ideas from disparate scientific disciplines foster engineering breakthroughs?',
      ['By importing proven principles, analogies, and tools from one field into another where they are novel and transformative',
       'By planting flowering botanical gardens around engineering department buildings',
       'By forcing mechanical engineers to grade sociology undergraduate homework',
       'By translating engineering textbooks into ancient classical languages'],
      0,
      'Major innovations often occur at disciplinary intersections where concepts routine in one domain solve long-standing bottlenecks in another.')

# MODULE 27: Research Ethics, Academic Integrity & Fabrication (Lecture 27)
add_q(27, 'In research integrity and ethics, what are the "Big Three" forms of scientific misconduct (FFP)?',
      ['Fabrication, Falsification, and Plagiarism',
       'Failure, Frustration, and Procrastination',
       'Funding, Fellowship, and Promotion',
       'Formatting, Footnoting, and Pagination'],
      0,
      'FFP constitutes the internationally codified triad of serious research misconduct subject to severe academic sanctions.')

add_q(27, 'What is the precise definition of "Fabrication" in research ethics?',
      ['Making up data or results and recording or reporting them without actually conducting the research',
       'Manipulating research equipment or altering data points to support a desired conclusion',
       'Using another scholar\'s words without proper attribution',
       'Publishing a paper in a journal with an impact factor below 2.0'],
      0,
      'Fabrication is the complete invention of non-existent data, laboratory observations, or patient clinical records.')

add_q(27, 'What is the precise definition of "Falsification" in research ethics?',
      ['Manipulating research materials, equipment, or processes, or changing/omitting data or results such that the research is not accurately represented',
       'Translating foreign language articles without paying a professional translator',
       'Submitting a grant proposal one hour past the official deadline',
       'Using an open-source operating system in the laboratory'],
      0,
      'Falsification involves doctoring real records, cherry-picking flattering data, or altering micrographs to deceive reviewers.')

add_q(27, 'What is "Data Cherry-Picking" (data cooking / trimming)?',
      ['Selectively reporting only the data points that support one\'s favored hypothesis while discarding conflicting data without sound scientific justification',
       'Harvesting fresh fruit on agricultural research test plots',
       'Using statistical software that displays red and pink bar charts',
       'Choosing data with high numerical precision for printing in appendices'],
      0,
      'Cherry-picking conceals contradictory evidence, creating a false impression of reproducibility and scientific certainty.')

add_q(27, 'State whether True or False: Legitimate image processing (e.g., contrast adjustment of a microscopy image) is ethical ONLY if applied uniformly across the entire image and does not obscure, eliminate, or misrepresent any feature.',
      ['True', 'False'],
      0,
      'True. Linear adjustments across the entire field are acceptable if disclosed; selective cloning, erasing bands, or differential enhancements constitute fraud.')

add_q(27, 'What ethical requirement must be fulfilled before conducting research involving human participants?',
      ['Obtaining formal Institutional Review Board (IRB) / Ethics Committee clearance and secure informed consent from all participants',
       'Getting verbal approval from a fellow graduate student over lunch',
       'Publishing the participants’ names and personal phone numbers online',
       'Paying participants in cash without keeping receipts'],
      0,
      'Human studies require prior approval from an accredited ethics board (IRB/IEC) and voluntary, informed, documented consent.')

add_q(27, 'What was the landmark 1979 ethical declaration that established the foundational principles of Respect for Persons, Beneficence, and Justice for human research?',
      ['The Belmont Report',
       'The Magna Carta',
       'The Treaty of Versailles',
       'The Kyoto Protocol'],
      0,
      'The Belmont Report set ethical boundaries for human research following the unethical Tuskegee syphilis study.')

add_q(27, 'What does the principle of "Beneficence" mandate in experimental research ethics?',
      ['Maximizing potential societal/scientific benefits while minimizing foreseeable physical, psychological, or economic risks and harms to subjects',
       'Paying the maximum possible financial compensation to researchers',
       'Ensuring that research results are always positive and pleasing',
       'Exclusively researching topics that are guaranteed to win Nobel Prizes'],
      0,
      'Beneficence obligates investigators to do no harm, assess risk-benefit ratios, and safeguard participant well-being.')

add_q(27, 'What is a "Whistleblower" in the context of academic integrity?',
      ['An individual who reports suspected research misconduct, fraud, or safety violations to institutional authorities or regulatory oversight bodies',
       'A referee who officiates university football tournaments',
       'An electronic sensor that emits acoustic alarms when furnace temperatures exceed limits',
       'A computer virus that corrupts scientific simulation files'],
      0,
      'Whistleblowers report ethical breaches; institutions are legally and ethically obligated to protect them from retaliation.')

add_q(27, 'What is the standard consequence when published research is proven to contain fabricated or fraudulent data?',
      ['Formal Retraction of the article by the journal editor, public notification, and institutional disciplinary/termination proceedings',
       'Issuing a small typographic correction note thanking the author for trying',
       'Awarding the author extra research funding to repeat the experiment correctly',
       'Converting the article into a fictional novel for commercial bookstore sales'],
      0,
      'Fraudulent articles are formally retracted to cleanse the scientific literature, accompanied by disciplinary investigations.')

# MODULE 28: Plagiarism, Paraphrasing & Authorship Ethics (Lecture 28)
add_q(28, 'What is the formal definition of "Plagiarism" according to global research integrity standards?',
      ['The appropriation of another person\'s ideas, processes, results, or words without giving appropriate credit and attribution',
       'Disliking a published paper and writing a critical book review about it',
       'Using the same mathematical calculus symbols (e.g., dx/dt) as Isaac Newton',
       'Purchasing commercial software to conduct data analysis'],
      0,
      'Plagiarism is the uncredited use of another’s intellectual output, text, or concepts, presenting them as one\'s own.')

add_q(28, 'What constitutes "Self-Plagiarism" (Text Recycling / Duplicate Publication)?',
      ['Reusing significant portions of one\'s own previously published copyrighted text or data in a new manuscript without disclosure or proper citation',
       'Reading one\'s own published papers to review theoretical formulas',
       'Recycling scrap paper in the laboratory print room',
       'Writing a doctoral thesis that builds upon the scholar\'s own Master\'s coursework'],
      0,
      'Self-plagiarism deceives readers and publishers regarding novelty, breaches copyright agreements, and artificially inflates publication counts.')

add_q(28, 'What is "Salami Slicing" (Least Publishable Unit - LPU) in academic publishing?',
      ['Splitting a single cohesive, comprehensive research investigation into multiple thin, fragmented papers to artificially inflate publication counts',
       'Cutting food into thin slices during lunchtime in the student cafeteria',
       'Dividing an experimental silicon wafer into smaller microchips',
       'Partitioning a computer hard drive into five logical sectors'],
      0,
      'Salami publishing fragments scientific findings, wastes peer review resources, and clutters the literature with incomplete studies.')

add_q(28, 'What is "Ghost Authorship" in scientific manuscripts?',
      ['Omitting an individual who made substantial intellectual contributions to the research from the author list',
       'Adding the name of a deceased historical scientist to an author list',
       'Publishing a paper under a pseudonym to protect one\'s identity',
       'Submitting a paper written entirely by an automated chatbot without human review'],
      0,
      'Ghost authorship conceals true contributors (often industry-hired medical writers), undermining scholarly transparency.')

add_q(28, 'What is "Guest Authorship" (Honorary / Gift Authorship)?',
      ['Including an individual as an author who made no significant intellectual contribution, often due to their high status, seniority, or institutional position',
       'Inviting an external keynote speaker to present at a conference',
       'Listing an undergraduate student who washed lab beakers on the paper',
       'Offering free journal copies to campus library visitors'],
      0,
      'Gift authorship unethically awards academic credit to individuals who did not meet standard authorship criteria.')

add_q(28, 'According to the International Committee of Medical Journal Editors (ICMJE) criteria, which of the following is REQUIRED to qualify for authorship?',
      ['Substantial contributions to conception/design OR acquisition, analysis, or interpretation of data AND drafting/revising manuscript critically AND final approval AND accountability',
       'Merely providing general departmental supervision or laboratory bench space without reading the paper',
       'Solely providing commercial grant funding without intellectual involvement',
       'Checking the English spelling of the bibliography section'],
      0,
      'ICMJE requires 4 criteria: substantial intellectual contribution, drafting/revising, final approval, and mutual accountability.')

add_q(28, 'State whether True or False: Merely changing every third word using synonyms while retaining the exact sentence structure and argument of another author without quotation marks is acceptable academic paraphrasing.',
      ['True', 'False'],
      1,
      'False. This is "patchwriting" or mosaic plagiarism. True paraphrasing requires completely restating ideas in one\'s own voice with proper citation.')

add_q(28, 'What do similarity detection software tools (such as Turnitin or iThenticate) actually detect?',
      ['Exact textual matches and overlapping string sequences between the submitted document and existing databases/web pages; they do NOT judge intent or validity',
       'Whether the scientific experimental data is scientifically true or false',
       'Whether the researcher was feeling tired while writing the manuscript',
       'Whether the mathematical proofs contain arithmetic errors'],
      0,
      'Similarity tools find string matches; a human editor must interpret the report to distinguish legitimate citations from plagiarism.')

add_q(28, 'What is the role of the "Corresponding Author" on a multi-authored scientific manuscript?',
      ['Taking primary responsibility for managing journal communication during submission, peer review, proofs, and answering post-publication inquiries',
       'Paying the highest percentage of the publication fee from personal savings',
       'Writing letters to the editor of the city newspaper',
       'The author who lives closest to the publisher’s corporate headquarters'],
      0,
      'The corresponding author orchestrates communication with the journal, handles administrative logistics, and archives original data.')

add_q(28, 'When using verbatim (word-for-word) text from another publication, what two elements are mandatory to avoid plagiarism?',
      ['Enclosing the text in quotation marks (or block quote formatting) AND providing an explicit reference citation with page number',
       'Translating the words into French and omitting the author\'s name',
       'Changing the font size to 8pt and deleting all capital letters',
       'Adding the word "Allegedly" before the copied sentence'],
      0,
      'Direct quotes require both enclosing quotation marks (to signal non-original wording) and exact citation attribution.')

# MODULE 29: Intellectual Property: Patents, Copyrights & Designs (Lecture 29)
add_q(29, 'What are the three fundamental statutory criteria an invention must satisfy to be eligible for a Patent?',
      ['Novelty (new), Inventive Step (non-obvious), and Industrial Applicability (utility)',
       'Beauty, Complexity, and Expensive manufacturing cost',
       'Theoretical purity, Absence of math, and High page count',
       'Popular acclaim, Endorsement by celebrities, and Secret formulas'],
      0,
      'Patent laws worldwide mandate that an invention must be novel, non-obvious to a person skilled in the art, and industrially useful.')

add_q(29, 'What is the standard duration (term) of patent protection granted for an invention under the WTO TRIPS agreement?',
      ['20 years from the filing date of the patent application',
       '5 years from the grant date',
       '50 years after the death of the inventor',
       'Perpetual protection with zero expiration date'],
      0,
      'Under the WTO TRIPS agreement, utility patents provide exclusive protection for 20 years from the initial filing date.')

add_q(29, 'What is the fundamental "Social Contract" or Grand Bargain underlying the patent system?',
      ['The inventor is granted a temporary legal monopoly (exclusive right) in exchange for disclosing the full technical details of the invention to the public',
       'The government confiscates all inventions and distributes them free to foreign companies',
       'Inventors must pay 90% of their business profits to the patent office in cash',
       'Inventors are exempted from paying income taxes for their entire lifetime'],
      0,
      'Society grants a 20-year exclusive commercial right; in return, the inventor enables public knowledge by fully disclosing the technology.')

add_q(29, 'What does "Copyright" protect in intellectual property law?',
      ['The original expression of ideas fixed in a tangible medium (literary, artistic, musical, software code); it does NOT protect underlying ideas or facts',
       'The abstract mathematical concept of addition and subtraction',
       'The functional mechanical operation of internal combustion engines',
       'The physical trademark logo printed on soda cans'],
      0,
      'Copyright protects the specific tangible expression, not the underlying ideas, functional concepts, or scientific principles.')

add_q(29, 'What is a "Trade Secret" (e.g., the formula for Coca-Cola or proprietary chemical recipes)?',
      ['Confidential business/technical information that provides competitive advantage and is actively kept secret, lasting as long as confidentiality is maintained',
       'A patent that has been registered with the government under seal',
       'An open-source software project hosted on GitHub',
       'A scientific paper published in an open-access journal'],
      0,
      'Trade secrets require no government filing and last indefinitely, provided the owner takes reasonable measures to preserve secrecy.')

add_q(29, 'What does an "Industrial Design" right (Design Patent) protect in intellectual property?',
      ['The ornamental, aesthetic, or visual appearance and shape of a functional product (not its functional mechanical operation)',
       'The internal thermodynamic efficiency of a turbine blade',
       'The mathematical software code compiled inside an electronic controller',
       'The chemical composition of a pharmaceutical tablet'],
      0,
      'Design rights protect aesthetic and visual appearance (lines, contours, colors, packaging shape), rather than technical utility.')

add_q(29, 'State whether True or False: In most patent jurisdictions (including India and the European Patent Office), a pure mathematical algorithm or abstract scientific discovery without technical apparatus cannot be patented.',
      ['True', 'False'],
      0,
      'True. Abstract mathematical formulas, natural scientific laws, and pure business schemes are excluded from patentability.')

add_q(29, 'What is a "Trademark"?',
      ['A recognizable sign, design, phrase, or logo that identifies and distinguishes the commercial source of goods/services of one enterprise from others',
       'A physical mark left on a metal piece by an automated milling machine',
       'A scientific trade catalog published by chemical reagent vendors',
       'The watermark embedded inside currency banknotes'],
      0,
      'Trademarks safeguard brand identity and prevent consumer confusion regarding commercial provenance.')

add_q(29, 'What is "Freedom to Operate" (FTO) analysis in product development and R&D?',
      ['A comprehensive legal search to verify that commercializing a new technology will not infringe upon active patents held by third parties',
       'The legal right of university students to enter the laboratory outside normal hours',
       'An exemption allowing non-profit research institutes to ignore all patent laws',
       'The right of scientists to choose their preferred computer operating system'],
      0,
      'FTO assesses infringement risk, ensuring that manufacturing or selling a product will not trigger lawsuits from active patent holders.')

add_q(29, 'In India, under Section 3(d) of the Indian Patents Act, what is excluded from patentability in pharmaceutical and chemical inventions?',
      ['The mere discovery of a new form of a known substance which does not result in the enhancement of the known efficacy of that substance',
       'Any medicine that costs more than 100 rupees to manufacture',
       'Medicines derived from natural herbal plant extracts',
       'Synthetic vaccines designed using computer modeling'],
      0,
      'Section 3(d) prevents "evergreening" by disallowing patents on trivial tweaks to known molecules unless substantial efficacy enhancement is proven.')

# MODULE 30: Prior Art Search, Patent Claims & Filing Procedures (Lecture 30)
add_q(30, 'In patent law, what does the term "Prior Art" encompass?',
      ['Any public knowledge, published literature, patents, demonstrations, or commercial sales existing anywhere in the world prior to the filing/priority date',
       'Ancient paintings created during the Renaissance era in Europe',
       'Confidential, unpublished personal notes kept locked in a private desk drawer',
       'Textbooks published exclusively within the inventor\'s home city'],
      0,
      'Prior art includes all publicly available information globally that could invalidate the novelty or non-obviousness of a patent claim.')

add_q(30, 'What is the most critical and legally binding section of a patent specification that defines the exact scope of legal monopoly protection?',
      ['The Claims section',
       'The Abstract summary',
       'The Background description',
       'The Brief Description of Drawings'],
      0,
      'The Claims define the legal boundaries ("metes and bounds") of the exclusive property rights; what is not claimed is surrendered to the public.')

add_q(30, 'What is the difference between an "Independent Claim" and a "Dependent Claim" in a patent application?',
      ['An independent claim stands alone and sets out the broadest core invention; a dependent claim refers back to and narrows another claim by adding specific limitations',
       'Independent claims are filed by individuals; dependent claims are filed by corporations',
       'Independent claims expire in 10 years; dependent claims expire in 20 years',
       'Independent claims do not require review by patent examiners'],
      0,
      'Independent claims define the essential invention broadly; dependent claims provide fallback positions by incorporating narrower embodiments.')

add_q(30, 'What does the international Patent Cooperation Treaty (PCT) provide to inventors?',
      ['A unified, streamlined procedure for filing a single international patent application to preserve priority rights across more than 150 contracting member states',
       'A single international patent that automatically grants immediate global patent protection worldwide without national phase entry',
       'Free patent examination without charging any legal or processing fees',
       'An international court that automatically arrests copyright infringers'],
      0,
      'The PCT establishes a unified filing procedure and provides a 30/31-month window to seek national patents across member nations.')

add_q(30, 'What is a "Provisional Patent Application", and what is its strategic advantage for academic researchers?',
      ['A quick, cost-effective initial filing that establishes an official priority filing date, giving the inventor 12 months to file the complete specification',
       'A permanent patent granted automatically within 24 hours of filing',
       'An informal letter to a patent attorney that requires no technical documentation',
       'A patent application that remains valid for only 30 days before mandatory withdrawal'],
      0,
      'Provisional applications secure an early priority date quickly, giving inventors 12 months to finalize experiments before submitting full claims.')

add_q(30, 'State whether True or False: If a researcher publishes their invention in an open scientific conference paper BEFORE filing a patent application, the paper destroys the novelty of the invention in absolute novelty jurisdictions.',
      ['True', 'False'],
      0,
      'True. In countries without grace periods, public disclosure before filing constitutes prior art against oneself, permanently destroying novelty.')

add_q(30, 'What is the "Person Having Ordinary Skill in the Art" (PHOSITA) standard used by patent examiners?',
      ['A hypothetical legal benchmark person who possesses average technical knowledge and standard capabilities in the specific domain to evaluate obviousness',
       'A world-renowned Nobel Laureate with unparalleled genius in the field',
       'A non-technical consumer with zero scientific training',
       'The senior patent examiner managing the government intellectual property office'],
      0,
      'Non-obviousness is judged against a hypothetical practitioner with ordinary skill in the art—neither a genius nor an untrained layperson.')

add_q(30, 'What is the Cooperative Patent Classification (CPC) system used by major patent offices (USPTO and EPO)?',
      ['A hierarchical classification system of alphanumeric codes organizing technical subject matter into fine-grained technology buckets to facilitate prior art searching',
       'A grading scale used to evaluate the financial profitability of startup companies',
       'A code used by international customs officers to track counterfeit electronics',
       'A computer programming language used exclusively by patent attorneys'],
      0,
      'The CPC organizes technology into detailed hierarchical classes (A through H, and Y) to enable precise prior art searches.')

add_q(30, 'What is "Doctrine of Equivalents" in patent infringement law?',
      ['A legal doctrine holding that an accused product infringes a claim if it performs substantially the same function in substantially the same way to achieve the same result',
       'A rule stating that all patents granted in the same year have equal monetary value',
       'A requirement that patent attorneys must hold equivalent degrees in law and science',
       'A treaty ensuring that all member countries charge equivalent patent filing fees'],
      0,
      'The Doctrine of Equivalents prevents copycats from evading literal patent claims through insubstantial or trivial substitutions.')

add_q(30, 'What is an "Office Action" issued by a patent office during patent prosecution?',
      ['An official written communication from the patent examiner rejecting, objecting to, or querying specific claims or procedural aspects of the application',
       'A physical inspection of the inventor\'s laboratory by armed police officers',
       'A marketing brochure sent to corporate investors to sell patent licenses',
       'A certificate marking the final granting of the patent title'],
      0,
      'An Office Action details the examiner\'s prior art objections and rejections, requiring the applicant to submit amendments or counterarguments.')

out_path = r'd:\Interview\SAA\NPTEL\quiz_data\m21_30.json'
with open(out_path, 'w', encoding='utf-8') as f:
    json.dump(questions, f, indent=2)

print(f'Successfully generated {len(questions)} questions for Modules 21 to 30 in {out_path}')
