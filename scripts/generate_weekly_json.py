# -*- coding: utf-8 -*-
"""
Full transcription of all 120 authentic NPTEL Weekly Assignment questions
Extracted directly from NPTEL weekly assignment screenshots (image.png to image-36.png).
"""
import json
import os

weekly_questions = [
    # =========================================================================
    # WEEK 1 ASSIGNMENT (image.png, image-1.png, image-2.png, image-3.png)
    # =========================================================================
    {
        "id": "W1-Q1",
        "week": 1,
        "type": "multi",
        "question": "What sets a PhD apart from other degrees?",
        "options": [
            "Focus on practical skills and hands-on experience",
            "Development of critical thinking and analytical abilities",
            "Preparation to guide others pursuing a PhD",
            "Completion of coursework and examinations"
        ],
        "answer": [1, 2],
        "explanation": "Accepted answer: Development of critical thinking and analytical abilities; Preparation to guide others pursuing a PhD.",
        "passage": None,
        "points": 1
    },
    {
        "id": "W1-Q2",
        "week": 1,
        "type": "single",
        "question": "What distinguishes research-based degree from a typical undergraduate degree?",
        "options": [
            "Well-defined boundaries throughout the degree program",
            "Opportunities for continuous discovery and learning",
            "Graduation day marking the complete end of the degree",
            "Acquisition of expertise and recognition in a specific field"
        ],
        "answer": 1,
        "explanation": "Accepted answer: Opportunities for continuous discovery and learning.",
        "passage": None,
        "points": 1
    },
    {
        "id": "W1-Q3",
        "week": 1,
        "type": "single",
        "question": "What is the importance of attitude and communication in the student-advisor relationship?",
        "options": [
            "Having prior knowledge is the most important factor for a student to work towards a PhD",
            "Advisors expect students to define their own research problems without any guidance",
            "Students should choose advisors based on their reputation and availability",
            "Attitude, inclination to learn, and effective communication with the advisor are crucial."
        ],
        "answer": 3,
        "explanation": "Accepted answer: Attitude, inclination to learn, and effective communication with the advisor are crucial.",
        "passage": None,
        "points": 1
    },
    {
        "id": "W1-Q4",
        "week": 1,
        "type": "single",
        "question": "What makes research challenging for first-time researchers?",
        "options": [
            "The need to handle routine work and drudgery",
            "The sudden shift in patterns from coursework to research",
            "The discovery process involved in understanding the research process",
            "The pressure to obtain a degree and complete the research process"
        ],
        "answer": 1,
        "explanation": "Accepted answer: The sudden shift in patterns from coursework to research.",
        "passage": None,
        "points": 1
    },
    {
        "id": "W1-Q5",
        "week": 1,
        "type": "single",
        "question": "What is one advantage of research when dealing with failure?",
        "options": [
            "Research allows for changing initial assumptions and exploring different approaches",
            "Research ensures that failures are minimized and success is guaranteed",
            "Research provides a predefined path to follow, for sure eliminating the possibility of failure",
            "Research discourages any changes in assumptions or approaches to maintain consistency"
        ],
        "answer": 0,
        "explanation": "Accepted answer: Research allows for changing initial assumptions and exploring different approaches.",
        "passage": None,
        "points": 1
    },
    {
        "id": "W1-Q6",
        "week": 1,
        "type": "single",
        "question": "When conducting experiments and analysing results in research:",
        "options": [
            "Each individual step is always something significant",
            "The familiarity with the area helps in building experiments but the results are often insignificant",
            "Day-to-day experiments and results are usually significant and groundbreaking",
            "Small steps are taken, and over time they contribute to something significant."
        ],
        "answer": 3,
        "explanation": "Accepted answer: Small steps are taken, and over time they contribute to something significant.",
        "passage": None,
        "points": 1
    },
    {
        "id": "W1-Q7",
        "week": 1,
        "type": "single",
        "question": "Technologies in use today have life span of decades",
        "options": ["True", "False"],
        "answer": 1,
        "explanation": "Accepted answer: False. Many gadgets and technologies today become outdated in 2 to 3 years.",
        "passage": "Engineers and Scientists\n\nWe live in a world that is filled with a wide range of technologies that we use and we take for granted. The speed with which new technologies appear and disappear is constantly increasing. These days many of the gadgets we buy get outdated in a time frame of two to three years. This is a short time frame since many of the technologies in use are robust enough to physically last several years. However, in terms of features and utility they get outdated much sooner than that. This is also a short time frame relative to how long technologies were used two or three decades ago. An example is the media used to store music. While gramophone records and cassettes lasted decades, DVDs have fast disappeared. Almost any mobile phone or computer purchased these days become obsolete in two to three years.\n\nBehind this vast moving world of technologies, is a worldwide army of scientists and engineers. They are constantly on the prowl for making advances to existing technologies. Many industries, companies, and educational institutions are filled with scientists and engineers. While there may be some similarities in the tasks they are involved in, there are also some differences.\n\nAn engineer in an industry setting usually faces several technical trouble shooting challenges. Such challenges, with stiff timelines, require substantial familiarity with information databases, and characterization techniques, to be successfully addressed. Addressing trouble shooting challenges are often based on the selection and use of the best available resources and substitutes. The types of questions the engineer is faced with include questions of the sort:\n1. Is there a lighter material readily available which can replace the existing material in the product?\n2. Why is a specific batch of the product not as good as another batch?\n3. Will it be possible for this product to function with lesser parts than it currently has?\nAnswers to such questions enable the industry meet the demands of their customers at lower costs and with greater reliability.\n\nA scientist in a university or laboratory setting faces a different kind of challenge. The questions the scientist wishes to answer are:\n1. Why is the value of any specific property of a material what it is?\n2. What is the fundamental science behind the property?\n3. What are the limits, if any, to this property?\nAnswers to such questions enable one to design new materials and to push the capabilities of existing materials.\n\nBased on the professional setting a materials specialist ends up in, he/she will likely get pulled into one of the above types of activities. However, having both - a good feel for the fundamental sciences, as well as an understanding of the engineering approach to relate to the real world, can greatly enhance the value of a materials scientist/engineer to his or her organization.\n\nAt the same time, it usually takes considerable experience to fully understand, appreciate, and make use of the linkages between fundamental science and the world of engineering. Experience and systematic studies provide us with the insight to make the connections between the real-world inventions and the science behind them. Such insight helps us truly appreciate the contributions of the scientist as well as the engineer in shaping our interactions with the world around us. Such insight also enables us to take our technical pursuits to greater heights and wider reaches, and hence is desirable.",
        "points": 1
    },
    {
        "id": "W1-Q8",
        "week": 1,
        "type": "single",
        "question": "Engineers aim to reduce the number of parts in a product",
        "options": ["True", "False"],
        "answer": 0,
        "explanation": "Accepted answer: True. As stated in the passage: 'Will it be possible for this product to function with lesser parts than it currently has?'",
        "passage": "Engineers and Scientists\n\n(Refer to the passage on Engineers and Scientists provided above)",
        "points": 1
    },
    {
        "id": "W1-Q9",
        "week": 1,
        "type": "single",
        "question": "Global warming is only a theoretical phenomenon",
        "options": ["True", "False"],
        "answer": 1,
        "explanation": "Accepted answer: False. There is very strong experimental evidence that global warming is a real phenomenon.",
        "passage": "Global Warming\n\nGlobal warming refers to the idea that the temperature of the planet is, on average, increasing. It is a topic of considerable discussion and debate internationally because there are differing views on the severity of the phenomenon, the cause for the phenomenon, remedial measures to be considered and the financial impact of such remedial measures.\n\nThere is very strong experimental evidence that global warming is a real phenomenon. 10 of the hottest years recorded in history have all occurred in the last 15 years or so.\n\nThere is also strong reason to believe that the amount of carbon dioxide in the atmosphere, directly impacts the raise in temperature observed globally. This evidence can be seen in the strong correlation between temperature and atmospherical carbon dioxide data collected in the past nearly 60 years, as well as in the temperature and carbon dioxide data that can be obtained for more than 100,000 years, from ice core samples obtained from Antarctica.\n\nBased on energy usage patterns as well as the amount of carbon dioxide released as a function of the energy usage, it is possible to see how human activity can impact carbon dioxide content in the atmosphere in a significant manner. In fact a simple calculation will show that with the present level of energy usage, assuming all of it is from crude oil, the amount of carbon dioxide in the atmosphere will double in less than 100 years.\n\nIn addition to carbon dioxide, there are other gases as well that can accelerate global warming, some much more severely than carbon dioxide. However in terms of sheer quantity in the atmosphere, carbon dioxide is the most significant contributor to global warming.\n\nThe controversy over what needs to be done to combat global warming, is purely one of short term economic impact. Nations which release the most carbon dioxide total, as well the most carbon dioxide per-capita, are both reluctant to take measures to curb the release of carbon dioxide since it impacts quality of life of their populations in the short term. However there is grave danger in assuming such a short term outlook to this issue. If this issue is not addressed urgently, the planet may become unliveable in a relatively short time and at that point, with the very existence of humanity in question, it will look completely absurd to place a few comforts above survival of the planet.\n\nNature controls us indirectly by causing severe weather patterns that shut down cities for days and months. It is much more prudent that we address this issue on our initiative rather than wait for nature to complete the arguments in this context.",
        "points": 1
    },
    {
        "id": "W1-Q10",
        "week": 1,
        "type": "single",
        "question": "Carbon dioxide in the atmosphere contributes to global warming",
        "options": ["True", "False"],
        "answer": 0,
        "explanation": "Accepted answer: True. Carbon dioxide is the most significant contributor to global warming in terms of quantity.",
        "passage": "Global Warming\n\n(Refer to the passage on Global Warming provided above)",
        "points": 1
    },

    # =========================================================================
    # WEEK 2 ASSIGNMENT (image-4.png, image-5.png, image-6.png)
    # =========================================================================
    {
        "id": "W2-Q1",
        "week": 2,
        "type": "single",
        "question": "Experimental data generated from a setup must validate the theoretical predictions or models designed for that setup",
        "options": ["True", "False", "Sometimes", "Never"],
        "answer": 2,
        "explanation": "Accepted answer: Sometimes.",
        "passage": None,
        "points": 1
    },
    {
        "id": "W2-Q2",
        "week": 2,
        "type": "multi",
        "question": "Literature survey is important because",
        "options": [
            "It helps in getting a summary of work that has been done till date in some particular research area",
            "It is helpful in ensuring that a research work is not getting repeated",
            "It is helpful in understanding the approaches taken by scientists and what are the gaps in the processes",
            "It is helpful in clarifying the controversial results that one can get"
        ],
        "answer": [0, 1, 2, 3],
        "explanation": "Accepted answer: It helps in getting a summary of work that has been done till date in some particular research area; It is helpful in ensuring that a research work is not getting repeated; It is helpful in understanding the approaches taken by scientists and what are the gaps in the processes; It is helpful in clarifying the controversial results that one can get.",
        "passage": None,
        "points": 1
    },
    {
        "id": "W2-Q3",
        "week": 2,
        "type": "single",
        "question": "Which of the following methods of searching for literature is suitable to identify the earliest contributor to a scientific outcome?",
        "options": [
            "Keyword based search followed by sorting by year of publication",
            "Citation based search followed by sorting by year of publication",
            "Keyword based search followed by sorting by citations",
            "Back reference based search following a keyword based search"
        ],
        "answer": 3,
        "explanation": "Accepted answer: Back reference based search following a keyword based search.",
        "passage": None,
        "points": 1
    },
    {
        "id": "W2-Q4",
        "week": 2,
        "type": "single",
        "question": "Which of the following bibliographic details is sufficient and unique piece of information to locate an article in an archival journal?",
        "options": ["ISSN", "DOI", "Page Number", "Volume Number"],
        "answer": 1,
        "explanation": "Accepted answer: DOI (Digital Object Identifier).",
        "passage": None,
        "points": 1
    },
    {
        "id": "W2-Q5",
        "week": 2,
        "type": "single",
        "question": "Which of the following is always true of open access journal?",
        "options": [
            "Such journals are not peer-reviewed",
            "Articles in such journal are freely available for download",
            "Such journals do not charge for publication of article",
            "Such journals are of dubious reputation"
        ],
        "answer": 1,
        "explanation": "Accepted answer: Articles in such journal are freely available for download.",
        "passage": None,
        "points": 1
    },
    {
        "id": "W2-Q6",
        "week": 2,
        "type": "single",
        "question": "Which of the following is NOT a recommended practice to identify publications that need to be listed under references of an article?",
        "options": [
            "Relevant publications actually referred to",
            "Latest publications by the editor of the journal",
            "Original publications in the topic of the article",
            "Own publications referred in the article for further details"
        ],
        "answer": 1,
        "explanation": "Accepted answer: Latest publications by the editor of the journal.",
        "passage": None,
        "points": 1
    },
    {
        "id": "W2-Q7",
        "week": 2,
        "type": "single",
        "question": "Which of the following indices is considered as a measure of the impact of a particular author in its area of his/her specialization?",
        "options": [
            "Total number of articles published",
            "Hirsch index of the author",
            "Number of views of his/her latest article",
            "Number of downloads of all articles in a year"
        ],
        "answer": 1,
        "explanation": "Accepted answer: Hirsch index of the author (h-index).",
        "passage": None,
        "points": 1
    },
    {
        "id": "W2-Q8",
        "week": 2,
        "type": "multi",
        "question": "The following are categorized as primary source for literature survey",
        "options": [
            "Periodicals & research reports",
            "Conference proceedings & official publications",
            "Compilations & reviews",
            "Directories & year books"
        ],
        "answer": [0, 1],
        "explanation": "Accepted answer: Periodicals & research reports; Conference proceedings & official publications.",
        "passage": None,
        "points": 1
    },
    {
        "id": "W2-Q9",
        "week": 2,
        "type": "multi",
        "question": "The abstracting databases for systematic manual searches include",
        "options": [
            "INSPEC and COMPENDEX",
            "PubMed",
            "Wikipedia",
            "Chemical Abstract (CA) service"
        ],
        "answer": [0, 1, 3],
        "explanation": "Accepted answer: INSPEC and COMPENDEX; PubMed; Chemical Abstract (CA) service.",
        "passage": None,
        "points": 1
    },
    {
        "id": "W2-Q10",
        "week": 2,
        "type": "single",
        "question": "Consider that you have collected the following resources towards your research:\n(1) A reference in a journal article that you have not referred yet\n(2) A link to the website of a professional society\n(3) A published article with journal, year, volume and page number\n(4) An article from a newly launched journal with volume number, page number but year and ISSN number are due\n(5) A newly accepted journal article with DOI link\n(6) A book with an ISBN number available\n\nWhich of the following can be considered as archival (valuable record) references for inclusion in a publication?",
        "options": [
            "Only 1, 2 and 3",
            "Only 3, 5 and 6",
            "Only 3, 4 and 6",
            "Only 1, 2 and 5"
        ],
        "answer": 1,
        "explanation": "Accepted answer: Only 3, 5 and 6.",
        "passage": None,
        "points": 1
    },

    # =========================================================================
    # WEEK 3 ASSIGNMENT (image-7.png, image-8.png, image-9.png)
    # =========================================================================
    {
        "id": "W3-Q1",
        "week": 3,
        "type": "multi",
        "question": "Safety must be the most important discipline in our routine when in a laboratory or industrial environment. The common sources which have the potential to cause damage, available in a lab towards which we need to be careful are:",
        "options": [
            "Sources of heat",
            "Chemicals (Acids, Bases etc.)",
            "Pressurized gas cylinders",
            "Electricity and water sources"
        ],
        "answer": [0, 1, 2, 3],
        "explanation": "Accepted answer: Sources of heat; Chemicals (Acids, Bases etc.); Pressurized gas cylinders; Electricity and water sources.",
        "passage": None,
        "points": 1
    },
    {
        "id": "W3-Q2",
        "week": 3,
        "type": "single",
        "question": "Which of the following statistics is used to quantify errors in parameter estimates:",
        "options": ["Mode", "Skewness", "Standard deviation", "Median"],
        "answer": 2,
        "explanation": "Accepted answer: Standard deviation.",
        "passage": None,
        "points": 1
    },
    {
        "id": "W3-Q3",
        "week": 3,
        "type": "single",
        "question": "A temperature sensor is installed at the bottom of the cooling tower storage tank to measure temperature of outlet water. The sensor did not function properly for some time and gave data with higher temperature values. The conclusion we can draw from the process is:",
        "options": [
            "Since data with different values were recorded, this increased the possibility of wide analysis thus very useful for our work",
            "The data obtained cannot be reliable because these are not true data from the system but the malfunctioned one",
            "The data can be used with good accuracy using the predictive type data analysis where we can assume the extent of error and finally subtract the error from final value",
            "None of these"
        ],
        "answer": 1,
        "explanation": "Accepted answer: The data obtained cannot be reliable because these are not true data from the system but the malfunctioned one.",
        "passage": None,
        "points": 1
    },
    {
        "id": "W3-Q4",
        "week": 3,
        "type": "single",
        "question": "Which of the following can be treated as deterministic signals?",
        "options": [
            "Measurements of atmospheric temperature",
            "A sine wave corrupted by a rectangular pulse",
            "Estimates of a signal from measurements",
            "None of the above"
        ],
        "answer": 1,
        "explanation": "Accepted answer: A sine wave corrupted by a rectangular pulse.",
        "passage": None,
        "points": 1
    },
    {
        "id": "W3-Q5",
        "week": 3,
        "type": "multi",
        "question": "Identify the incorrect statement(s) among the following on non-linear models:",
        "options": [
            "Linearization involves mere discarding of the non-linear terms in a model",
            "The standard Taylor series-based linearized model changes with the nominal point of linearization",
            "A non-linear model can never yield a zero-valued output to a non-zero input",
            "Estimates of linear models have smaller errors than those of non-linear models"
        ],
        "answer": [0, 2, 3],
        "explanation": "Accepted answer: Linearization involves mere discarding of the non-linear terms in a model; A non-linear model can never yield a zero-valued output to a non-zero input; Estimates of linear models have smaller errors than those of non-linear models.",
        "passage": None,
        "points": 1
    },
    {
        "id": "W3-Q6",
        "week": 3,
        "type": "single",
        "question": "Which of the following transforms are used to detect periodic (oscillatory) components in a signal?",
        "options": [
            "Hilbert transform",
            "Z-transform",
            "Fourier transform",
            "All of the above"
        ],
        "answer": 2,
        "explanation": "Accepted answer: Fourier transform.",
        "passage": None,
        "points": 1
    },
    {
        "id": "W3-Q7",
        "week": 3,
        "type": "single",
        "question": "The ratio of errors in parameter estimates of a model from two data sets with SNR 9 and 100 is",
        "options": ["3 : 10", "10 : 3", "9 : 100", "100 : 9"],
        "answer": 1,
        "explanation": "Accepted answer: 10 : 3 (Error is inversely proportional to square root of SNR: sqrt(100)/sqrt(9) = 10/3).",
        "passage": None,
        "points": 1
    },
    {
        "id": "W3-Q8",
        "week": 3,
        "type": "single",
        "question": "Which of the following is true concerning a parameter estimate?",
        "options": [
            "It is generally close to the true value with high probability",
            "When averaged across a million experimental records under same operating conditions, the estimate equals the true value",
            "Least squares method always gives the estimate with lowest error",
            "It is a mathematical function of the observations"
        ],
        "answer": 3,
        "explanation": "Accepted answer: It is a mathematical function of the observations.",
        "passage": None,
        "points": 1
    },
    {
        "id": "W3-Q9",
        "week": 3,
        "type": "multi",
        "question": "Which of the following statements are true?",
        "options": [
            "Deterministic phenomena produce outcomes that can be predicted accurately",
            "Random processes only occur randomly",
            "A process can produce a mix of deterministic and stochastic effects",
            "Signals from random phenomena cannot take negative values"
        ],
        "answer": [0, 2],
        "explanation": "Accepted answer: Deterministic phenomena produce outcomes that can be predicted accurately; A process can produce a mix of deterministic and stochastic effects.",
        "passage": None,
        "points": 1
    },
    {
        "id": "W3-Q10",
        "week": 3,
        "type": "single",
        "question": "An estimator is said to be most efficient when",
        "options": [
            "Parameters can be estimated in the least possible time",
            "The estimator provides accurate estimates with the smallest number of observations",
            "Standard error in the parameter estimates is lowest when compared to that of other estimators",
            "It estimates parameters accurately even in the presence of outliers"
        ],
        "answer": 2,
        "explanation": "Accepted answer: Standard error in the parameter estimates is lowest when compared to that of other estimators.",
        "passage": None,
        "points": 1
    },

    # =========================================================================
    # WEEK 4 ASSIGNMENT (image-10.png, image-11.png, image-12.png)
    # =========================================================================
    {
        "id": "W4-Q1",
        "week": 4,
        "type": "multi",
        "question": "The title of a paper is 'Battery design and its impact'. This title:",
        "options": [
            "Identifies the area of research clearly",
            "Indicates what is unique about the research",
            "Does not identify the area of the research clearly",
            "Does not indicate what is unique about the research"
        ],
        "answer": [2, 3],
        "explanation": "Accepted answer: Does not identify the area of the research clearly; Does not indicate what is unique about the research.",
        "passage": None,
        "points": 1
    },
    {
        "id": "W4-Q2",
        "week": 4,
        "type": "single",
        "question": "In scientific images:",
        "options": [
            "High magnification implies high resolution",
            "High magnification does not necessarily imply high resolution",
            "Low magnification implies high resolution",
            "High resolution implies low magnification"
        ],
        "answer": 1,
        "explanation": "Accepted answer: High magnification does not necessarily imply high resolution.",
        "passage": None,
        "points": 1
    },
    {
        "id": "W4-Q3",
        "week": 4,
        "type": "single",
        "question": "Tables are preferred over graphs:",
        "options": [
            "Always",
            "Never",
            "Only when exact values need to be indicated",
            "Only when trends in data need to be indicated"
        ],
        "answer": 2,
        "explanation": "Accepted answer: Only when exact values need to be indicated.",
        "passage": None,
        "points": 1
    },
    {
        "id": "W4-Q4",
        "week": 4,
        "type": "multi",
        "question": "The length of a document:",
        "options": [
            "Indicates how much you know",
            "Indicates how little you know",
            "Does not indicate anything about your knowledge",
            "Does not indicate anything about the reader's knowledge"
        ],
        "answer": [2, 3],
        "explanation": "Accepted answer: Does not indicate anything about your knowledge; Does not indicate anything about the reader's knowledge.",
        "passage": None,
        "points": 1
    },
    {
        "id": "W4-Q5",
        "week": 4,
        "type": "single",
        "question": "The title of a paper should indicate the area and not what is unique about the work:",
        "options": ["True", "False"],
        "answer": 1,
        "explanation": "Accepted answer: False. A good title should clearly indicate both the specific area and what is unique about the work.",
        "passage": None,
        "points": 1
    },
    {
        "id": "W4-Q6",
        "week": 4,
        "type": "single",
        "question": "In scientific documents, sentences should be relatively short and simple:",
        "options": ["True", "False"],
        "answer": 0,
        "explanation": "Accepted answer: True. Sentences in scientific writing should be concise, clear, and direct.",
        "passage": None,
        "points": 1
    },
    {
        "id": "W4-Q7",
        "week": 4,
        "type": "multi",
        "question": "In an article, the image of a car engine must:",
        "options": [
            "Show the level of detail required for the discussion in the article",
            "Have a marker bar indicating scale",
            "Be in colour and not in black and white",
            "Be in black and white and not in colour"
        ],
        "answer": [0, 1],
        "explanation": "Accepted answer: Show the level of detail required for the discussion in the article; Have a marker bar indicating scale.",
        "passage": None,
        "points": 1
    },
    {
        "id": "W4-Q8",
        "week": 4,
        "type": "multi",
        "question": "Strategies one can use in the middle of a document include:",
        "options": [
            "Chronological strategy",
            "Spatial strategy",
            "Following a variable",
            "Suspense strategy"
        ],
        "answer": [0, 1, 2],
        "explanation": "Accepted answer: Chronological strategy; Spatial strategy; Following a variable.",
        "passage": None,
        "points": 1
    },
    {
        "id": "W4-Q9",
        "week": 4,
        "type": "single",
        "question": "While working with electricity only the voltage poses a danger to the users:",
        "options": ["True", "False"],
        "answer": 1,
        "explanation": "Accepted answer: False. Current (amperage) and pathway through the body also pose critical dangers.",
        "passage": None,
        "points": 1
    },
    {
        "id": "W4-Q10",
        "week": 4,
        "type": "single",
        "question": "\"Pouring rain results in clogged drains and slippery roads. These clogged drains spill further water on the road.\" Use of the word 'these' in the previous sentence is ambiguous:",
        "options": ["True", "False"],
        "answer": 1,
        "explanation": "Accepted answer: False. 'These clogged drains' clearly points to the specific clogged drains mentioned right before.",
        "passage": None,
        "points": 1
    },

    # =========================================================================
    # WEEK 5 ASSIGNMENT (image-13.png, image-14.png, image-15.png)
    # =========================================================================
    {
        "id": "W5-Q1",
        "week": 5,
        "type": "multi",
        "question": "According to Sternberg's theories of intelligence, practical intelligence is:",
        "options": [
            "How one relates to the environment around them",
            "How street smart they are",
            "How fast they can come up with new theories",
            "How easily they solve new mathematical problems"
        ],
        "answer": [0, 1],
        "explanation": "Accepted answer: How one relates to the environment around them; How street smart they are.",
        "passage": None,
        "points": 1
    },
    {
        "id": "W5-Q2",
        "week": 5,
        "type": "single",
        "question": "Few research scholars collaborated to work on some specific topic. They generated some data and analysed the results. Some of them published the results independently since they were the first to type. Is it ethical to do so?",
        "options": [
            "Yes, because they have collaborated and know each other",
            "No, all authors should know and agree with the publication",
            "Yes, if the collaborators are junior",
            "No, only if the authors are senior"
        ],
        "answer": 1,
        "explanation": "Accepted answer: No, all authors should know and agree with the publication.",
        "passage": None,
        "points": 1
    },
    {
        "id": "W5-Q3",
        "week": 5,
        "type": "single",
        "question": "Creativity is seen in:",
        "options": ["Drama", "Science fiction", "Engineering", "All of the above"],
        "answer": 3,
        "explanation": "Accepted answer: All of the above.",
        "passage": None,
        "points": 1
    },
    {
        "id": "W5-Q4",
        "week": 5,
        "type": "single",
        "question": "A researcher is often well read in many topics:",
        "options": ["True", "False"],
        "answer": 0,
        "explanation": "Accepted answer: True.",
        "passage": None,
        "points": 1
    },
    {
        "id": "W5-Q5",
        "week": 5,
        "type": "single",
        "question": "We can work at the best of our potential when we are:",
        "options": ["Hypo stressed", "Eustressed", "Hyper stressed", "Distressed"],
        "answer": 1,
        "explanation": "Accepted answer: Eustressed (optimal level of positive stress).",
        "passage": None,
        "points": 1
    },
    {
        "id": "W5-Q6",
        "week": 5,
        "type": "multi",
        "question": "The measure of a successful researcher is that the work of the researcher should be:",
        "options": [
            "Recognized by peers at an international level",
            "Typically published in peer reviewed journals",
            "Mentioned in the campus magazine of the college",
            "Must be discussed in the Department meeting of the researcher's department"
        ],
        "answer": [0, 1],
        "explanation": "Accepted answer: Recognized by peers at an international level; Typically published in peer reviewed journals.",
        "passage": None,
        "points": 1
    },
    {
        "id": "W5-Q7",
        "week": 5,
        "type": "multi",
        "question": "Creative people are:",
        "options": [
            "More likely to follow societal restrictions",
            "Less likely to follow societal restrictions",
            "More likely to think within the limits of previous work in the area",
            "More likely to come up with a surprisingly new solution to a problem"
        ],
        "answer": [1, 3],
        "explanation": "Accepted answer: Less likely to follow societal restrictions; More likely to come up with a surprisingly new solution to a problem.",
        "passage": None,
        "points": 1
    },
    {
        "id": "W5-Q8",
        "week": 5,
        "type": "single",
        "question": "A PhD usually makes you a:",
        "options": [
            "Specialist in one narrow area",
            "Person who conducts experiments fast",
            "Person who has a wide knowledge in a wide range of topics",
            "Person who makes excellent sketches"
        ],
        "answer": 0,
        "explanation": "Accepted answer: Specialist in one narrow area.",
        "passage": None,
        "points": 1
    },
    {
        "id": "W5-Q9",
        "week": 5,
        "type": "multi",
        "question": "To become a good researcher, one must usually:",
        "options": [
            "Have good communication skills",
            "Have mastery over specific techniques",
            "Have a line of investigation",
            "Be aware of recent advances in the field"
        ],
        "answer": [0, 1, 2, 3],
        "explanation": "Accepted answer: Have good communication skills; Have mastery over specific techniques; Have a line of investigation; Be aware of recent advances in the field.",
        "passage": None,
        "points": 1
    },
    {
        "id": "W5-Q10",
        "week": 5,
        "type": "multi",
        "question": "The followings can be attributed to a fully professional researcher:",
        "options": [
            "They have some fundamental concepts that their peers (international) might be interested in",
            "They have command over their area",
            "They are aware of the situation where they can make significant contribution",
            "They work without focusing on literature in the area"
        ],
        "answer": [0, 1, 2],
        "explanation": "Accepted answer: They have some fundamental concepts that their peers (international) might be interested in; They have command over their area; They are aware of the situation where they can make significant contribution.",
        "passage": None,
        "points": 1
    },

    # =========================================================================
    # WEEK 6 ASSIGNMENT (image-16.png, image-17.png, image-18.png)
    # =========================================================================
    {
        "id": "W6-Q1",
        "week": 6,
        "type": "multi",
        "question": "Which of the following falls in the category of intellectual property?",
        "options": [
            "An original set of ideas or research results",
            "Properties originating from real estate",
            "Properties emanating from human creative labor",
            "All of the above"
        ],
        "answer": [0, 2],
        "explanation": "Accepted answer: An original set of ideas or research results; Properties emanating from human creative labor.",
        "passage": None,
        "points": 1
    },
    {
        "id": "W6-Q2",
        "week": 6,
        "type": "single",
        "question": "Violations of Intellectual Property Rights leads to:",
        "options": [
            "Infringement",
            "Casual penalties, not a big deal",
            "We have licenses & fundamental rights to do whatever we want",
            "None of the above"
        ],
        "answer": 0,
        "explanation": "Accepted answer: Infringement.",
        "passage": None,
        "points": 1
    },
    {
        "id": "W6-Q3",
        "week": 6,
        "type": "single",
        "question": "In order to obtain legal protection, you don't have to register which of the following types of intellectual property rights?",
        "options": ["Copyrights", "Patents", "Designs", "Geographical Indications"],
        "answer": 0,
        "explanation": "Accepted answer: Copyrights (copyright protection exists automatically upon original creation).",
        "passage": None,
        "points": 1
    },
    {
        "id": "W6-Q4",
        "week": 6,
        "type": "single",
        "question": "If a person invents a process to capture musical performance on a cassette tape, he/she will most likely apply for:",
        "options": ["Copyrights", "Trade Marks", "Patents", "Trade Secrets"],
        "answer": 2,
        "explanation": "Accepted answer: Patents (a novel technical process is protected by patent).",
        "passage": None,
        "points": 1
    },
    {
        "id": "W6-Q5",
        "week": 6,
        "type": "single",
        "question": "Use of an unregistered trade mark by a competitor shall amount to a tort of:",
        "options": ["Deceit", "Fraud", "Negligence", "Passing off"],
        "answer": 3,
        "explanation": "Accepted answer: Passing off.",
        "passage": None,
        "points": 1
    },
    {
        "id": "W6-Q6",
        "week": 6,
        "type": "single",
        "question": "What does a right entitle a person?",
        "options": [
            "Right to file a suit in case of an infringement",
            "Right to excludability",
            "Right to commercial exploitation",
            "All of the above"
        ],
        "answer": 3,
        "explanation": "Accepted answer: All of the above.",
        "passage": None,
        "points": 1
    },
    {
        "id": "W6-Q7",
        "week": 6,
        "type": "single",
        "question": "The Reebok Delta symbol and Hyundai logo are protected by:",
        "options": ["Patent", "Trade Marks", "Trade Dress", "Geographical Indications"],
        "answer": 1,
        "explanation": "Accepted answer: Trade Marks.",
        "passage": None,
        "points": 1
    },
    {
        "id": "W6-Q8",
        "week": 6,
        "type": "single",
        "question": "Under the Patents Act, 1970, the one entitled to receive a patent on a new invention is:",
        "options": [
            "The one who invented the invention first",
            "The one who commercialized the invention first",
            "The one who thought of the invention first",
            "The one who filed a patent application first"
        ],
        "answer": 3,
        "explanation": "Accepted answer: The one who filed a patent application first ('first-to-file' system).",
        "passage": None,
        "points": 1
    },
    {
        "id": "W6-Q9",
        "week": 6,
        "type": "single",
        "question": "What is the term of a Patent in India?",
        "options": ["20 years", "25 years", "10 years", "15 years"],
        "answer": 0,
        "explanation": "Accepted answer: 20 years from the date of filing.",
        "passage": None,
        "points": 1
    },
    {
        "id": "W6-Q10",
        "week": 6,
        "type": "single",
        "question": "What is the full form of TRIPS?",
        "options": [
            "Tariff Related Aspects of Intellectual Properties",
            "Trade Related Aspects of Intellectual Property Science",
            "The Registration of Intellectual Property",
            "Trade Related Aspects of Intellectual Property Rights"
        ],
        "answer": 3,
        "explanation": "Accepted answer: Trade Related Aspects of Intellectual Property Rights.",
        "passage": None,
        "points": 1
    },

    # =========================================================================
    # WEEK 7 ASSIGNMENT (image-19.png, image-20.png, image-21.png)
    # =========================================================================
    {
        "id": "W7-Q1",
        "week": 7,
        "type": "single",
        "question": "In the true experimental research design:",
        "options": [
            "No control on external variables",
            "Less control on external variables",
            "Control on external variables by randomization",
            "No use of randomization"
        ],
        "answer": 2,
        "explanation": "Accepted answer: Control on external variables by randomization.",
        "passage": None,
        "points": 1
    },
    {
        "id": "W7-Q2",
        "week": 7,
        "type": "single",
        "question": "Which of the following is an incomplete experimental research design?",
        "options": [
            "Before and after with control group design",
            "Factorial design",
            "One group before-after design",
            "Latin Square design"
        ],
        "answer": 2,
        "explanation": "Accepted answer: One group before-after design.",
        "passage": None,
        "points": 1
    },
    {
        "id": "W7-Q3",
        "week": 7,
        "type": "multi",
        "question": "Coefficient of Determination is said to be unity when:",
        "options": [
            "Error Sum of Squares is zero",
            "Total Sum of Squares is zero",
            "Regression Sum of Squares is zero",
            "Regression Sum of Squares is same as Total Sum of Squares"
        ],
        "answer": [0, 3],
        "explanation": "Accepted answer: Error Sum of Squares is zero; Regression Sum of Squares is same as Total Sum of Squares (R^2 = SSR/SST = 1 - SSE/SST = 1).",
        "passage": None,
        "points": 1
    },
    {
        "id": "W7-Q4",
        "week": 7,
        "type": "single",
        "question": "The probability density function describes the following:",
        "options": [
            "Probability of a phenomenon occurring",
            "Probability of a phenomenon occurring at micro scale",
            "Distribution of probabilities in the continuous random variable domain",
            "Distribution of probabilities in some particular set of undefined variables"
        ],
        "answer": 2,
        "explanation": "Accepted answer: Distribution of probabilities in the continuous random variable domain.",
        "passage": None,
        "points": 1
    },
    {
        "id": "W7-Q5",
        "week": 7,
        "type": "single",
        "question": "During Response Surface Methodology & Canonical Analysis involving two factors, maximum response is said to be achieved when the eigen values of the matrix are:",
        "options": [
            "all positive",
            "all negative",
            "all zero",
            "such that one is positive and the other is negative"
        ],
        "answer": 1,
        "explanation": "Accepted answer: all negative (negative definite Hessian indicates a local maximum).",
        "passage": None,
        "points": 1
    },
    {
        "id": "W7-Q6",
        "week": 7,
        "type": "single",
        "question": "Experiments are conducted in laboratories to:",
        "options": [
            "Verify scientific predictions",
            "Obtain trends when theory is not known",
            "Find effect of different variables on the desired response",
            "All of the above"
        ],
        "answer": 3,
        "explanation": "Accepted answer: All of the above.",
        "passage": None,
        "points": 1
    },
    {
        "id": "W7-Q7",
        "week": 7,
        "type": "single",
        "question": "SPC and Design of Experiments are very closely interrelated:",
        "options": ["True", "False"],
        "answer": 0,
        "explanation": "Accepted answer: True.",
        "passage": None,
        "points": 1
    },
    {
        "id": "W7-Q8",
        "week": 7,
        "type": "single",
        "question": "Which of these is NOT an application of experimental design in the field of Engineering design?",
        "options": [
            "Evaluation and comparison of basic design configurations",
            "Evaluation of material alternatives",
            "Evaluation of key product parameters that impact performance",
            "Evaluation of correct process to develop the product"
        ],
        "answer": 3,
        "explanation": "Accepted answer: Evaluation of correct process to develop the product.",
        "passage": None,
        "points": 1
    },
    {
        "id": "W7-Q9",
        "week": 7,
        "type": "single",
        "question": "The average estimated from a data collection is 50 cm. The quantity (quantities) which has the same units as the data is (are):",
        "options": [
            "Standard deviation",
            "Median",
            "Mode",
            "All of the above"
        ],
        "answer": 3,
        "explanation": "Accepted answer: All of the above (Mean, median, mode, and standard deviation all share the identical measurement unit as the underlying data).",
        "passage": None,
        "points": 1
    },
    {
        "id": "W7-Q10",
        "week": 7,
        "type": "single",
        "question": "Sample collected from an instrument giving binary data has the following values {1, -1, -1, 1, 1, -1}. Mean of the above data set is:",
        "options": ["0", "1", "-1", "0.5"],
        "answer": 0,
        "explanation": "Accepted answer: 0 (Sum = 1 - 1 - 1 + 1 + 1 - 1 = 0; Mean = 0 / 6 = 0).",
        "passage": None,
        "points": 1
    },

    # =========================================================================
    # WEEK 8 ASSIGNMENT (image-22.png, image-23.png, image-24.png)
    # =========================================================================
    {
        "id": "W8-Q1",
        "week": 8,
        "type": "single",
        "question": "Doing queue the research, which of the following is priorly required?",
        "options": [
            "Developing research design",
            "Formulating a research question",
            "Deciding about the data analysis procedure",
            "Formulating a research hypothesis"
        ],
        "answer": 1,
        "explanation": "Accepted answer: Formulating a research question.",
        "passage": None,
        "points": 1
    },
    {
        "id": "W8-Q2",
        "week": 8,
        "type": "single",
        "question": "Which one among the following statements is false in the context of participatory research?",
        "options": [
            "It recognizes knowledge as power",
            "It is a collective process of inquiry",
            "It emphasizes people as experts",
            "Its sole purpose is the production of knowledge"
        ],
        "answer": 3,
        "explanation": "Accepted answer: Its sole purpose is the production of knowledge.",
        "passage": None,
        "points": 1
    },
    {
        "id": "W8-Q3",
        "week": 8,
        "type": "single",
        "question": "How do you judge the depth of any research?",
        "options": [
            "By research title",
            "By research duration",
            "By research objectives",
            "By total expenditure on research"
        ],
        "answer": 2,
        "explanation": "Accepted answer: By research objectives.",
        "passage": None,
        "points": 1
    },
    {
        "id": "W8-Q4",
        "week": 8,
        "type": "single",
        "question": "What is the main aim of interdisciplinary research?",
        "options": [
            "To oversimplify the problem of research",
            "Integrating knowledge from multiple disciplines to solve a problem",
            "To create a new trend in research methodology",
            "To reduce the emphasis on a single subject in the research domain"
        ],
        "answer": 1,
        "explanation": "Accepted answer: Integrating knowledge from multiple disciplines to solve a problem.",
        "passage": None,
        "points": 1
    },
    {
        "id": "W8-Q5",
        "week": 8,
        "type": "single",
        "question": "Electron microscopes can be used to view extremely small areas:",
        "options": ["True", "False"],
        "answer": 0,
        "explanation": "Accepted answer: True.",
        "passage": None,
        "points": 1
    },
    {
        "id": "W8-Q6",
        "week": 8,
        "type": "single",
        "question": "What are the core elements of a dissertation?",
        "options": [
            "Introduction; Data Collection; Data Analysis; Conclusions and Recommendations",
            "Executive Summary; Literature Review; Data Gathered; Conclusions; Bibliography",
            "Research Plan; Research Data; Analysis; References",
            "Introduction; Literature Review; Research Methodology; Results; Discussions and Conclusions"
        ],
        "answer": 3,
        "explanation": "Accepted answer: Introduction; Literature Review; Research Methodology; Results; Discussions and Conclusions.",
        "passage": None,
        "points": 1
    },
    {
        "id": "W8-Q7",
        "week": 8,
        "type": "single",
        "question": "How can we enhance the research objective?",
        "options": [
            "By making it more valid",
            "By making it more reliable",
            "By making it more impartial",
            "All of the above"
        ],
        "answer": 3,
        "explanation": "Accepted answer: All of the above.",
        "passage": None,
        "points": 1
    },
    {
        "id": "W8-Q8",
        "week": 8,
        "type": "single",
        "question": "A common test in research demands much priority on:",
        "options": ["Reliability", "Useability", "Objectivity", "All of the above"],
        "answer": 3,
        "explanation": "Accepted answer: All of the above.",
        "passage": None,
        "points": 1
    },
    {
        "id": "W8-Q9",
        "week": 8,
        "type": "single",
        "question": "An appropriate source to find out descriptive information is:",
        "options": ["Bibliography", "Directory", "Encyclopedia", "Dictionary"],
        "answer": 2,
        "explanation": "Accepted answer: Encyclopedia.",
        "passage": None,
        "points": 1
    },
    {
        "id": "W8-Q10",
        "week": 8,
        "type": "single",
        "question": "Mahabalipuram in south-east India is pre-eminently testimony to the civilization of:",
        "options": ["Pallavas", "Mauryas", "Guptas", "Cholas"],
        "answer": 0,
        "explanation": "Accepted answer: Pallavas.",
        "passage": None,
        "points": 1
    },

    # =========================================================================
    # WEEK 9 ASSIGNMENT (image-25.png, image-26.png, image-27.png)
    # =========================================================================
    {
        "id": "W9-Q1",
        "week": 9,
        "type": "multi",
        "question": "Which of the following characteristics distinguish a research programme from a curriculum-oriented academic programme?",
        "options": [
            "The research question may itself require extensive exploration before becoming well defined.",
            "Experimental outcomes may deviate from expectations and require modification of the research approach.",
            "The programme follows a highly predictable schedule with predefined training outcomes for every stage.",
            "The researcher may repeatedly formulate new questions as insights emerge from previous work."
        ],
        "answer": [0, 1, 3],
        "explanation": "Accepted answer: The research question may itself require extensive exploration before becoming well defined; Experimental outcomes may deviate from expectations and require modification of the research approach; The researcher may repeatedly formulate new questions as insights emerge from previous work.",
        "passage": None,
        "points": 1
    },
    {
        "id": "W9-Q2",
        "week": 9,
        "type": "single",
        "question": "The lecture compares the research journey to a roller-coaster ride primarily because:",
        "options": [
            "Research requires researchers to work continuously under high pressure",
            "Research consists of predictable stages followed by unavoidable examinations",
            "Research involves alternating periods of progress, uncertainty, setbacks, breakthroughs, and renewed progress",
            "Research is primarily dependent on collaboration with a large number of researchers"
        ],
        "answer": 2,
        "explanation": "Accepted answer: Research involves alternating periods of progress, uncertainty, setbacks, breakthroughs, and renewed progress.",
        "passage": None,
        "points": 1
    },
    {
        "id": "W9-Q3",
        "week": 9,
        "type": "multi",
        "question": "According to the lecture, which factors can contribute to the overall research experience of a scholar in a laboratory?",
        "options": [
            "Relationships with advisers and labmates",
            "Emotional experiences and friendships",
            "Availability and accessibility of research facilities",
            "Support received from friends and family"
        ],
        "answer": [0, 1, 2, 3],
        "explanation": "Accepted answer: Relationships with advisers and labmates; Emotional experiences and friendships; Availability and accessibility of research facilities; Support received from friends and family.",
        "passage": None,
        "points": 1
    },
    {
        "id": "W9-Q4",
        "week": 9,
        "type": "multi",
        "question": "Which practices are presented in the lecture as useful for maintaining a sustainable rhythm in research life?",
        "options": [
            "Adequate sleep and physical activity",
            "Taking time for recreation and renewal",
            "Reflecting periodically on one's activities and decisions",
            "Working continuously for extremely long hours whenever a problem arises"
        ],
        "answer": [0, 1, 2],
        "explanation": "Accepted answer: Adequate sleep and physical activity; Taking time for recreation and renewal; Reflecting periodically on one's activities and decisions.",
        "passage": None,
        "points": 1
    },
    {
        "id": "W9-Q5",
        "week": 9,
        "type": "single",
        "question": "A researcher receives harsh feedback from an adviser and immediately feels angry and personally inadequate. Based on the lecture, what should be the most appropriate immediate response?",
        "options": [
            "Respond immediately to the adviser to defend the research",
            "Suppress the emotion completely and continue working without reflection",
            "Pause, recognize the emotion, regulate it through techniques such as rhythmic breathing, and then respond with greater clarity.",
            "Discuss the adviser's behaviour with labmates immediately"
        ],
        "answer": 2,
        "explanation": "Accepted answer: Pause, recognize the emotion, regulate it through techniques such as rhythmic breathing, and then respond with greater clarity.",
        "passage": None,
        "points": 1
    },
    {
        "id": "W9-Q6",
        "week": 9,
        "type": "multi",
        "question": "Which of the following strategies are specifically discussed in the lecture as ways of processing or reducing intense anger?",
        "options": [
            "Practicing rhythmic breathing",
            "Temporarily stepping away from the situation",
            "Journaling what one is feeling",
            "Immediately confronting the person responsible for the trigger"
        ],
        "answer": [0, 1, 2],
        "explanation": "Accepted answer: Practicing rhythmic breathing; Temporarily stepping away from the situation; Journaling what one is feeling.",
        "passage": None,
        "points": 1
    },
    {
        "id": "W9-Q7",
        "week": 9,
        "type": "single",
        "question": "A research scholar feels discouraged after a labmate's paper is accepted while their own paper remains unpublished. Which response reflects the approach advocated in the lecture?",
        "options": [
            "Compare the two researchers and conclude that the labmate is more capable",
            "Suppress the feeling of comparison without examining its cause",
            "Convert the comparison into curiosity by investigating what the labmate did differently and identifying possible improvements in one's own approach.",
            "Avoid interacting with the labmate until one's own paper is accepted"
        ],
        "answer": 2,
        "explanation": "Accepted answer: Convert the comparison into curiosity by investigating what the labmate did differently and identifying possible improvements in one's own approach.",
        "passage": None,
        "points": 1
    },
    {
        "id": "W9-Q8",
        "week": 9,
        "type": "multi",
        "question": "According to the lecture, prolonged emotional distress and isolation can negatively affect which aspects of a researcher's life?",
        "options": [
            "Research progress",
            "Only the researcher's publication record",
            "Physical health",
            "Friendships and social relationships"
        ],
        "answer": [0, 2, 3],
        "explanation": "Accepted answer: Research progress; Physical health; Friendships and social relationships.",
        "passage": None,
        "points": 1
    },
    {
        "id": "W9-Q9",
        "week": 9,
        "type": "single",
        "question": "A researcher becomes stuck on a difficult problem and begins working for very long hours while withdrawing from friends and labmates. According to the lecture, what is the primary concern with this response?",
        "options": [
            "It demonstrates insufficient commitment to independent research",
            "Emotional isolation may worsen the situation and negatively affect research progress as well as personal well-being.",
            "Long working hours always produce incorrect experimental results",
            "Researchers should never attempt to solve difficult problems independently"
        ],
        "answer": 1,
        "explanation": "Accepted answer: Emotional isolation may worsen the situation and negatively affect research progress as well as personal well-being.",
        "passage": None,
        "points": 1
    },
    {
        "id": "W9-Q10",
        "week": 9,
        "type": "multi",
        "question": "Which of the following constitute potential support systems for a research scholar according to the lecture?",
        "options": [
            "Adviser or supervisor",
            "Labmates and friends",
            "Mentor",
            "Family or old friends"
        ],
        "answer": [0, 1, 2, 3],
        "explanation": "Accepted answer: Adviser or supervisor; Labmates and friends; Mentor; Family or old friends.",
        "passage": None,
        "points": 1
    },

    # =========================================================================
    # WEEK 10 ASSIGNMENT (image-28.png, image-29.png, image-30.png)
    # =========================================================================
    {
        "id": "W10-Q1",
        "week": 10,
        "type": "multi",
        "question": "Students in schools typically expect:",
        "options": [
            "Well defined questions",
            "Question paper patterns to be finalized in advance",
            "Clarity on the portions for exam",
            "Questions outside the syllabus"
        ],
        "answer": [0, 1, 2],
        "explanation": "Accepted answer: Well defined questions; Question paper patterns to be finalized in advance; Clarity on the portions for exam.",
        "passage": None,
        "points": 1
    },
    {
        "id": "W10-Q2",
        "week": 10,
        "type": "single",
        "question": "From the perspective of a school student, the question 'How long will it take to go from Chennai to Kolkata?' is:",
        "options": [
            "A 'poorly' defined question",
            "A well defined question",
            "Is typically how a full question is framed in an exam",
            "Has a unique answer"
        ],
        "answer": 0,
        "explanation": "Accepted answer: A 'poorly' defined question (mode of transport, route, and conditions are unspecified).",
        "passage": None,
        "points": 1
    },
    {
        "id": "W10-Q3",
        "week": 10,
        "type": "multi",
        "question": "The format of exams in schools:",
        "options": [
            "Helps you understand fundamentals",
            "Teaches you to breakdown a problem to parts and solve them",
            "Prepares you for a professional setting",
            "Teaches you to handle unexpected questions"
        ],
        "answer": [0, 1, 2],
        "explanation": "Accepted answer: Helps you understand fundamentals; Teaches you to breakdown a problem to parts and solve them; Prepares you for a professional setting.",
        "passage": None,
        "points": 1
    },
    {
        "id": "W10-Q4",
        "week": 10,
        "type": "multi",
        "question": "A typical professional workplace requires you to:",
        "options": [
            "Handle open ended questions",
            "Solve 'poorly' defined problems",
            "Focus only on a syllabus",
            "Work within a question paper pattern"
        ],
        "answer": [0, 1],
        "explanation": "Accepted answer: Handle open ended questions; Solve 'poorly' defined problems.",
        "passage": None,
        "points": 1
    },
    {
        "id": "W10-Q5",
        "week": 10,
        "type": "multi",
        "question": "Learning in college is expected to:",
        "options": [
            "Prepare you for professional life",
            "Focus only on well-defined problems",
            "Teach you to handle open ended problems",
            "Follow the same approach used in school"
        ],
        "answer": [0, 2],
        "explanation": "Accepted answer: Prepare you for professional life; Teach you to handle open ended problems.",
        "passage": None,
        "points": 1
    },
    {
        "id": "W10-Q6",
        "week": 10,
        "type": "single",
        "question": "Applying a known concept to a new situation is most likely:",
        "options": [
            "Breakthrough research",
            "Incremental research",
            "Transformational research",
            "Important contribution to research"
        ],
        "answer": 1,
        "explanation": "Accepted answer: Incremental research.",
        "passage": None,
        "points": 1
    },
    {
        "id": "W10-Q7",
        "week": 10,
        "type": "single",
        "question": "Use of a series of experimental techniques to study the same phenomenon across different samples is typically an example of:",
        "options": [
            "Systematic research",
            "Transformational research",
            "Incremental research",
            "Breakthrough research"
        ],
        "answer": 0,
        "explanation": "Accepted answer: Systematic research.",
        "passage": None,
        "points": 1
    },
    {
        "id": "W10-Q8",
        "week": 10,
        "type": "single",
        "question": "In the development of phones, which of the following can be considered transformational?",
        "options": [
            "First deployment of the landline",
            "First deployment of the cordless phone",
            "The improvement from cordless phone to mobile phone",
            "Making the first-generation mobile phones smaller and more colorful"
        ],
        "answer": 2,
        "explanation": "Accepted answer: The improvement from cordless phone to mobile phone.",
        "passage": None,
        "points": 1
    },
    {
        "id": "W10-Q9",
        "week": 10,
        "type": "single",
        "question": "In the development of bicycles, which of the following can be considered transformational?",
        "options": [
            "Improvement from wooden seat to cushioned seat",
            "Making the seat more ergonomic",
            "Adding a carrier",
            "Adding gears to a bicycle"
        ],
        "answer": 3,
        "explanation": "Accepted answer: Adding gears to a bicycle.",
        "passage": None,
        "points": 1
    },
    {
        "id": "W10-Q10",
        "week": 10,
        "type": "single",
        "question": "In the development of airplanes, we can associate imagination with:",
        "options": [
            "Designing fixed wings even though birds have flapping wings",
            "Adding seats inside an airplane",
            "Creating a cargo version of the airplane",
            "Adding more engines to the airplane"
        ],
        "answer": 0,
        "explanation": "Accepted answer: Designing fixed wings even though birds have flapping wings.",
        "passage": None,
        "points": 1
    },

    # =========================================================================
    # WEEK 11 ASSIGNMENT (image-31.png, image-32.png, image-33.png)
    # =========================================================================
    {
        "id": "W11-Q1",
        "week": 11,
        "type": "multi",
        "question": "The lecture uses the example of Arthur Samuel's checkers program to illustrate an early form of machine learning. Which of the following statements are correct?",
        "options": [
            "The machine was explicitly programmed with every possible checkers strategy",
            "The machine learned through experience by repeatedly playing the game",
            "The example is associated with an early instance of reinforcement learning",
            "The example demonstrates that AI-based learning is a phenomenon that occurred only with generative AI"
        ],
        "answer": [1, 2],
        "explanation": "Accepted answer: The machine learned through experience by repeatedly playing the game; The example is associated with an early instance of reinforcement learning.",
        "passage": None,
        "points": 1
    },
    {
        "id": "W11-Q2",
        "week": 11,
        "type": "multi",
        "question": "Which of the following statements correctly reflect the lecture's discussion of classical AI and generative AI?",
        "options": [
            "Generative AI is the only appropriate approach for solving modern research problems",
            "Classical AI methods can still provide effective solutions for domain-specific problems",
            "Researchers should select an approach according to the problem rather than assuming that generative AI must always be used.",
            "Classical AI became completely irrelevant after the emergence of LLMs."
        ],
        "answer": [1, 2],
        "explanation": "Accepted answer: Classical AI methods can still provide effective solutions for domain-specific problems; Researchers should select an approach according to the problem rather than assuming that generative AI must always be used.",
        "passage": None,
        "points": 1
    },
    {
        "id": "W11-Q3",
        "week": 11,
        "type": "multi",
        "question": "Consider an LLM that predicts the next token from the context provided. Which of the following statements are correct?",
        "options": [
            "The probability of a token can depend on the preceding context",
            "A token with the highest probability must always be generated",
            "Different contexts can result in different probability distributions for the next token",
            "The model can repeatedly predict tokens to construct a response"
        ],
        "answer": [0, 2, 3],
        "explanation": "Accepted answer: The probability of a token can depend on the preceding context; Different contexts can result in different probability distributions for the next token; The model can repeatedly predict tokens to construct a response.",
        "passage": None,
        "points": 1
    },
    {
        "id": "W11-Q4",
        "week": 11,
        "type": "multi",
        "question": "Which of the following correctly distinguish token size, context size, and parameter count in an LLM?",
        "options": [
            "Token size is related to the vocabulary of words or subwords that the model can generate",
            "Context size refers to the amount of previous token information considered by the model",
            "Parameter count refers to the number of tokens that can be stored in the prompt",
            "Parameter count is related to how the learned probability distributions are represented in the model."
        ],
        "answer": [0, 1, 3],
        "explanation": "Accepted answer: Token size is related to the vocabulary of words or subwords that the model can generate; Context size refers to the amount of previous token information considered by the model; Parameter count is related to how the learned probability distributions are represented in the model.",
        "passage": None,
        "points": 1
    },
    {
        "id": "W11-Q5",
        "week": 11,
        "type": "multi",
        "question": "Which statements correctly describe the role of vector representations in an LLM framework explained in the lecture?",
        "options": [
            "A very large probability matrix can be represented through a comparatively smaller-dimensional vector space",
            "Different contexts may be projected to nearby locations in the vector space",
            "Such compression can contribute to variability and errors because information from different contexts may influence generation.",
            "Each possible sentence is retained as a completely independent point with no overlap"
        ],
        "answer": [0, 1, 2],
        "explanation": "Accepted answer: A very large probability matrix can be represented through a comparatively smaller-dimensional vector space; Different contexts may be projected to nearby locations in the vector space; Such compression can contribute to variability and errors because information from different contexts may influence generation.",
        "passage": None,
        "points": 1
    },
    {
        "id": "W11-Q6",
        "week": 11,
        "type": "multi",
        "question": "Which of the following statements are consistent with the lecture's explanation of alignment?",
        "options": [
            "Alignment can modify model behaviour so that generated probabilities better correspond to desired outcomes",
            "Alignment may be directed towards objectives such as factuality, bias reduction, or local context",
            "Alignment guarantees that all outputs produced by an LLM are factually correct",
            "Reinforcement learning from human preferences is associated with the alignment process"
        ],
        "answer": [0, 1, 3],
        "explanation": "Accepted answer: Alignment can modify model behaviour so that generated probabilities better correspond to desired outcomes; Alignment may be directed towards objectives such as factuality, bias reduction, or local context; Reinforcement learning from human preferences is associated with the alignment process.",
        "passage": None,
        "points": 1
    },
    {
        "id": "W11-Q7",
        "week": 11,
        "type": "multi",
        "question": "A researcher asks a language model a question whose meaning is ambiguous. Relevant information is retrieved from an external repository and added to the original question before generating the answer. Which statements correctly describe this approach?",
        "options": [
            "The approach is consistent with Retrieval-Augmented Generation (RAG)",
            "The retrieved information provides additional context to the model",
            "The approach necessarily requires retraining the entire language model",
            "Additional context can make the model's response more focused"
        ],
        "answer": [0, 1, 3],
        "explanation": "Accepted answer: The approach is consistent with Retrieval-Augmented Generation (RAG); The retrieved information provides additional context to the model; Additional context can make the model's response more focused.",
        "passage": None,
        "points": 1
    },
    {
        "id": "W11-Q8",
        "week": 11,
        "type": "multi",
        "question": "The lecture uses the example of the 2011 ICC World Cup to explain the effect of retrieval-augmented generation. Which of the following correctly captures the idea?",
        "options": [
            "Additional retrieved information can contextualize an otherwise ambiguous query",
            "The original question can be effectively shifted toward a more appropriate contextual representation",
            "RAG works primarily by increasing the number of parameters in the LLM",
            "A richer context can increase the probability of producing the intended response"
        ],
        "answer": [0, 1, 3],
        "explanation": "Accepted answer: Additional retrieved information can contextualize an otherwise ambiguous query; The original question can be effectively shifted toward a more appropriate contextual representation; A richer context can increase the probability of producing the intended response.",
        "passage": None,
        "points": 1
    },
    {
        "id": "W11-Q9",
        "week": 11,
        "type": "multi",
        "question": "Which of the following statements about hallucination are correct according to the lecture?",
        "options": [
            "A model may produce a plausible answer even when the generated information does not match the ground truth.",
            "Hallucination can occur when the model has insufficiently represented information in context",
            "Hallucination can be reduced through techniques such as providing context but it cannot necessarily be eliminated completely.",
            "Hallucination means that the model has deliberately decided to provide false information"
        ],
        "answer": [0, 1, 2],
        "explanation": "Accepted answer: A model may produce a plausible answer even when the generated information does not match the ground truth; Hallucination can occur when the model has insufficiently represented information in context; Hallucination can be reduced through techniques such as providing context but it cannot necessarily be eliminated completely.",
        "passage": None,
        "points": 1
    },
    {
        "id": "W11-Q10",
        "week": 11,
        "type": "multi",
        "question": "A language model produces a misleading recommendation because a false or deliberately misleading article was present in the information from which the model learned. Which statements are appropriate?",
        "options": [
            "The problem is necessarily an example of hallucination",
            "AI systems can potentially propagate misinformation present in their information sources",
            "A response may be misleading even when it is not simply an invented fact by the model",
            "Independent verification of important AI-generated information remains necessary."
        ],
        "answer": [1, 2, 3],
        "explanation": "Accepted answer: AI systems can potentially propagate misinformation present in their information sources; A response may be misleading even when it is not simply an invented fact by the model; Independent verification of important AI-generated information remains necessary.",
        "passage": None,
        "points": 1
    },

    # =========================================================================
    # WEEK 12 ASSIGNMENT (image-34.png, image-35.png, image-36.png)
    # =========================================================================
    {
        "id": "W12-Q1",
        "week": 12,
        "type": "multi",
        "question": "Which of the following statements are correct in distinguishing course-based education from research-based education as discussed in the lecture?",
        "options": [
            "Course-based education primarily deals with an existing body of knowledge, whereas PhD research is expected to create new knowledge.",
            "A PhD programme follows a common prescribed syllabus and curriculum in the same way as a course-based degree.",
            "Course-based education generally has a prescribed syllabus and curriculum, whereas research-based education does not simply follow a fixed syllabus.",
            "Knowledge in course-based education and new knowledge generated through PhD research are evaluated in exactly the same way."
        ],
        "answer": [0, 2],
        "explanation": "Accepted answer: Course-based education primarily deals with an existing body of knowledge, whereas PhD research is expected to create new knowledge; Course-based education generally has a prescribed syllabus and curriculum, whereas research-based education does not simply follow a fixed syllabus.",
        "passage": None,
        "points": 1
    },
    {
        "id": "W12-Q2",
        "week": 12,
        "type": "multi",
        "question": "A research scholar is beginning a PhD and expects the research guide to provide a complete step-by-step procedure for the entire research programme. Which responses are consistent with the lecture?",
        "options": [
            "The scholar should recognize that PhD research involves substantially self-directed work.",
            "The absence of a fixed syllabus means that the scholar does not need guidance from the research guide.",
            "The research guide can provide guidance and support when ambiguity or difficulty arises.",
            "The scholar is expected to develop the ability to decide how the research should progress."
        ],
        "answer": [0, 2, 3],
        "explanation": "Accepted answer: The scholar should recognize that PhD research involves substantially self-directed work; The research guide can provide guidance and support when ambiguity or difficulty arises; The scholar is expected to develop the ability to decide how the research should progress.",
        "passage": None,
        "points": 1
    },
    {
        "id": "W12-Q3",
        "week": 12,
        "type": "multi",
        "question": "A researcher proposes a hypothesis based on existing knowledge and experience. Which conditions, according to the lecture, are relevant to treating it as a scientific hypothesis?",
        "options": [
            "It should be an educated prediction rather than a statement already established as true.",
            "It should allow a possibility of being disproved.",
            "It should be protected from contradictory observations by adding explanations that cannot be tested.",
            "Its truth must be established before experiments or data collection begin."
        ],
        "answer": [0, 1],
        "explanation": "Accepted answer: It should be an educated prediction rather than a statement already established as true; It should allow a possibility of being disproved (falsifiability criterion).",
        "passage": None,
        "points": 1
    },
    {
        "id": "W12-Q4",
        "week": 12,
        "type": "multi",
        "question": "Consider the hypothesis: 'All swans are white.' Based on the falsifiability example in the lecture, which statements are correct?",
        "options": [
            "Finding a single black swan would provide an observation capable of disproving the hypothesis.",
            "It is necessary to observe every swan in the world before the hypothesis can be scientifically examined.",
            "The possibility of disproving the hypothesis is central to the criterion discussed in the lecture.",
            "The criterion discussed emphasizes the possibility of disproof rather than establishing the hypothesis as permanently true."
        ],
        "answer": [0, 2, 3],
        "explanation": "Accepted answer: Finding a single black swan would provide an observation capable of disproving the hypothesis; The possibility of disproving the hypothesis is central to the criterion discussed in the lecture; The criterion discussed emphasizes the possibility of disproof rather than establishing the hypothesis as permanently true.",
        "passage": None,
        "points": 1
    },
    {
        "id": "W12-Q5",
        "week": 12,
        "type": "multi",
        "question": "A student starts a PhD after being given a broad research topic. According to the lecture, which actions are appropriate before arriving at a testable hypothesis?",
        "options": [
            "Begin by formulating relevant questions about the topic and considering why the topic is important.",
            "Start an unrestricted literature survey immediately and use it as the only route for identifying the research problem.",
            "Use literature exploration and observations to refine the initial questions through repeated cycles.",
            "Formulate the final testable hypothesis immediately from the broad topic without further exploration."
        ],
        "answer": [0, 2],
        "explanation": "Accepted answer: Begin by formulating relevant questions about the topic and considering why the topic is important; Use literature exploration and observations to refine the initial questions through repeated cycles.",
        "passage": None,
        "points": 1
    },
    {
        "id": "W12-Q6",
        "week": 12,
        "type": "multi",
        "question": "In the obesity and food habit example, observations from the literature and study were used to identify an anomaly and develop a hypothesis. Which statements are supported by the lecture?",
        "options": [
            "An anomaly can arise when observations do not match a commonly assumed explanation.",
            "The observed influence of factors such as the amount of food offered can motivate further investigation.",
            "The hypothesis was formulated directly from the topic without any literature survey or observations.",
            "Identifying a missing link or contradiction can provide scope for further research and help generate a hypothesis."
        ],
        "answer": [0, 1, 3],
        "explanation": "Accepted answer: An anomaly can arise when observations do not match a commonly assumed explanation; The observed influence of factors such as the amount of food offered can motivate further investigation; Identifying a missing link or contradiction can provide scope for further research and help generate a hypothesis.",
        "passage": None,
        "points": 1
    },
    {
        "id": "W12-Q7",
        "week": 12,
        "type": "multi",
        "question": "According to the Revised Bloom's Taxonomy discussed in the lecture, which statements are correct?",
        "options": [
            "Remember, Understand and Apply are described as lower-order thinking levels.",
            "Analyze, Evaluate and Create are described as higher-order thinking levels.",
            "Create is placed below Remember because generating an idea generally requires minimal cognitive effort.",
            "The taxonomy states that every individual experiences exactly the same difficulty across all six levels."
        ],
        "answer": [0, 1],
        "explanation": "Accepted answer: Remember, Understand and Apply are described as lower-order thinking levels; Analyze, Evaluate and Create are described as higher-order thinking levels.",
        "passage": None,
        "points": 1
    },
    {
        "id": "W12-Q8",
        "week": 12,
        "type": "multi",
        "question": "A PhD scholar collects experimental data, examines unfamiliar patterns, considers alternative hypotheses, and develops a new research model. Which Bloom's levels are most directly represented in these activities?",
        "options": [
            "Analyze",
            "Evaluate",
            "Remember",
            "Create"
        ],
        "answer": [0, 1, 3],
        "explanation": "Accepted answer: Analyze; Evaluate; Create.",
        "passage": None,
        "points": 1
    },
    {
        "id": "W12-Q9",
        "week": 12,
        "type": "multi",
        "question": "Which statements correctly reflect the lecture's discussion of the role of higher-order thinking in PhD research?",
        "options": [
            "All six levels of thinking may be used during research problem solving.",
            "The lecture identifies analysis as an important starting level in PhD research because researchers collect and analyze data.",
            "The main intellectual focus of a PhD is memorizing information from the existing body of knowledge.",
            "Evaluation can involve considering alternate hypotheses and attempting to validate them."
        ],
        "answer": [0, 1, 3],
        "explanation": "Accepted answer: All six levels of thinking may be used during research problem solving; The lecture identifies analysis as an important starting level in PhD research because researchers collect and analyze data; Evaluation can involve considering alternate hypotheses and attempting to validate them.",
        "passage": None,
        "points": 1
    },
    {
        "id": "W12-Q10",
        "week": 12,
        "type": "multi",
        "question": "Which statements are consistent with the lecture's discussion of creativity and functional fixedness?",
        "options": [
            "Creative thinking can be developed or improved through practice rather than being limited to an ability fixed at birth.",
            "Functional fixedness can cause a person to perceive an object only through its conventional purpose and can hinder lateral thinking.",
            "Complete knowledge of the existing body of knowledge guarantees the creation of something new.",
            "Functional fixedness helps researchers generate new approaches when unexpected results emerge."
        ],
        "answer": [0, 1],
        "explanation": "Accepted answer: Creative thinking can be developed or improved through practice rather than being limited to an ability fixed at birth; Functional fixedness can cause a person to perceive an object only through its conventional purpose and can hinder lateral thinking.",
        "passage": None,
        "points": 1
    }
]

out_path = r'd:\Interview\SAA\NPTEL\quiz_data\weekly_assignments.json'
with open(out_path, 'w', encoding='utf-8') as f:
    json.dump(weekly_questions, f, indent=2, ensure_ascii=False)

print(f"Successfully saved {len(weekly_questions)} authentic weekly test questions to {out_path}")
