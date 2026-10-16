# -*- coding: utf-8 -*-
import json
import os

questions = []

def add_q(mod_id, q_text, options, answer, exp, q_type='single', passage=None):
    questions.append({
        'id': 100 + len(questions) + 1,
        'module': mod_id,
        'type': q_type,
        'question': q_text,
        'options': options,
        'answer': answer,
        'explanation': exp,
        'passage': passage
    })

# MODULE 11: Word Processing with Bibliographic Sources (Lecture 11)
add_q(11, 'Where does Microsoft Word store its master bibliographic database across documents on a Windows machine?',
      ['Sources.xml in the user’s AppData\\Roaming\\Microsoft\\Bibliography directory',
       'Registry entry HKEY_LOCAL_MACHINE\\Software\\Microsoft\\Office',
       'In the root C:\\Windows\\System32 directory',
       'Directly inside the computer BIOS firmware'],
      0,
      'Word stores its global bibliographic master list in Sources.xml, which allows references to be reused across different Word documents.')

add_q(11, 'In Microsoft Word’s native citation manager, what is the difference between the Master List and the Current List?',
      ['Master List contains all sources ever entered or imported on that PC; Current List contains sources cited in the active document',
       'Master List only stores journal articles; Current List only stores websites',
       'Master List is deleted whenever Word is closed; Current List is permanent',
       'Current List is synchronized with the cloud; Master List is kept offline'],
      0,
      'The Master List persists on the local computer across all sessions, while the Current List is embedded specifically within the open document.')

add_q(11, 'Which tool or script is commonly used to convert a standard BibTeX (.bib) file into Word’s native XML format (Sources.xml)?',
      ['Bib2Word (or JabRef export to MS-Word XML format)',
       'Notepad.exe find-and-replace command',
       'Adobe Acrobat Reader export function',
       'Windows PowerShell format-volume command'],
      0,
      'Tools like Bib2Word or JabRef’s built-in export to MS Office Bibliography XML allow seamless transfer of BibTeX references into Word.')

add_q(11, 'What is the XML tag used in Word’s bibliography XML schema to store the unique citation tag/key?',
      ['<b:Tag>', '<b:CitationKey>', '<b:ID>', '<b:KeyName>'],
      0,
      'Word’s bibliographic XML uses the <b:Tag> element to represent the citation identifier.')

add_q(11, 'When updating citations and bibliography in Microsoft Word, which key combination updates selected fields or entire document fields?',
      ['F9', 'F5', 'Ctrl + Alt + Del', 'Alt + F4'],
      0,
      'Pressing F9 in Word refreshes/updates dynamic fields, including cross-references, table of contents, and bibliography blocks.')

add_q(11, 'State whether True or False: In Microsoft Word, when you change the citation style (e.g., from IEEE to APA 7th), Word automatically re-formats both the in-text citations and the bibliography.',
      ['True', 'False'],
      0,
      'True. Word’s dynamic citation engine automatically updates both inline references and the terminal reference list according to the selected XSL stylesheet.')

add_q(11, 'Which file extension defines the citation formatting stylesheets used by Microsoft Word?',
      ['.xsl (XSLT stylesheets in the Word Bibliography\\Style folder)',
       '.css (Cascading Style Sheets)',
       '.exe (Executable binaries)',
       '.dll (Dynamic Link Libraries)'],
      0,
      'Word uses XSLT (.xsl) transformation stylesheets to format bibliographic entries according to specific style guidelines.')

add_q(11, 'What is a major limitation of using Microsoft Word’s built-in citation tool compared to dedicated managers like Zotero or EndNote?',
      ['Inability to directly sync with online scholarly databases, lack of PDF metadata extraction, and limited built-in citation styles',
       'Word does not permit typing text in English',
       'Word cannot save documents to a local hard drive',
       'Word requires manual recalculation of all mathematical tables'],
      0,
      'Word’s native bibliography tool lacks web browser connectors, PDF auto-indexing, and flexible tag synchronization provided by dedicated managers.')

add_q(11, 'In Microsoft Word, what does the "Placeholder" citation feature allow a researcher to do?',
      ['Insert a temporary citation tag in the text while writing and fill in the full bibliographic details later in Source Manager',
       'Prevent other authors from viewing the document text',
       'Generate random lorem ipsum text paragraphs',
       'Encrypt the manuscript before email submission'],
      0,
      'Placeholders let writers mark the location of a reference without interrupting their writing flow to input full source metadata.')

add_q(11, 'How can you convert dynamic Word citation fields into static plain text before final journal submission?',
      ['Select the field and press Ctrl + Shift + F9 (or unlink fields command)',
       'Press Ctrl + S three times quickly',
       'Restart the computer in safe mode',
       'Change the display font size to 10pt'],
      0,
      'Ctrl + Shift + F9 permanently unlinks dynamic fields in Word, converting them into plain, uneditable static text.')

# MODULE 12: Using EndNote & Citation Plugins (Part 1 - Lectures 12 & 13)
add_q(12, 'What is the proprietary file extension used by EndNote for its desktop reference library file?',
      ['.enl (accompanied by a corresponding .Data folder)',
       '.bib', '.doc', '.end'],
      0,
      'EndNote stores reference collections in an .enl file accompanied by an associated .Data folder holding attachments and databases.')

add_q(12, 'What happens if a user copies an EndNote .enl file to another computer but forgets to copy the accompanying .Data folder?',
      ['The library opens but lacks all attached PDFs, figure attachments, and internal index links',
       'The computer crashes and deletes the operating system',
       'The .enl file is automatically converted into an Excel spreadsheet',
       'EndNote charges a penalty fee to restore the library'],
      0,
      'The .enl file is only a pointer index; all actual PDFs, figures, and full-text databases reside in the .Data folder.')

add_q(12, 'What is the name of the Microsoft Word plugin installed with EndNote that enables interactive citation insertion?',
      ['Cite While You Write (CWYW)',
       'Write-N-Cite',
       'Paperpile Word Link',
       'EndNote FastType'],
      0,
      'EndNote’s Microsoft Word toolbar and plugin is called Cite While You Write (CWYW).')

add_q(12, 'When CWYW is in unformatted citation mode, how do EndNote temporary citations appear in the Word document body?',
      ['Enclosed in curly braces: {Author, Year #RecordNumber}',
       'Enclosed in square brackets: [Author, Year]',
       'Enclosed in HTML tags: <citation id="123">',
       'Enclosed in double quotes: "Author, Year"'],
      0,
      'Unformatted EndNote citations appear as {Author, Year #RecordNumber}, which CWYW transforms into formatted citations upon command.')

add_q(12, 'Which feature in EndNote Desktop automatically monitors a specific folder and imports newly downloaded research PDFs?',
      ['PDF Auto-Import Folder',
       'Trash Bin Auto-Empty',
       'Online Search Sync',
       'Library Sharing Manager'],
      0,
      'The PDF Auto-Import folder monitors designated local folders, imports new PDFs, and queries DOI servers to populate bibliographic fields.')

add_q(12, 'State whether True or False: In EndNote, modifying the citation output style (e.g., from Nature to IEEE) alters the underlying data inside your EndNote library.',
      ['True', 'False'],
      1,
      'False. Output styles only change how data is displayed/formatted in the document; the underlying records in the EndNote library remain untouched.')

add_q(12, 'How does EndNote extract metadata (authors, title, journal) from an imported PDF document?',
      ['By scanning the first pages for a Digital Object Identifier (DOI) and querying CrossRef / PubMed databases via the internet',
       'By using human transcription workers via Amazon Mechanical Turk',
       'By reading the filename of the PDF file only',
       'By analyzing the date and time the file was downloaded'],
      0,
      'EndNote scans the document for embedded DOIs and queries scientific registries like CrossRef to retrieve exact metadata.')

add_q(12, 'What is an "EndNote Compressed Library" file extension, useful for emailing complete libraries?',
      ['.enlx', '.zip', '.rar', '.7z'],
      0,
      'An .enlx file is a compressed archive containing both the .enl file and the entire .Data folder.')

add_q(12, 'In EndNote Term Lists, why is importing the "Medical" or "Bioscience" Journal Terms List recommended?',
      ['It enables automated conversion between full journal names and official standard ISO/NLM abbreviations required by different journals',
       'It provides medical diagnoses for laboratory researchers',
       'It increases the computer processor speed during citation insertion',
       'It translates foreign medical terms into Latin automatically'],
      0,
      'Journal Terms Lists map full journal names to their official abbreviations so EndNote can switch between styles without manual editing.')

add_q(12, 'What command in Word CWYW allows you to edit an existing citation to add page numbers or suppress the author\'s name?',
      ['Edit & Manage Citation(s)',
       'Delete Citation',
       'Convert to Unformatted',
       'Export to EndNote'],
      0,
      'Edit & Manage Citation(s) allows customizing individual citations, such as excluding author, excluding year, or adding specific cited pages.')

# MODULE 13: Using EndNote & Citation Customization (Part 2)
add_q(13, 'In the EndNote Style Editor, what does the "Link Adjacent Text" symbol (|) accomplish in a bibliography template?',
      ['It forces adjacent text or punctuation to appear only if the associated field contains data',
       'It splits the author list across two separate lines',
       'It inserts a vertical bar character literally into the printed citation',
       'It deletes the preceding word from the bibliography'],
      0,
      'The vertical bar (|) links punctuation to a specific field so punctuation does not print if the field is empty (e.g., avoiding dangling commas).')

add_q(13, 'In EndNote bibliography templates, what is the purpose of the "Forced Separation" symbol (|)?',
      ['To separate text from an adjacent field so they are treated as independent elements',
       'To disconnect the computer from the local network',
       'To divide the bibliography into two equal columns',
       'To force a page break before every reference'],
      0,
      'Forced separation isolates non-field text from adjacent fields to prevent dependent formatting rules from suppressing desired punctuation.')

add_q(13, 'In EndNote citation style templates, what does the "Non-breaking space" (accent grave ` or small circle) prevent?',
      ['It prevents a line break from occurring between two terms, such as "Vol." and the volume number',
       'It prevents the user from saving the file',
       'It deletes extra blank spaces between paragraphs',
       'It disables spelling check for foreign author names'],
      0,
      'Non-breaking spaces keep associated elements (like "p." and page number) together on the same line.')

add_q(13, 'How does EndNote handle multiple citations appearing at the exact same location in the text (e.g., [1, 2, 3])?',
      ['Through "Citation Clustering" rules defined in the Output Style (Numbering / Citation sort order)',
       'By creating separate paragraphs for each citation number',
       'By averaging the reference numbers into a single decimal number',
       'By deleting all citations except the first one entered'],
      0,
      'Citation styles define grouping and sorting rules that compress consecutive citations (e.g., [1-4]) or sort them alphabetically/chronologically.')

add_q(13, 'State whether True or False: You should manually type additions or deletions directly inside grey-shaded EndNote field codes in Microsoft Word.',
      ['True', 'False'],
      1,
      'False. Typing directly into active field codes corrupts the document; changes must be made via "Edit & Manage Citation(s)" or the EndNote library.')

add_q(13, 'What is the "Export Traveling Library" feature in Word CWYW used for?',
      ['Extracting reference metadata embedded inside a colleague\'s Word document into your own EndNote desktop library',
       'Exporting citations onto a USB flash drive for international travel',
       'Printing physical library index cards on cardstock paper',
       'Translating the document into the language of the destination country'],
      0,
      'Traveling Library allows extracting references from a document even if you do not have the author’s original EndNote library file.')

add_q(13, 'Which EndNote feature allows multiple researchers across different universities to collaborate on a single synchronized library?',
      ['EndNote Library Sharing (via EndNote Sync / EndNote Web cloud)',
       'Sending individual screenshot images of references over chat',
       'Burning weekly CD-ROM updates and mailing them',
       'Using a shared thumb drive connected to a router'],
      0,
      'EndNote Sync enables cloud synchronization and sharing of libraries with permission control for collaborative research teams.')

add_q(13, 'What does the "Find Full Text" command in EndNote Desktop execute?',
      ['It authenticates via institutional OpenURL / EZProxy to automatically locate and attach full-text PDFs to existing library records',
       'It conducts a Google search for the author\'s biography',
       'It downloads the entire Wikipedia encyclopedia onto the hard drive',
       'It prints the full text of all papers on the local office printer'],
      0,
      'Find Full Text uses DOI, PubMed ID, and institutional library proxy settings to automatically find and download PDFs.')

add_q(13, 'What is the primary function of the "Deduplication" tool in EndNote?',
      ['Identifying and merging/deleting duplicate records imported from multiple databases during a systematic review',
       'Detecting plagiarized sentences inside imported PDFs',
       'Checking for duplicated words inside the student\'s thesis',
       'Splitting dual-authored papers into separate entries'],
      0,
      'Deduplication identifies identical records imported from multiple sources (e.g., WoS and Scopus) based on configurable matching fields.')

add_q(13, 'Before submitting a final manuscript to a publisher that does not support EndNote field codes, what step should you take?',
      ['Save a backup copy, then run "Convert to Plain Text" to strip CWYW field codes',
       'Delete the bibliography section from the paper completely',
       'Change all fonts to Comic Sans MS',
       'Encrypt the document with a 256-bit password'],
      0,
      'Converting to plain text removes active field codes, preventing corruption or error messages when processed by publisher typesetting systems.')

# MODULE 14: Peer Review Process & Scientific Communication
add_q(14, 'What is the primary purpose of the peer review process in scientific publishing?',
      ['To evaluate research manuscripts for technical rigor, originality, scientific validity, and adherence to ethical standards',
       'To correct spelling errors and verify the author\'s bank balance',
       'To guarantee that the paper will be cited more than 1,000 times',
       'To ensure that only researchers from famous universities are allowed to publish'],
      0,
      'Peer review provides expert evaluation of methodological soundness, data integrity, significance, and novelty before formal publication.')

add_q(14, 'What defines a "Single-Blind" peer review system?',
      ['The reviewers know the identities of the authors, but the authors do not know the identities of the reviewers',
       'Both the authors and the reviewers remain anonymous to each other',
       'The reviewers are blindfolded while reading the printed manuscripts',
       'The public reads the paper before the journal editors see it'],
      0,
      'In single-blind review, reviewers know author names and institutions, but reviewer identities are withheld from authors.')

add_q(14, 'What defines a "Double-Blind" peer review system?',
      ['Both author identities and reviewer identities are concealed from each other throughout the review process',
       'The editor is not permitted to read the title of the manuscript',
       'Two independent reviewers must reject the paper simultaneously',
       'The paper is reviewed twice by the same reviewer six months apart'],
      0,
      'Double-blind review anonymizes both parties to minimize biases related to author prestige, gender, nationality, or affiliation.')

add_q(14, 'What is "Open Peer Review"?',
      ['A transparent review model where reviewer identities, review reports, and author responses are openly published alongside the article',
       'Allowing any anonymous internet user to vote on whether a paper is accepted',
       'Publishing papers without any editorial assessment',
       'Reviewing manuscripts during a live televised video conference'],
      0,
      'Open peer review fosters transparency and accountability by disclosing reviewer names and publishing reviewer comments.')

add_q(14, 'What does a "Desk Reject" (or Summary Rejection) by a journal editor signify?',
      ['The editor rejects the manuscript without sending it out for external peer review because it is out of scope or lacks basic quality',
       'The reviewer accidentally knocked the manuscript off their physical desk',
       'The journal has run out of paper at the printing press',
       'The author failed to pay the optional color printing fee'],
      0,
      'A desk reject occurs when an editor decides that a manuscript does not fit the journal’s scope, lacks novelty, or has fatal flaws.')

add_q(14, 'When responding to reviewer comments on a revised manuscript, how should authors structure their response document?',
      ['Provide a point-by-point response, quoting each reviewer comment, followed by a polite, detailed reply and exact page/line changes',
       'Dismiss reviewer criticisms as incompetent and demand immediate publication',
       'Ignore difficult questions and answer only simple stylistic comments',
       'Send a generic one-sentence email stating that changes have been made'],
      0,
      'Authors must provide a respectful, comprehensive, point-by-point response specifying exactly how each comment was addressed in the manuscript.')

add_q(14, 'State whether True or False: Authors are obligated to agree with every single criticism made by a reviewer and must change their conclusions accordingly.',
      ['True', 'False'],
      1,
      'False. Authors may respectfully disagree with a reviewer provided they present sound scientific rationale, additional data, or literature evidence.')

add_q(14, 'What constitutes a "Conflict of Interest" (COI) for an invited peer reviewer?',
      ['Recent co-authorship, personal relationship, financial ties, or direct institutional/intellectual rivalry with the authors',
       'Reviewing papers while sitting in a coffee shop',
       'Holding a PhD degree in the same broad engineering discipline',
       'Having read previous papers published in the same journal'],
      0,
      'COIs arise from personal, professional, or financial ties that could compromise objective and impartial evaluation.')

add_q(14, 'What does the term "Post-Publication Peer Review" refer to?',
      ['Ongoing scientific critique, replication attempts, comments, and discussions on platforms like PubPeer after a paper is published',
       'Publishing a second edition of a textbook ten years later',
       'Printing letters to the editor in the daily newspaper',
       'A university committee awarding tenure to a faculty member'],
      0,
      'Post-publication review allows the scientific community to scrutinize published claims, detect irreproducible data, or identify errors.')

add_q(14, 'What is the responsibility of a peer reviewer regarding the confidentiality of a manuscript under review?',
      ['Treat the manuscript as strictly confidential; never share, cite, or use unpublished ideas or data from it prior to publication',
       'Share the manuscript with graduate students to help them write their own papers',
       'Upload the manuscript to public social media platforms for discussion',
       'Incorporate the manuscript\'s equations into one\'s own active grant proposal'],
      0,
      'Reviewers are bound by strict confidentiality; using or disseminating unpublished information from reviewed manuscripts is serious misconduct.')

# MODULE 15: Experimental Skills, Measurement & Error Mitigation
add_q(15, 'What is the fundamental distinction between "accuracy" and "precision" in experimental measurement?',
      ['Accuracy reflects closeness to the true reference value; precision reflects closeness of repeated measurements to each other',
       'Accuracy refers to electronic displays; precision refers to analog needle gauges',
       'Accuracy is measured in kilograms; precision is measured in seconds',
       'Accuracy and precision are mathematically identical synonyms'],
      0,
      'Accuracy measures proximity to the true or accepted standard, while precision measures reproducibility and repeatability.')

add_q(15, 'What is a "Systematic Error" (bias), and how can it be eliminated or minimized?',
      ['A reproducible, directional offset caused by faulty calibration or ambient conditions, corrected through calibration and zero-adjustments',
       'Unpredictable random fluctuations eliminated by closing the laboratory window',
       'Typographical mistakes made while typing numbers into an electronic calculator',
       'Errors caused exclusively by student inattention during morning hours'],
      0,
      'Systematic errors shift measurements predictably in one direction and are corrected through calibration, zeroing, and baseline correction.')

add_q(15, 'What is a "Random Error", and what is the primary statistical technique used to mitigate its impact?',
      ['Unpredictable statistical fluctuations in measurement, mitigated by repeating measurements and computing the mean and standard error',
       'A deliberate calculation error that cannot be reduced by any mathematical method',
       'An error caused by using the wrong unit system (e.g., inches instead of centimeters)',
       'An error that occurs only once every leap year'],
      0,
      'Random errors are unbiased stochastic fluctuations; averaging multiple repeated measurements significantly reduces uncertainty.')

add_q(15, 'According to the Hierarchy of Science discussed in Lecture 15, what is the ultimate arbiter when theoretical predictions disagree with rigorous, repeatable experiments?',
      ['The experiment: "If it disagrees with experiment, it is wrong" (Richard Feynman)',
       'The mathematical elegance and beauty of the theoretical equation',
       'The academic seniority and prestige of the theoretical physicist',
       'A majority vote conducted among university professors'],
      0,
      'Feynman famously stated: "It does not matter how beautiful your theory is... if it disagrees with experiment, it is wrong."')

add_q(15, 'State whether True or False: In experimental science, a measurement without an associated statement of uncertainty (error bar) is scientifically incomplete.',
      ['True', 'False'],
      0,
      'True. Scientific measurements are incomplete without quantifiable uncertainty bounds (error limits or confidence intervals).')

add_q(15, 'What is the purpose of a "Negative Control" in an experimental design?',
      ['To demonstrate that no effect occurs in the absence of the independent experimental variable/treatment',
       'To ensure that the experiment produces completely negative emotional feelings',
       'To prove that all laboratory instruments are functioning at maximum voltage',
       'To eliminate the necessity of measuring baseline background noise'],
      0,
      'Negative controls verify that the experimental setup does not produce a false positive response when the active treatment is omitted.')

add_q(15, 'What is the purpose of a "Positive Control" in an experimental design?',
      ['To verify that the experimental system and reagents are capable of detecting a known response under established conditions',
       'To ensure the experimenter remains in a positive psychological mood',
       'To guarantee that the experimental findings will be approved by patent examiners',
       'To replace the need for measuring the experimental sample'],
      0,
      'Positive controls demonstrate that the assay or detector is functioning correctly by verifying a known, expected positive result.')

add_q(15, 'When propagating independent random errors in a formula Z = X + Y, how is the absolute uncertainty delta_Z computed?',
      ['By adding the individual uncertainties in quadrature: delta_Z = sqrt((delta_X)^2 + (delta_Y)^2)',
       'By simply multiplying delta_X and delta_Y together',
       'By subtracting delta_Y from delta_X',
       'By taking the arithmetic mean of delta_X and delta_Y'],
      0,
      'For independent uncorrelated random errors in addition or subtraction, uncertainties add in quadrature (root sum of squares).')

add_q(15, 'What is "Hysteresis" in experimental instrumentation?',
      ['A phenomenon where the instrument’s output depends on its previous history (different reading when approaching a value from below vs above)',
       'The overheating of electronic circuits when exposed to sunlight',
       'The permanent destruction of measuring equipment due to mechanical shock',
       'The speed at which an analog needle returns to zero after power is shut down'],
      0,
      'Hysteresis occurs when the measurement curve during loading differs from unloading due to internal friction, memory, or lag.')

add_q(15, 'What is "Parallax Error" in experimental reading, and how is it prevented?',
      ['Apparent shift in the position of a needle/meniscus due to viewing at an angle; prevented by viewing line-of-sight perpendicular to the scale',
       'An electronic glitch caused by static electricity on plastic voltmeter screens',
       'An error in mathematical division when using logarithmic graph paper',
       'A failure of the laboratory air conditioning system to maintain 25°C'],
      0,
      'Parallax error arises from an oblique viewing angle relative to the scale; aligning the line of sight perpendicularly eliminates it.')

# MODULE 16: LaTeX Typesetting & Overleaf Collaboration
add_q(16, 'What is Overleaf in the context of scientific technical writing?',
      ['A cloud-based, collaborative LaTeX editor that allows real-time co-authoring, version control, and automated cloud compilation',
       'A desktop spreadsheet software used for accounting',
       'A proprietary graphics editing suite for 3D animation',
       'A compiler used exclusively for writing Android smartphone applications'],
      0,
      'Overleaf is the leading browser-based collaborative LaTeX platform with real-time compilation and version history.')

add_q(16, 'In LaTeX, what command is used to include an external image file (e.g., PNG or PDF) into a document?',
      ['\\includegraphics[options]{filename}',
       '\\insertimage{filename}',
       '\\picture{filename}',
       '\\openimage{filename}'],
      0,
      '\\includegraphics (from the graphicx package) is the standard command to include graphics in LaTeX.')

add_q(16, 'Which package must be loaded in the LaTeX preamble to enable \\includegraphics and image scaling?',
      ['graphicx', 'tikz', 'amsmath', 'geometry'],
      0,
      'The \\usepackage{graphicx} declaration is required to manipulate and insert external graphical images.')

add_q(16, 'How do you cross-reference a figure, table, or equation in LaTeX so that the numbering updates automatically?',
      ['Assign a unique \\label{key} inside the float/equation and refer to it with \\ref{key} in the text',
       'Type the static number manually into the text (e.g., "Figure 1")',
       'Use the \\footnote{key} command',
       'Use the \\cite{key} command'],
      0,
      'LaTeX achieves dynamic cross-referencing by pairing \\label{marker} with \\ref{marker}.')

add_q(16, 'State whether True or False: In LaTeX, a tilde (~) placed between a word and a cross-reference (e.g., Figure~\\ref{fig1}) creates a non-breaking space.',
      ['True', 'False'],
      0,
      'True. The tilde (~) acts as a tie or non-breaking space, preventing "Figure" and its number from being split across separate lines.')

add_q(16, 'In LaTeX mathematical environments, what command generates a Greek letter uppercase Omega?',
      ['\\Omega', '\\omega', '\\Delta', '\\Sigma'],
      0,
      '\\Omega produces the uppercase Greek letter Omega, whereas \\omega produces lowercase omega.')

add_q(16, 'What is the purpose of the \\newcommand declaration in a LaTeX document preamble?',
      ['To define custom user-created macros or shortcut commands to reduce repetitive typing',
       'To purchase additional cloud storage on Overleaf',
       'To download external software drivers for computer printers',
       'To switch the language of the LaTeX compiler interface'],
      0,
      '\\newcommand creates custom shorthand macros, ensuring consistent notation throughout a long manuscript.')

add_q(16, 'In Overleaf, which version control system can be integrated directly with projects for repository synchronization?',
      ['Git (via Overleaf Git Bridge / GitHub integration)',
       'Subversion (SVN)',
       'Mercurial',
       'BVS'],
      0,
      'Overleaf provides native Git access and direct GitHub synchronization for version control and offline editing.')

add_q(16, 'What does the LaTeX package "amsmath" provide to scientific researchers?',
      ['Advanced mathematical formatting structures, including align, subequations, bmatrix, and split environments',
       'Automated translation of documents into foreign languages',
       'A tool for balancing chemical reaction equations automatically',
       'A spreadsheet engine for computing student exam marks'],
      0,
      'The American Mathematical Society package (amsmath) provides essential environments and symbols for complex mathematical expressions.')

add_q(16, 'When working with tables in LaTeX, what character is used to separate adjacent columns in a row?',
      ['& (Ampersand)',
       '% (Percent)',
       '# (Hash)',
       '\\ (Backslash)'],
      0,
      'The ampersand (&) acts as the column separator, and double backslash (\\\\) ends each row in LaTeX tabular environments.')

# MODULE 17: Foundations of Data Analysis & Statistical Inferencing
add_q(17, 'What is the fundamental difference between descriptive statistics and inferential statistics?',
      ['Descriptive statistics summarize and display observed sample data; inferential statistics draw conclusions about an unobserved population',
       'Descriptive statistics use calculus; inferential statistics use only subtraction',
       'Descriptive statistics are only used in social sciences; inferential statistics are only used in physics',
       'Descriptive statistics require computers; inferential statistics are calculated by hand'],
      0,
      'Descriptive statistics summarize sample properties, while inferential statistics use probability theory to estimate population parameters.')

add_q(17, 'In statistical estimation, what does it mean for an estimator to be "unbiased"?',
      ['The expected value (mathematical expectation) of the estimator equals the true population parameter being estimated: E[theta_hat] = theta',
       'The estimator produces zero error in every single individual trial',
       'The estimator was computed by an impartial independent researcher',
       'The estimator uses only integer values without decimals'],
      0,
      'An estimator is unbiased if its sampling distribution has a mean equal to the true parameter value.')

add_q(17, 'Why is sample variance calculated with divisor (n - 1) instead of n when estimating population variance (Bessel’s correction)?',
      ['Because dividing by n underestimates true population variance; dividing by (n - 1) removes bias and yields an unbiased estimator',
       'Because one observation is always assumed to be corrupted by lab error',
       'Because sample size in statistics must always be an odd number',
       'Because calculating square roots requires an even denominator'],
      0,
      'Bessel\'s correction (n - 1) compensates for the fact that sample deviations are measured from the sample mean rather than the true population mean.')

add_q(17, 'What is the Central Limit Theorem (CLT), and why is it foundational to experimental data analysis?',
      ['The distribution of the sample mean approaches a normal distribution as sample size increases, regardless of the underlying population distribution',
       'All physical phenomena in nature strictly follow a uniform probability distribution',
       'The error in an experiment always converges to zero if you wait long enough',
       'The variance of any sample is always equal to its mean'],
      0,
      'The CLT proves that the sum or average of independent random variables tends toward a normal distribution for sufficiently large n.')

add_q(17, 'State whether True or False: A 95% Confidence Interval for the mean implies that there is a 95% probability that the fixed population mean mu lies inside that specific computed numerical interval.',
      ['True', 'False'],
      1,
      'False. In frequentist statistics, mu is a fixed constant, not a random variable. The 95% refers to the procedure: 95% of such calculated intervals will enclose mu upon repeated sampling.')

add_q(17, 'What is the p-value in a statistical hypothesis test?',
      ['The probability, assuming the null hypothesis is true, of obtaining a test statistic at least as extreme as the observed value',
       'The probability that the alternative hypothesis is true',
       'The percentage of flawed data points in the sample',
       'The precision rating of the laboratory sensor'],
      0,
      'A p-value measures the probability of observing data as extreme as or more extreme than the actual sample, under the assumption that H0 holds.')

add_q(17, 'If a hypothesis test yields a p-value of 0.02 and the chosen significance level alpha is 0.05, what is the statistical decision?',
      ['Reject the null hypothesis (H0) because p < alpha',
       'Fail to reject the null hypothesis (H0) because p < alpha',
       'Discard the entire dataset and repeat the experiment',
       'Conclude that the sample size was too small'],
      0,
      'When p <= alpha, the observed effect is statistically significant at that alpha level, leading to the rejection of H0.')

add_q(17, 'Which statistical test is appropriate for comparing the means of two independent groups assuming normally distributed data with equal variances?',
      ['Two-sample independent Student\'s t-test',
       'Chi-square test of independence',
       'One-way ANOVA with 10 groups',
       'Kruskal-Wallis rank test'],
      0,
      'Student\'s two-sample independent t-test evaluates whether the difference between two sample means is statistically significant.')

add_q(17, 'What is the primary consequence of multicollinearity among independent variables in multiple linear regression?',
      ['Inflated standard errors of coefficient estimates, making individual predictors appear statistically insignificant despite high overall R^2',
       'The regression equation is rendered impossible to plot on a computer screen',
       'The model automatically forces the intercept term to zero',
       'Multicollinearity eliminates all random residuals from the model'],
      0,
      'Multicollinearity inflates coefficient variances, leading to unstable estimates and high p-values for individual predictors.')

add_q(17, 'What is the Variance Inflation Factor (VIF), and what threshold typically indicates problematic multicollinearity?',
      ['VIF measures how much variance of an estimated regression coefficient is inflated; VIF > 5 or 10 indicates severe multicollinearity',
       'VIF measures the inflation rate of laboratory equipment purchase prices; VIF > 1 indicates inflation',
       'VIF evaluates the speed of data transfer across Ethernet cables; VIF > 100 indicates latency',
       'VIF measures the atmospheric pressure inside cleanrooms; VIF < 1 indicates vacuum'],
      0,
      'VIF quantifies predictor collinearity; values exceeding 5 to 10 suggest severe variance inflation requiring remediation.')

# MODULE 18: Statistical Computing in R & RStudio Environment
add_q(18, 'What is RStudio in the context of scientific programming in R?',
      ['An integrated development environment (IDE) for R featuring a console, script editor, plotting window, and workspace manager',
       'A commercial hardware device used to connect sensors to computers',
       'A closed-source proprietary database engine developed by Microsoft',
       'A cloud backup service for storing digital photographs'],
      0,
      'RStudio is the premier open-source IDE for R programming, data science, visualization, and reproducible reporting.')

add_q(18, 'In R, which operator is the idiomatic standard assignment operator used to assign a value to an object?',
      ['<- (Left arrow)',
       '== (Double equals)',
       '~ (Tilde)',
       ':= (Colon equals)'],
      0,
      'The left arrow (<-) is the idiomatic standard assignment operator in R.')

add_q(18, 'Which core R function is used to fit a linear regression model using ordinary least squares?',
      ['lm(formula, data)',
       'glm(formula, family = gaussian)',
       'regress(y ~ x)',
       'fit_linear(data)'],
      0,
      'The lm() function (Linear Models) is R’s foundational tool for fitting linear regressions.')

add_q(18, 'In R regression syntax, what does the formula "y ~ x1 * x2" specify?',
      ['Fitting main effects of x1 and x2 PLUS their interaction term (equivalent to y ~ x1 + x2 + x1:x2)',
       'Multiplying column x1 by column x2 before performing a t-test',
       'Fitting only the interaction term without the main effects',
       'Dividing variable x1 by x2 and ignoring y'],
      0,
      'In R formula notation, the asterisk (*) expands to include both individual main effects and their two-way interaction.')

add_q(18, 'Which function in R provides comprehensive regression summary output including coefficients, t-values, p-values, and R-squared?',
      ['summary(model)',
       'print(model)',
       'details(model)',
       'inspect(model)'],
      0,
      'summary(model) displays full diagnostic statistics, parameter estimates, standard errors, t-statistics, and overall fit metrics.')

add_q(18, 'State whether True or False: In R, data frames allow different columns to have different data types (e.g., numeric, character, factor), while matrices require all elements to share the same data type.',
      ['True', 'False'],
      0,
      'True. Data frames are heterogeneous rectangular structures; matrices are homogeneous two-dimensional arrays.')

add_q(18, 'What does the function t.test(x, y, var.equal = TRUE) execute in R?',
      ['Student\'s two-sample t-test assuming equal population variances (pooled variance t-test)',
       'Welch\'s t-test with Satterthwaite degrees of freedom adjustment',
       'Paired samples t-test on repeated measures',
       'One-sample t-test against zero'],
      0,
      'Setting var.equal = TRUE invokes classical Student\'s t-test with pooled variance; the default in R is Welch\'s t-test.')

add_q(18, 'What is ggplot2 in the R statistical software ecosystem?',
      ['A widely used data visualization package based on the Grammar of Graphics framework developed by Hadley Wickham',
       'A package for designing graphical user interfaces in Java',
       'A command-line text editor for Unix terminals',
       'A hardware driver for color laser printers'],
      0,
      'ggplot2 implements Leland Wilkinson\'s Grammar of Graphics, building visual plots layer-by-layer.')

add_q(18, 'What is the function of the set.seed() command in R prior to running simulations or random sampling?',
      ['To initialize the pseudo-random number generator, ensuring identical, reproducible results across runs',
       'To plant agricultural experimental seeds in laboratory greenhouses',
       'To clear all active variables from the R global workspace memory',
       'To establish a secure encrypted connection to CRAN mirrors'],
      0,
      'set.seed() guarantees reproducibility by locking the starting state of the pseudo-random number generation sequence.')

add_q(18, 'In R, which function is used to perform Analysis of Variance (ANOVA) on a fitted linear model?',
      ['anova(model)',
       'variance(model)',
       'f_test(model)',
       'test_factors(model)'],
      0,
      'anova(model) computes the ANOVA table displaying sum of squares, mean squares, F-statistics, and p-values.')

# MODULE 19: First-Principles vs Empirical Modelling (Lecture 19A)
add_q(19, 'What defines a "First-Principles" (mechanistic / white-box) model in engineering research?',
      ['A model derived from fundamental physical conservation laws (mass, momentum, energy) and constitutive thermodynamic relations',
       'A model developed purely by fitting polynomial curves to measured experimental data points',
       'A model generated randomly by neural network algorithms without physical variables',
       'A model based solely on subjective hunches of senior technicians'],
      0,
      'First-principles models are built from governing physical laws (conservation of mass, energy, Navier-Stokes, Fourier\'s law, etc.).')

add_q(19, 'What defines an "Empirical" (data-driven / black-box) model in engineering research?',
      ['A model established purely from observed mathematical correlations between measured inputs and outputs without modeling underlying physical mechanisms',
       'A model derived entirely from quantum mechanical wave equations from scratch',
       'A model that cannot be simulated on modern computers',
       'A model that strictly uses Roman numerals for variables'],
      0,
      'Empirical models map input-output relationships mathematically from experimental datasets without explicit mechanistic derivation.')

add_q(19, 'What is a "Grey-Box" (hybrid) model in scientific research?',
      ['A hybrid model combining fundamental physical equations (known mechanisms) with data-driven empirical terms for unmodeled or complex dynamics',
       'A model displayed exclusively in grayscale on computer monitors',
       'A model whose mathematical derivation has been kept secret by a corporation',
       'A model that has failed three consecutive laboratory validation tests'],
      0,
      'Grey-box models leverage known physics for structure while using data-driven estimation for uncertain parameters or complex phenomena.')

add_q(19, 'What is a major advantage of first-principles mechanistic models over purely empirical models?',
      ['High extrapolation capability: ability to predict behavior outside tested experimental regimes where governing physical laws still hold',
       'Zero computational time required to solve differential equations',
       'No requirement for understanding physics or thermodynamics',
       'Guaranteed lack of differential or algebraic equations'],
      0,
      'Because they reflect underlying conservation laws, first-principles models generalize and extrapolate far better than empirical curves.')

add_q(19, 'What is a major limitation of first-principles models in complex industrial systems?',
      ['High mathematical complexity, difficult-to-determine physical parameters, and prohibitive computational cost for turbulent or reacting multi-phase flows',
       'They can only be used on mechanical systems and never on fluids',
       'They are illegal to publish under international copyright laws',
       'They can never be expressed in algebraic notation'],
      0,
      'Complex systems involve turbulent fluid dynamics, chemical kinetics, and fouling that make analytical first-principles models intractable.')

add_q(19, 'In the Liquid-Level Tank case study discussed in Lecture 19A, how does Level 1 modeling describe the system?',
      ['Pure empirical linear regression relating inlet valve position directly to steady-state liquid height',
       'Full 3D turbulent Navier-Stokes computational fluid dynamics simulation with volume of fluid free surface tracking',
       'A non-linear mass conservation ordinary differential equation incorporating Torricelli’s law of efflux',
       'A quantum mechanical simulation of fluid molecules'],
      0,
      'Lecture 19A illustrates a hierarchy of 5 modeling levels, starting from simple empirical curves up to rigorous non-linear dynamic differential equations.')

add_q(19, 'State whether True or False: An empirical polynomial model with R^2 = 0.999 is guaranteed to produce accurate predictions when extrapolating far beyond the tested range of experimental inputs.',
      ['True', 'False'],
      1,
      'False. High-order polynomials fitted to data often exhibit wild oscillations (Runge\'s phenomenon) and disastrous errors when extrapolating beyond training bounds.')

add_q(19, 'In dynamic system modeling, what is "lumped parameter" modeling compared to "distributed parameter" modeling?',
      ['Lumped parameter models assume spatially uniform properties (ordinary differential equations, ODEs); distributed parameter models account for spatial gradients (partial differential equations, PDEs)',
       'Lumped models are for liquids; distributed models are exclusively for solids',
       'Lumped models have no mathematical equations; distributed models have hundreds of tables',
       'Distributed models are solved by hand; lumped models require supercomputers'],
      0,
      'Lumped systems neglect spatial variations (ODEs in time); distributed systems model spatial dimensions explicitly (PDEs).')

add_q(19, 'What is "Parameter Identifiability" in mathematical modeling?',
      ['Whether the model parameters can be uniquely and reliably estimated from the available experimental input-output measurements',
       'Assigning employee identification numbers to researchers in a laboratory',
       'Labeling variables with Greek letters in the thesis appendix',
       'Checking if the computer processor supports 64-bit floating point arithmetic'],
      0,
      'Identifiability examines whether distinct parameter values yield distinct model outputs, ensuring unique mathematical solutions from data.')

add_q(19, 'Why are dimensionless numbers (e.g., Reynolds number, Nusselt number, Biot number) central to engineering modeling?',
      ['They collapse complex multiparameter relationships into universal scaling groups, enabling dynamic similitude and scale-up from lab prototypes to full industrial plants',
       'They eliminate the need to calculate physical density or viscosity',
       'They allow engineers to write papers without including numerical figures',
       'They are required by patent offices before awarding grants'],
      0,
      'Dimensionless numbers provide physical insight, scale similitude, and drastically reduce the number of independent variables needing testing.')

# MODULE 20: Hands-on Modelling & Overfitting Diagnostics in R
add_q(20, 'What is "Overfitting" in empirical modeling and machine learning?',
      ['A condition where a model fits random noise and idiosyncrasies in the training data too closely, resulting in poor predictive performance on new, unseen test data',
       'A model that has too few parameters to capture the underlying trend',
       'Running a simulation for more than 24 hours on a computer',
       'Printing a regression chart that is too large for the manuscript page margins'],
      0,
      'Overfitting occurs when excessive model flexibility causes it to memorize noise, undermining its generalization capability.')

add_q(20, 'What is "Underfitting" in statistical modeling?',
      ['A condition where the model is overly simplistic (high bias) and fails to capture the true underlying systematic trend in the data',
       'Fitting a 15th-degree polynomial to four experimental points',
       'Using floating-point numbers instead of integers',
       'Collecting too much experimental data in the laboratory'],
      0,
      'Underfitting arises when model complexity is insufficient to represent the underlying physical phenomenon.')

add_q(20, 'What is the "Bias-Variance Trade-off" in predictive modeling?',
      ['The trade-off between error from erroneous model assumptions (bias) and error from sensitivity to small fluctuations in the training set (variance)',
       'The choice between purchasing hardware from two competing vendors',
       'The trade-off between font size and page count in a doctoral thesis',
       'The balance between the salary of professors and postdoctoral scholars'],
      0,
      'Increasing model complexity decreases bias but increases variance; optimal predictive performance occurs at the balance point minimizing total expected error.')

add_q(20, 'Why is Adjusted R-squared (Adj-R^2) preferred over regular R-squared (R^2) when comparing regression models with different numbers of predictors?',
      ['Adj-R^2 penalizes the addition of unnecessary predictor variables that do not meaningfully improve model explanatory power',
       'Adj-R^2 is always equal to 1.0',
       'Adj-R^2 eliminates all residual terms from the regression equation',
       'Regular R^2 decreases whenever a new predictor is added to the model'],
      0,
      'Regular R^2 always increases or stays constant when adding variables; Adj-R^2 introduces a penalty for degrees of freedom lost.')

add_q(20, 'What is k-fold Cross-Validation in model validation?',
      ['Splitting data into k subsets, training on (k - 1) subsets, and validating on the remaining subset, repeating k times to estimate out-of-sample error',
       'Multiplying the dataset by k to increase statistical power artificially',
       'Running the regression algorithm k times on the exact same dataset without splitting',
       'Dividing the computer processor into k parallel virtual machines'],
      0,
      'k-fold cross-validation evaluates how well a model generalizes to independent unseen data by cycling training and test folds.')

add_q(20, 'In linear regression diagnostics, what does a funnel-shaped pattern in a Residuals vs. Fitted plot indicate?',
      ['Heteroscedasticity: non-constant variance of residuals across the range of predicted values',
       'Perfect normality and ideal fit of the linear regression model',
       'Zero measurement error across all experimental runs',
       'That the independent variable is strictly binary'],
      0,
      'A funnel pattern signifies heteroscedasticity, violating the classical assumption of constant residual variance (homoscedasticity).')

add_q(20, 'What diagnostic plot is used in R to check whether model residuals follow a normal distribution?',
      ['Quantile-Quantile (Q-Q) plot',
       'Box-and-whisker plot of input variables',
       'Scatterplot of independent variable vs time',
       'Pie chart of regression coefficients'],
      0,
      'A normal Q-Q plot compares empirical residual quantiles against theoretical normal distribution quantiles; points should fall along the 45-degree line.')

add_q(20, 'What is Cook’s Distance in regression diagnostics?',
      ['A metric measuring the influence of a single data point on all fitted values when that point is excluded from the model',
       'The physical distance between the laboratory bench and the office desk',
       'The time taken for a computer simulation to converge to a solution',
       'The correlation coefficient between the first two independent variables'],
      0,
      'Cook’s distance identifies influential data points that exert disproportionate leverage on the estimated regression coefficients.')

add_q(20, 'What do the Akaike Information Criterion (AIC) and Bayesian Information Criterion (BIC) measure?',
      ['Model quality that balances goodness-of-fit against model complexity (parsimony), where lower values indicate a better model',
       'The monetary cost of publishing the article in open access journals',
       'The total number of citations the authors have accumulated',
       'The percentage of variance explained multiplied by 100'],
      0,
      'AIC and BIC penalize model complexity to prevent overfitting; models with lower AIC/BIC values are preferred.')

add_q(20, 'In regularization techniques for regression, what distinguishes Lasso (L1) regression from Ridge (L2) regression?',
      ['Lasso uses an L1 penalty that can shrink coefficients exactly to zero (performing automated feature selection); Ridge uses an L2 penalty that shrinks coefficients toward zero without setting them exactly to zero',
       'Lasso is only for polynomials; Ridge is only for linear lines',
       'Ridge requires supercomputers; Lasso can be solved by hand',
       'Lasso regression always produces higher training errors than zero'],
      0,
      'Lasso (L1 norm) drives coefficients of uninformative variables to exactly zero, performing feature selection; Ridge (L2 norm) shrinks weights smoothly.')

out_path = r'd:\Interview\SAA\NPTEL\quiz_data\m11_20.json'
with open(out_path, 'w', encoding='utf-8') as f:
    json.dump(questions, f, indent=2)

print(f'Successfully generated {len(questions)} questions for Modules 11 to 20 in {out_path}')
