# -*- coding: utf-8 -*-
import json
import os

questions = []

def add_q(mod_id, q_text, options, answer, exp, q_type='single', passage=None):
    questions.append({
        'id': 300 + len(questions) + 1,
        'module': mod_id,
        'type': q_type,
        'question': q_text,
        'options': options,
        'answer': answer,
        'explanation': exp,
        'passage': passage
    })

# MODULE 31: Response Surface Methodology & Central Composite Design (Lecture 31)
add_q(31, 'What is the primary goal of Response Surface Methodology (RSM) in engineering experimentation?',
      ['To explore the relationship between several explanatory variables and one or more response variables, and optimize the response surface',
       'To draw 3D computer animation graphics for video games',
       'To compute the surface area of irregular geometric rocks manually',
       'To replace all physical laboratory experiments with random number generators'],
      0,
      'RSM uses mathematical and statistical techniques to model, optimize, and evaluate relationships between controllable factors and measured responses.')

add_q(31, 'What are the three structural components that comprise a standard Central Composite Design (CCD)?',
      ['Factorial points (2^k), Axial / Star points (2k), and Center points (n_c)',
       'Random points, Triangular points, and Hexagonal points',
       'Initial points, Intermediate points, and Concluding points',
       'Boundary points, Negative points, and Null points'],
      0,
      'A CCD builds on a 2^k factorial core by adding 2k axial points (at distance alpha) and n_c replicates at the center.')

add_q(31, 'Why are multiple replicated Center Points included in a Central Composite Design (CCD)?',
      ['To estimate experimental pure error and assess the adequacy / curvature of the second-order model',
       'To ensure the laboratory technician takes frequent rest breaks',
       'To double the electrical power consumption of the furnace',
       'To balance the physical weight of specimens on a mechanical scale'],
      0,
      'Center point replicates provide an independent estimate of experimental pure error without needing to replicate all factorial runs.')

add_q(31, 'What is the property of "Rotatability" in response surface designs?',
      ['The variance of the predicted response depends only on the distance from the design center, not on the direction',
       'The physical specimen must be continuously rotated on a lathe during testing',
       'The experimental factors can be swapped in alphabetical order without calculation',
       'The graph can be flipped upside down without changing axes'],
      0,
      'A rotatable design ensures equal prediction variance at all points equidistant from the center of the experimental region.')

add_q(31, 'For a standard k-factor Central Composite Design, what value of axial distance alpha yields a Rotatable design?',
      ['alpha = (2^k)^(1/4) (or (N_F)^(1/4))',
       'alpha = 1.0 exactly',
       'alpha = k^2',
       'alpha = 0.5 * k'],
      0,
      'Rotatability in a CCD is achieved when the axial distance alpha equals (2^k)^(1/4), which for k=2 equals 1.414, and for k=3 equals 1.682.')

add_q(31, 'What is the total number of design runs required in a standard Central Composite Design for k = 3 factors with 6 center points?',
      ['20 runs (8 factorial + 6 axial + 6 center = 20)',
       '12 runs',
       '27 runs',
       '50 runs'],
      0,
      'For k = 3: Factorial points = 2^3 = 8; Axial points = 2*3 = 6; Center points = 6. Total runs = 8 + 6 + 6 = 20.')

add_q(31, 'State whether True or False: In a second-order polynomial response surface model, quadratic terms (e.g., beta_ii * x_i^2) model curvature in the response.',
      ['True', 'False'],
      0,
      'True. First-order terms model planar slope, interaction terms model twist, and quadratic terms model peak, valley, or saddle curvature.')

add_q(31, 'In Response Surface analysis, what does a "Saddle Point" (minimax point) on the response contour map represent?',
      ['A stationary point where the response increases in one direction but decreases in another orthogonal direction (neither a true maximum nor minimum)',
       'The highest possible peak on the entire response surface',
       'A point where all experimental measurements equal zero',
       'A location where the laboratory equipment overheated'],
      0,
      'A saddle point is a stationary point where the eigenvalues of the second-derivative Hessian matrix have mixed positive and negative signs.')

add_q(31, 'What does the Box-Behnken Design (BBD) offer as an alternative to Central Composite Design (CCD)?',
      ['A spherical 3-level design that avoids extreme corner combinations (axial points outside limits), useful when corner conditions are dangerous or unfeasible',
       'A design that requires zero center runs under any circumstance',
       'A design that only works on 1 factor at a time',
       'A linear model with zero interaction terms'],
      0,
      'Box-Behnken designs do not contain points where all factors are simultaneously at their extremes, protecting sensitive equipment from overload.')

add_q(31, 'In RSM regression analysis, what does a statistically significant "Lack of Fit" test indicate?',
      ['The proposed model (e.g., quadratic) is inadequate and fails to capture systematic features of the true response surface',
       'The model fits the experimental data with complete perfection',
       'The researcher forgot to record the units of measurement',
       'The experiment was conducted in an uncalibrated room'],
      0,
      'A significant lack of fit (p < 0.05) indicates that model predictions systematically deviate from true response values beyond pure error.')

# MODULE 32: Hypothesis Testing, F-Distribution & One-Factor ANOVA (Lecture 32)
add_q(32, 'What is the primary purpose of One-Factor Analysis of Variance (ANOVA)?',
      ['To test whether there are statistically significant differences among the means of three or more independent groups',
       'To compute the correlation coefficient between two continuous variables',
       'To measure the electrical conductivity of metal alloys',
       'To convert Celsius temperatures into Fahrenheit'],
      0,
      'One-way ANOVA compares variance between treatment groups against variance within groups to test equality of group means.')

add_q(32, 'Why is conducting multiple pairwise t-tests (e.g., doing 10 separate t-tests across 5 groups) statistically flawed compared to ANOVA?',
      ['It causes family-wise error rate inflation (drastically inflating the probability of committing at least one Type I error)',
       'It takes less computer time than ANOVA',
       't-tests can only be calculated on positive numbers',
       't-tests cannot calculate sample variances'],
      0,
      'Performing multiple pairwise tests inflates the family-wise alpha: alpha_total = 1 - (1 - alpha)^m, leading to spurious false positives.')

add_q(32, 'How is the test statistic F calculated in One-Factor ANOVA?',
      ['F = MS_between / MS_within (Mean Square Between treatments divided by Mean Square Within error)',
       'F = MS_within / MS_between',
       'F = SS_total * degrees of freedom',
       'F = Mean_1 - Mean_2'],
      0,
      'The F-statistic is the ratio of treatment variance (MS_between) to random error variance (MS_within).')

add_q(32, 'Under the null hypothesis in ANOVA (all treatment population means are equal), what is the expected value of the F-statistic?',
      ['Approximately 1.0',
       '0.0',
       'Infinity',
       '-1.0'],
      0,
      'When H0 is true, MS_between and MS_within both estimate the common error variance sigma^2, so their ratio F fluctuates around 1.0.')

add_q(32, 'In One-Way ANOVA with a treatments and N total observations, what are the degrees of freedom for the treatment and error terms respectively?',
      ['Treatments: (a - 1); Error: (N - a)',
       'Treatments: a; Error: N',
       'Treatments: (N - 1); Error: (a - 1)',
       'Treatments: (a * N); Error: (a / N)'],
      0,
      'Between-group degrees of freedom is (a - 1); within-group (error) degrees of freedom is (N - a); total degrees of freedom is (N - 1).')

add_q(32, 'State whether True or False: In ANOVA, the F-distribution is strictly non-negative (F >= 0) and positively skewed.',
      ['True', 'False'],
      0,
      'True. Being a ratio of two independent chi-square variables divided by their degrees of freedom, F values cannot be negative.')

add_q(32, 'What are the three core assumptions required for standard parametric One-Factor ANOVA to be valid?',
      ['Normality of residuals, Homogeneity of variances (homoscedasticity), and Independence of observations',
       'Multicollinearity, Skewness, and Kurtosis',
       'Binary variables, Monotonicity, and Linear independence',
       'Equal sample sizes, Zero variance, and Continuous time steps'],
      0,
      'ANOVA assumes independent observations, normally distributed residuals, and equal variance across all treatment groups.')

add_q(32, 'Which statistical test is commonly used to test the assumption of homogeneity of variances across groups before ANOVA?',
      ['Levene\'s Test (or Bartlett\'s Test)',
       'Student\'s t-test',
       'Pearson correlation test',
       'Durbin-Watson autocorrelation test'],
      0,
      'Levene\'s test and Bartlett\'s test evaluate whether group variances are equal (homoscedasticity).')

add_q(32, 'If an ANOVA F-test rejects the null hypothesis (p < 0.05), what does this result prove?',
      ['At least one group mean is significantly different from the others, but it does NOT indicate which specific pairs differ',
       'All group means are completely different from one another',
       'The first group mean is guaranteed to be the highest value',
       'The experiment must be discarded and repeated'],
      0,
      'An omnibus ANOVA rejection indicates a difference exists somewhere, necessitating post-hoc tests to identify specific pair differences.')

add_q(32, 'Which post-hoc multiple comparison procedure controls family-wise error rate when comparing all pairwise combinations of means?',
      ['Tukey’s Honest Significant Difference (Tukey HSD) test',
       'Standard unadjusted Student\'s t-test',
       'Simple linear regression',
       'Binomial sign test'],
      0,
      'Tukey\'s HSD rigorously controls the family-wise Type I error rate across all pairwise mean comparisons.')

# MODULE 33: Two-Factor Experiments, Interactions & Regression Models (Lecture 33)
add_q(33, 'What is an "Interaction Effect" between two experimental factors A and B in a factorial design?',
      ['The effect of factor A on the response changes depending on the specific level of factor B',
       'The sum of factor A and factor B always equals zero',
       'Both factors are measured using the same electronic multimeter',
       'Factor A was tested on Monday and factor B was tested on Tuesday'],
      0,
      'An interaction occurs when the effect of one factor depends on the setting of another factor; non-parallel lines on an interaction plot illustrate this.')

add_q(33, 'On a two-factor interaction plot, what visual pattern indicates the ABSENCE of an interaction effect?',
      ['The response lines for the different factor levels run approximately parallel to each other',
       'The lines cross each other at a sharp right angle',
       'The lines form concentric circular loops',
       'One line is completely missing from the chart'],
      0,
      'Parallel response curves signify additive independent effects (no interaction); diverging or intersecting lines signal interaction.')

add_q(33, 'In a 2-factor factorial ANOVA with factor A (a levels), factor B (b levels), and n replicates per cell, what are the interaction degrees of freedom?',
      ['(a - 1) * (b - 1)',
       'a * b',
       '(a - 1) + (b - 1)',
       'n - 1'],
      0,
      'Degrees of freedom for the two-way interaction term AB is the product of individual factor degrees of freedom: df_AB = (a - 1)(b - 1).')

add_q(33, 'What is a "Full Factorial Design" (e.g., 2^k design)?',
      ['An experimental design that tests every possible combination of all factor levels across all factors',
       'A design that tests only one factor at a time while holding others constant',
       'A design where factors are chosen randomly from a hat',
       'A design where half of the experimental data is discarded'],
      0,
      'Full factorial designs evaluate all combinations of factor levels, allowing unconfounded estimation of all main effects and interactions.')

add_q(33, 'What is the primary drawback of the traditional "One-Factor-At-A-Time" (OFAT) experimental approach compared to Factorial Design?',
      ['OFAT cannot detect interaction effects between factors and requires far more experimental runs to achieve equivalent precision',
       'OFAT requires expensive supercomputers to calculate results',
       'OFAT is prohibited by international engineering standards',
       'OFAT can only be performed on chemical liquids'],
      0,
      'OFAT fails to reveal interactions and is statistically inefficient compared to factorial designs.')

add_q(33, 'State whether True or False: In a two-factor ANOVA, if the interaction effect (A x B) is statistically significant and strong, interpreting main effects in isolation can be misleading.',
      ['True', 'False'],
      0,
      'True. When an interaction is significant, the effect of factor A depends on B; interpreting main effects averaged across B obscures reality.')

add_q(33, 'In a 2^3 full factorial design, how many unique treatment combinations are investigated?',
      ['8 combinations', '6 combinations', '9 combinations', '16 combinations'],
      0,
      'A 2^3 design has 3 factors each tested at 2 levels: 2^3 = 8 experimental combinations.')

add_q(33, 'What is "Randomization" in experimental design, and what purpose does it serve?',
      ['Running experimental trials in a random sequence to balance out the confounding effects of extraneous nuisance variables (e.g., machine warm-up, room temperature)',
       'Guessing numerical data values without reading the sensor',
       'Allowing different researchers to grade different papers',
       'Randomly formatting table borders in the report'],
      0,
      'Randomization protects against systematic bias and unknown time-dependent trends, validating the statistical assumption of independent errors.')

add_q(33, 'What is "Blocking" in experimental design?',
      ['A technique to isolate and eliminate the variability caused by known, controllable nuisance factors (e.g., different reagent batches or different days)',
       'Physically obstructing the laboratory door to prevent interruptions',
       'Refusing to publish data that contradicts expectations',
       'Preventing other research groups from purchasing raw materials'],
      0,
      'Blocking groups homogeneous experimental units together, removing batch-to-batch variation from the experimental error.')

add_q(33, 'In multiple linear regression, what does the coefficient of determination R-squared (R^2) represent?',
      ['The proportion of total variance in the dependent variable explained by the regression model',
       'The probability that the slope coefficient is equal to zero',
       'The ratio of sample size to population size',
       'The error in sensor calibration expressed in percent'],
      0,
      'R^2 = SS_regression / SS_total: it quantifies the proportion of variation in the response accounted for by the predictors.')

# MODULE 34: Sampling Distributions, CLT, CI & t/Chi-Square Tests (Lecture 34)
add_q(34, 'What is the "Sampling Distribution" of a statistic (such as the sample mean)?',
      ['The probability distribution of the values taken by the statistic across all possible independent random samples of the same size drawn from the population',
       'The physical layout of test tubes on a laboratory shelf',
       'The histogram of a single raw dataset',
       'A chart showing the geographic location where soil samples were collected'],
      0,
      'A sampling distribution describes the theoretical distribution of a sample statistic across repeated independent samplings.')

add_q(34, 'How is the Standard Error of the Mean (SEM) related to population standard deviation sigma and sample size n?',
      ['SEM = sigma / sqrt(n)',
       'SEM = sigma * n',
       'SEM = sigma / n^2',
       'SEM = sqrt(sigma * n)'],
      0,
      'The standard error of the sample mean decreases inversely with the square root of sample size: SEM = sigma / sqrt(n).')

add_q(34, 'Under what conditions should Student\'s t-distribution be used instead of standard Normal (Z) distribution for hypothesis testing on the mean?',
      ['When the population standard deviation sigma is unknown and estimated using sample standard deviation s (especially for small samples)',
       'When the sample size n exceeds 1,000,000 observations',
       'When data values are strictly integers between 0 and 10',
       'When the data is recorded in binary code'],
      0,
      'The t-distribution accounts for the added uncertainty of estimating sigma with sample standard deviation s.')

add_q(34, 'How does the shape of the Student\'s t-distribution compare to the standard Normal (Z) distribution?',
      ['The t-distribution is symmetric and bell-shaped like the Normal, but has heavier (fatter) tails, converging to Normal as degrees of freedom approach infinity',
       'The t-distribution is a flat rectangular uniform distribution',
       'The t-distribution is strictly skewed to the left with zero area on the right',
       'The t-distribution has a sharp triangular shape with no curves'],
      0,
      'Heavier tails in the t-distribution reflect higher sampling variability; as df -> infinity, t converges to standard Normal N(0, 1).')

add_q(34, 'What is the Chi-Square (chi^2) distribution, and what is a primary application in experimental statistics?',
      ['A continuous distribution representing the sum of squared independent standard normal variables; used for testing variance and goodness-of-fit / contingency tables',
       'A distribution used exclusively for analyzing agricultural crop yields in China',
       'A discrete distribution modeling the arrival of customers at a bank teller',
       'A distribution used to measure the wavelength of laser beams'],
      0,
      'Chi-square is the distribution of the sum of squared standard normal variates, applied in variance testing and goodness-of-fit tests.')

add_q(34, 'What is the two-sample F-test used to evaluate?',
      ['Testing the equality of the variances of two independent normally distributed populations (H0: sigma_1^2 = sigma_2^2)',
       'Testing whether two population means are both equal to zero',
       'Testing whether the correlation coefficient equals 1.0',
       'Comparing the color intensity of two liquid dyes'],
      0,
      'The two-sample F-test compares the ratio of two sample variances: F = s_1^2 / s_2^2 to test H0: sigma_1^2 = sigma_2^2.')

add_q(34, 'State whether True or False: If a 95% confidence interval for the difference between two means (mu1 - mu2) contains the value 0, we fail to reject the null hypothesis of equal means at alpha = 0.05.',
      ['True', 'False'],
      0,
      'True. If zero lies inside the (1 - alpha) confidence interval, zero difference is a plausible value, corresponding to p > alpha.')

add_q(34, 'What is the degrees of freedom associated with a paired-samples t-test with n paired pairs of measurements?',
      ['n - 1', '2n - 2', 'n', '2n - 1'],
      0,
      'A paired t-test calculates differences d_i for each pair; the test is a one-sample t-test on the differences with df = n - 1.')

add_q(34, 'In statistical inference, what does the term "Robustness" mean?',
      ['The ability of a statistical test to maintain accurate Type I error rates and power even when underlying theoretical assumptions (e.g., normality) are moderately violated',
       'The physical resistance of the laboratory computer to mechanical shock',
       'The speed of algorithm convergence on supercomputers',
       'The length of time data can be stored on magnetic tapes'],
      0,
      'A test is robust if violations of its distributional assumptions do not severely distort its validity or error rates.')

add_q(34, 'When should non-parametric statistical tests (e.g., Mann-Whitney U test, Wilcoxon signed-rank test) be preferred over parametric t-tests?',
      ['When sample sizes are small and data severely violates normality assumptions or is measured on an ordinal scale',
       'When data is perfectly normally distributed with massive sample size',
       'When the researcher wants to publish in high-impact journals exclusively',
       'When calculating arithmetic means is computationally too fast'],
      0,
      'Non-parametric rank-based tests make fewer distributional assumptions, making them ideal for skewed, non-normal, or ordinal data.')

# MODULE 35: Research Methodologies in Applied Mechanics (Lecture 35)
add_q(35, 'In experimental applied mechanics, which technique is widely used for full-field, non-contact measurement of surface displacements and strain fields?',
      ['Digital Image Correlation (DIC)',
       'Charpy V-Notch impact testing',
       'Brinell ball hardness indentation',
       'Differential Scanning Calorimetry'],
      0,
      'DIC tracks stochastic speckle patterns on specimen surfaces to calculate 2D and 3D full-field displacement and strain tensors.')

add_q(35, 'What is the primary governing principle behind Finite Element Analysis (FEA) in solid mechanics?',
      ['Discretizing a continuous domain into small interconnected finite elements and solving approximate governing algebraic/differential equations using variational principles',
       'Carrying out physical tensile fracture tests on thousands of steel rods',
       'Measuring sound waves emitted when metal vibrates',
       'Using optical telescopes to inspect structural bridges from a distance'],
      0,
      'FEA subdivides complex geometries into discrete elements to solve boundary-value problems via numerical approximation.')

add_q(35, 'What is "Mesh Convergence" in computational mechanics simulations?',
      ['Demonstrating that refining the computational mesh (smaller element sizes) results in solution values that stabilize and become independent of element size',
       'The physical merging of metal fibers during composite curing',
       'Connecting multiple computers together using high-speed network cables',
       'The convergence of two cracks propagating toward each other in a plate'],
      0,
      'Mesh convergence studies verify that numerical discretization errors are sufficiently small and results are grid-independent.')

add_q(35, 'What does the Photoelasticity optical method exploit to visualize stress fields in transparent mechanical components?',
      ['Stress-induced birefringence (double refraction) under polarized light',
       'Fluorescent radiation emitted by radioactive isotopes',
       'Thermal infrared heat conduction patterns',
       'The scattering of X-rays by crystal lattices'],
      0,
      'Photoelastic materials exhibit temporary birefringence under stress, creating colored fringe patterns under polarized illumination.')

add_q(35, 'In fracture mechanics, what does the critical Stress Intensity Factor (K_IC) represent?',
      ['Plane-strain fracture toughness: the material’s intrinsic resistance to unstable brittle crack propagation',
       'The maximum compressive load a concrete pillar can withstand',
       'The electrical resistivity of a cracked semiconductor circuit',
       'The rate of chemical corrosion on an alloy surface'],
      0,
      'K_IC quantifies fracture toughness: the critical stress intensity at a crack tip that triggers rapid, unstable crack propagation.')

add_q(35, 'State whether True or False: In constitutive modeling of materials, linear elasticity (Hooke\'s law) accurately models large-strain plastic deformation and necking in metals.',
      ['True', 'False'],
      1,
      'False. Hooke\'s law applies only to small, reversible elastic strains; plasticity, work hardening, and necking require non-linear plasticity models.')

add_q(35, 'What is the role of an electrical resistance strain gauge in experimental mechanics?',
      ['Measuring localized surface strain by converting microscopic dimensional changes into proportional changes in electrical resistance',
       'Generating intense electrical sparks to cut steel plates',
       'Measuring the temperature of cryogenic cooling liquids',
       'Recording acoustic emissions during earthquakes'],
      0,
      'Bonded metallic foil strain gauges exploit the piezoresistive effect: mechanical deformation changes electrical resistance.')

add_q(35, 'What is the split-Hopkinson Pressure Bar (SHPB) apparatus used for in mechanics research?',
      ['Evaluating high-strain-rate dynamic material behavior and impact response (10^2 to 10^4 s^-1)',
       'Measuring static creep deformation over periods of five years',
       'Testing ultra-slow fatigue crack growth in vacuum chambers',
       'Polishing metallurgical specimens before optical microscopy'],
      0,
      'The SHPB measures dynamic stress-strain response of materials subjected to explosive or high-speed impact loading.')

add_q(35, 'What is the difference between "Lagrangian" and "Eulerian" descriptions in continuum mechanics?',
      ['Lagrangian tracks individual material particles as they move through space/time (common in solid mechanics); Eulerian observes flow properties at fixed points in space (common in fluid mechanics)',
       'Lagrangian is only for fluids; Eulerian is only for solids',
       'Lagrangian assumes zero friction; Eulerian assumes infinite friction',
       'Lagrangian does not use mathematics; Eulerian uses calculus'],
      0,
      'Lagrangian tracks moving reference particles; Eulerian observes field variables at fixed spatial coordinates.')

add_q(35, 'What is "Modal Analysis" in structural dynamics and vibration research?',
      ['Determining the intrinsic dynamic properties of a system: natural frequencies, damping factors, and mode shapes',
       'Analyzing the grammatical mode of sentences in a mechanics paper',
       'Classifying different modes of transportation used by researchers',
       'Measuring the brightness of fluorescent light fixtures in a laboratory'],
      0,
      'Experimental and numerical modal analysis identifies natural frequencies and mode shapes to prevent dangerous structural resonance.')

# MODULE 36: Research Methodologies in Chemical Engineering (Lecture 36)
add_q(36, 'What are the three fundamental "Transport Phenomena" that form the cornerstone of chemical engineering science?',
      ['Momentum transport (fluid dynamics), Energy transport (heat transfer), and Mass transport (diffusion/mass transfer)',
       'Rail transport, Road transport, and Air transport',
       'Electron transport, Proton transport, and Neutron transport',
       'Solidification, Liquefaction, and Evaporation'],
      0,
      'Bird, Stewart, and Lightfoot unified chemical engineering around the three transport phenomena: momentum, energy, and mass.')

add_q(36, 'What is the primary difference between a Continuous Stirred-Tank Reactor (CSTR) and a Plug Flow Reactor (PFR)?',
      ['In an ideal CSTR, contents are perfectly mixed with uniform concentration and temperature throughout; in an ideal PFR, fluid moves as orderly plugs with no axial mixing',
       'A CSTR operates only in space; a PFR operates only on land',
       'A CSTR has zero volume; a PFR has infinite volume',
       'A CSTR is strictly used for biological reactions; a PFR is used for nuclear reactions'],
      0,
      'CSTR assumes perfect spatial mixing (spatial homogeneity); PFR assumes zero axial mixing with continuous composition change along length.')

add_q(36, 'What is the Thiele Modulus in heterogeneous catalytic reaction engineering?',
      ['A dimensionless ratio comparing the intrinsic chemical reaction rate to the intraparticle diffusion rate inside porous catalyst pellets',
       'The ratio of reactor construction cost to product sales price',
       'The ratio of fluid viscosity to thermal conductivity',
       'The electrical capacitance of catalytic surface coatings'],
      0,
      'The Thiele modulus evaluates internal mass transfer resistance: high values indicate severe pore diffusion limitations.')

add_q(36, 'What is the Residence Time Distribution (RTD) measurement used for in chemical reactor diagnostics?',
      ['Characterizing non-ideal flow, channeling, stagnant dead zones, and bypassing by tracking an inert tracer pulse through the reactor',
       'Measuring how long researchers sit at their office desks during lunch',
       'Calculating the shelf-life of pharmaceutical medicines in pharmacies',
       'Evaluating the durability of stainless steel piping over twenty years'],
      0,
      'RTD analysis uses stimulus-response tracer pulses to detect flow non-idealities and quantify deviations from plug flow or perfect mixing.')

add_q(36, 'State whether True or False: In chemical process scale-up, maintaining geometric similarity (same aspect ratio) guarantees identical hydrodynamic and thermal performance at industrial scale.',
      ['True', 'False'],
      1,
      'False. Surface area to volume ratio changes drastically during scale-up (scales as 1/L), causing severe heat removal and mass transfer differences.')

add_q(36, 'What is the McCabe-Thiele graphical method used for in chemical engineering design?',
      ['Determining the theoretical number of equilibrium stages required for the distillation of a binary liquid mixture',
       'Calculating the thickness of insulation around cryogenic pipelines',
       'Predicting the turbulent velocity profile inside a centrifugal pump',
       'Designing electrical heating coils for chemical reactors'],
      0,
      'McCabe-Thiele uses equilibrium and operating lines to graphically step off theoretical equilibrium stages in binary distillation.')

add_q(36, 'What does Computational Fluid Dynamics (CFD) solve in chemical engineering multiphase flow modeling?',
      ['The Navier-Stokes equations governing fluid motion along with mass, species, and energy conservation equations via numerical discretization',
       'Standard thermodynamic steam tables using linear interpolation',
       'Chemical patent claims submitted to patent registries',
       'Stock market valuations of chemical manufacturing companies'],
      0,
      'CFD numerically resolves Navier-Stokes, turbulence closure, and transport equations to predict velocity, thermal, and concentration fields.')

add_q(36, 'What is "Process Intensification" (PI) in modern chemical engineering research?',
      ['Innovative engineering strategies that dramatically shrink equipment size, increase energy efficiency, and reduce waste (e.g., reactive distillation, microreactors)',
       'Running chemical processing plants at double speed until pipes rupture',
       'Hiring twice as many operators to monitor control panels in factories',
       'Increasing the temperature of chemical reactions to the boiling point'],
      0,
      'Process Intensification integrates unit operations into compact, ultra-efficient systems, reducing plant footprints and energy footprints.')

add_q(36, 'What is the "Pinch Analysis" methodology used for in chemical plant design?',
      ['A systematic thermodynamic technique for designing Heat Exchanger Networks (HEN) to maximize process-to-process heat recovery and minimize external utility consumption',
       'A manual technique for pinching plastic tubing to stop chemical leaks',
       'A mechanical hardness test on copper heat exchanger tubes',
       'A method for reducing the physical size of chemical engineering textbooks'],
      0,
      'Pinch analysis identifies thermodynamic energy pinch points, enabling optimal heat integration across industrial plant streams.')

add_q(36, 'In heterogeneous catalysis, what is the BET (Brunauer-Emmett-Teller) theory and measurement used to evaluate?',
      ['The specific surface area (m^2/g) and pore size distribution of solid porous catalysts via physical gas adsorption (typically N2 at 77 K)',
       'The biological toxicity of chemical reagents to laboratory animals',
       'The electrical resistivity of ceramic catalyst support substrates',
       'The rate of evaporation of solvent droplets in a spray dryer'],
      0,
      'BET analysis measures multilayer gas physisorption to determine the specific internal surface area of porous materials.')

# MODULE 37: Research Methodologies in Civil Engineering (Lecture 37)
add_q(37, 'What is the primary objective of "Geotechnical Site Characterization" in civil engineering research and practice?',
      ['Determining the subsurface soil/rock stratigraphy, groundwater conditions, shear strength, and compressibility to ensure foundation stability',
       'Designing the interior architectural furniture inside buildings',
       'Measuring traffic vehicle speeds along nearby highways',
       'Planting decorative grass and trees on construction grounds'],
      0,
      'Geotechnical investigation determines soil mechanics, bearing capacity, settlement parameters, and groundwater levels for design.')

add_q(37, 'In structural engineering research, what is "Shake Table Testing"?',
      ['A large-scale experimental platform that reproduces realistic multidimensional earthquake ground motions to evaluate the seismic performance of structural models',
       'A vibrating laboratory sieve used to sort sand into particle sizes',
       'A mechanical test to check if dining tables wobble on uneven floors',
       'An acoustic device used to disperse birds from bridge towers'],
      0,
      'Shake tables subject physical scale models or full-scale structures to real simulated seismic accelerations to analyze collapse mechanisms.')

add_q(37, 'What is the "Water-to-Cement Ratio" (w/c ratio), and what is its fundamental impact on concrete performance (Abrams’ Law)?',
      ['The ratio of water weight to cement weight; lower w/c ratio increases compressive strength and decreases porosity, provided concrete is properly consolidated',
       'Higher w/c ratio always increases concrete strength up to 100 MPa',
       'The w/c ratio only affects the color of concrete, not its strength',
       'The w/c ratio must always equal 1.0 according to international law'],
      0,
      'Abrams\' Law establishes that concrete compressive strength is inversely proportional to the water-cement ratio for a workable mix.')

add_q(37, 'In transportation engineering research, what does the "Four-Step Travel Demand Model" comprise?',
      ['Trip Generation, Trip Distribution, Mode Choice, and Traffic Assignment',
       'Vehicle Purchase, Fueling, Driving, and Parking',
       'Road Survey, Concrete Paving, Traffic Light Installation, and Toll Collection',
       'Speeding, Braking, Turning, and Crashing'],
      0,
      'The classic urban transportation planning process models trips via Generation, Distribution, Mode Choice, and Network Assignment.')

add_q(37, 'What is the purpose of "Structural Health Monitoring" (SHM) on critical civil infrastructure (e.g., long-span bridges, dams)?',
      ['Using permanently installed sensor arrays (accelerometers, strain sensors, inclinometers) to continuously monitor integrity, detect damage, and predict maintenance needs',
       'Conducting annual medical health check-ups for construction workers',
       'Cleaning dust and debris off bridge cables every weekend',
       'Painting historic bridges with decorative waterproof paint'],
      0,
      'SHM deploys smart sensors and diagnostic algorithms to detect structural degradation and damage in real-time, preventing catastrophic failures.')

add_q(37, 'State whether True or False: In soil mechanics, Terzaghi’s Effective Stress principle states that total stress sigma is the sum of effective stress sigma_prime and pore water pressure u (sigma = sigma_prime + u).',
      ['True', 'False'],
      0,
      'True. Terzaghi showed that soil deformation and shear strength are controlled exclusively by effective stress: sigma_prime = sigma - u.')

add_q(37, 'What is "Hydrologic and Hydraulic Modeling" (e.g., using EPA-SWMM or HEC-RAS) in water resources engineering?',
      ['Simulating rainfall-runoff processes, watershed hydrology, river flood routing, and urban stormwater drainage network performance',
       'Measuring the salinity of sea water using manual hydrometers',
       'Designing residential bathroom plumbing fixtures',
       'Testing the waterproof rating of construction boots'],
      0,
      'Hydrologic/hydraulic models simulate runoff generation and open-channel hydraulics to prevent urban flooding and design drainage.')

add_q(37, 'What is "Life Cycle Assessment" (LCA) in sustainable civil engineering materials research?',
      ['A cradle-to-grave environmental impact evaluation quantifying carbon footprint, embodied energy, and ecological burdens from raw material extraction through disposal',
       'Calculating the maximum financial lifespan of a bank loan for bridge construction',
       'Tracking the career lifespan of civil engineering graduates',
       'Measuring how long concrete remains wet before hardening'],
      0,
      'LCA quantifies environmental impacts across raw extraction, manufacturing, construction, operation, and end-of-life recycling/disposal.')

add_q(37, 'What is "Alkali-Silica Reaction" (ASR) in concrete degradation research (often called "concrete cancer")?',
      ['A deleterious chemical reaction between alkaline cement pore solution and reactive silica in aggregates, forming swelling gel that causes extensive cracking',
       'The rapid drying of concrete when exposed to direct summer sunlight',
       'The rusting of steel rebars caused by direct contact with acid rain',
       'A bacterial infection that digests wood framing inside concrete molds'],
      0,
      'ASR produces hygroscopic alkali-silica gel that swells upon absorbing moisture, generating expansive internal stresses and map cracking.')

add_q(37, 'What does Building Information Modeling (BIM) enable in civil engineering construction management?',
      ['An intelligent 3D model-based digital process that integrates geometric, spatial, structural, schedule (4D), and cost (5D) data throughout a project lifecycle',
       'A software package used exclusively for printing paper construction blueprints',
       'An automated robot that lays brick walls without human supervision',
       'A database tracking employee salaries in construction firms'],
      0,
      'BIM creates an integrated multidimensional digital representation of a facility, streamlining collaboration, clash detection, and project management.')

# MODULE 38: Research Methodologies in Computer Science & Engineering (Lecture 38)
add_q(38, 'In theoretical computer science and algorithm design, what does "Asymptotic Complexity" (Big-O notation) quantify?',
      ['The upper bound on the growth rate of runtime or memory requirements as the input size n approaches infinity, independent of hardware specifics',
       'The exact number of clock cycles a program takes on an Intel Core i7 processor',
       'The monetary retail cost of purchasing a commercial software license',
       'The physical surface temperature of the CPU chip during execution'],
      0,
      'Big-O notation characterizes algorithmic scalability and time/space complexity as input size grows toward infinity.')

add_q(38, 'What is the primary scientific requirement for empirical benchmarking in computer systems and architecture research?',
      ['Rigorous experimental methodology: using standard recognized benchmarks (e.g., SPEC CPU), multiple trials, statistical confidence intervals, and reporting exact hardware/compiler environments',
       'Testing the code once on the student’s personal laptop without reporting specs',
       'Measuring execution time with a mechanical handheld stopwatch',
       'Comparing algorithms using completely different random input datasets'],
      0,
      'Computer systems research demands reproducible benchmarks, detailed architectural specifications, controlled baselines, and statistical confidence.')

add_q(38, 'In empirical machine learning and computer vision research, why is the separation of datasets into Training, Validation, and Test sets mandatory?',
      ['To tune hyperparameters on validation data while preserving the test set as an untouched benchmark to evaluate true out-of-distribution generalization without data leakage',
       'To ensure that datasets can fit onto three separate thumb drives',
       'To allow three different student authors to work on separate files',
       'Because machine learning algorithms cannot read files larger than 100 megabytes'],
      0,
      'Strict isolation of the test set prevents data leakage and confirmation bias, ensuring genuine evaluation of generalization performance.')

add_q(38, 'What is "Data Leakage" in machine learning research?',
      ['When information from outside the training dataset (such as target labels or test-set statistics) inadvertently contaminates the model during training or preprocessing',
       'A physical tear in a magnetic tape data storage reel',
       'Unauthorized access to a database by an external computer hacker',
       'Deleting important lines of Python code by mistake'],
      0,
      'Data leakage artificially inflates training and validation metrics, causing severe model failure when deployed on real unseen data.')

add_q(38, 'What is the purpose of "Ablation Studies" in experimental AI and software engineering papers?',
      ['Systematically removing individual components, layers, or features one by one to determine their specific, isolated contribution to overall system performance',
       'Burning damaged server hard drives to permanently erase corrupted data',
       'Deleting all comments from computer source code before submitting to conferences',
       'Rewriting an entire software repository in assembly language'],
      0,
      'Ablation experiments isolate and prove which specific architectural design choices actually drive empirical performance gains.')

add_q(38, 'State whether True or False: In cryptographic protocol design, security through obscurity (keeping the encryption algorithm secret) is a recognized best practice.',
      ['True', 'False'],
      1,
      'False. Kerckhoffs’s Principle mandates that a cryptographic system must remain secure even if everything about the system, except the key, is public knowledge.')

add_q(38, 'What is the CAP Theorem in distributed computing systems research (proven by Eric Brewer)?',
      ['A distributed data store can simultaneously provide at most two of the following three guarantees: Consistency, Availability, and Partition Tolerance',
       'Computer algorithms require Calculus, Algebra, and Probability',
       'Central processing units can only execute addition, subtraction, and multiplication',
       'Cloud servers must be located in California, Amsterdam, and Paris'],
      0,
      'The CAP theorem proves that network partitions force distributed architectures to trade off either strong consistency or high availability.')

add_q(38, 'What constitutes a "Formal Verification" approach in computer systems and software engineering research?',
      ['Using mathematical proofs (e.g., model checking, theorem proving) to rigorously prove that a software or hardware system satisfies formal specifications under all conditions',
       'Asking an experienced software engineer to visually inspect the code',
       'Running an automated spell-checker on the user manual',
       'Recompiling code three times to check if errors disappear'],
      0,
      'Formal methods provide mathematical guarantees of correctness, essential for safety-critical aerospace, automotive, and cryptographic systems.')

add_q(38, 'What is the "Replication Crisis" in computational science, and how do "Artifact Evaluation" committees address it?',
      ['The inability of independent researchers to reproduce published experimental results; addressed by peer-reviewing executable code, docker containers, and datasets alongside manuscripts',
       'A global shortage of silicon microchips used to build supercomputers',
       'The failure of computer monitors to display high-resolution colors accurately',
       'A copyright conflict between software companies and academic universities'],
      0,
      'Artifact Evaluation verifies that code repositories, environments (e.g., Docker), and datasets execute reproducibly as claimed.')

add_q(38, 'In natural language processing and deep learning research, what is the core architectural innovation of the "Transformer" model (Vaswani et al., 2017)?',
      ['The Self-Attention Mechanism that computes dynamic dependencies between all tokens in a sequence in parallel, replacing sequential recurrent neural networks (RNNs)',
       'Replacing digital floating-point arithmetic with analog mechanical gears',
       'Running machine learning models on high-voltage electrical transformers',
       'Eliminating the need for training data by using philosophical logic'],
      0,
      'Self-attention enables parallel processing of long-range token relationships across sequences, transforming AI and NLP.')

# MODULE 39: Research Methodologies in Engineering Design (Lecture 39)
add_q(39, 'What makes the Department of Engineering Design at IIT Madras unique compared to traditional core engineering departments?',
      ['It focuses specifically on the comprehensive engineering design process, functional synthesis, and multidisciplinary product development rather than a single physical domain',
       'It teaches only painting, sculpture, and graphic arts',
       'It forbids the use of computers and mathematics in all research projects',
       'It offers degrees exclusively through correspondence without lab work'],
      0,
      'IITM Engineering Design focuses on design thinking, synthesis, multidisciplinary systems, robotics, and user-centric product engineering.')

add_q(39, 'What is the difference between "Analysis" and "Synthesis" in engineering design methodology?',
      ['Analysis breaks an existing system into components to understand behavior; Synthesis integrates diverse principles, components, and concepts to create a new functional system',
       'Analysis is done by engineers; Synthesis is done exclusively by lawyers',
       'Analysis uses computers; Synthesis is done using manual drawing pencils',
       'Analysis is for software; Synthesis is only for building wooden furniture'],
      0,
      'Analysis dissects existing entities to predict performance; Synthesis assembles novel combinations to fulfill desired functions.')

add_q(39, 'In product design, what does the "Pahl and Beitz" systematic design methodology prescribe as the sequential design phases?',
      ['Planning & Task Clarification -> Conceptual Design -> Embodiment Design -> Detail Design',
       'Brainstorming -> Manufacturing -> Marketing -> Sales',
       'Trial-and-error -> Patenting -> Prototyping -> Redesign',
       'Cost Estimation -> Factory Construction -> Product Ideation -> Testing'],
      0,
      'Pahl & Beitz established the classic German design framework moving systematically from task clarification to detail documentation.')

add_q(39, 'What is the purpose of the "Quality Function Deployment" (QFD) House of Quality in engineering design research?',
      ['Systematically translating customer needs ("Voice of the Customer") into measurable engineering design specifications and technical characteristics',
       'Designing residential housing layouts for factory floor workers',
       'Evaluating the financial creditworthiness of component suppliers',
       'Checking building compliance with municipal earthquake building codes'],
      0,
      'The House of Quality matrix maps customer requirements against engineering attributes to prioritize technical design targets.')

add_q(39, 'What is "Design for Manufacturing and Assembly" (DFMA)?',
      ['A concurrent engineering design philosophy aimed at simplifying product geometry, reducing part counts, and standardizing components to minimize manufacturing cost and assembly difficulty',
       'A government regulation mandating that all parts be manufactured in state-owned factories',
       'Designing products that can only be assembled by robotic arms in cleanrooms',
       'A software package used to calculate corporate corporate tax returns'],
      0,
      'DFMA streamlines parts, minimizes fasteners, eliminates assembly confusion, and lowers production and maintenance costs.')

add_q(39, 'State whether True or False: In human-centered design, "Affordance" refers to the perceived and actual properties of an object that visually signal to users how it should be operated (e.g., a handle affords pulling).',
      ['True', 'False'],
      0,
      'True. Don Norman popularized affordances in design: intuitive physical/visual cues that indicate how an interface or product functions.')

add_q(39, 'What is the "Pugh Concept Selection Matrix" used for in engineering design?',
      ['Evaluating multiple alternative design concepts against a set of weighted criteria relative to a chosen baseline / reference design (using +, -, or S scores)',
       'Calculating the maximum tensile stress on a suspension bridge cable',
       'Tracking the daily attendance of design team engineers',
       'Selecting which journal to submit a manuscript to based on impact factor'],
      0,
      'Stuart Pugh\'s concept matrix compares competing conceptual variants against a datum to objectively converge on the superior design.')

add_q(39, 'What is the role of "Ergonomics / Human Factors Engineering" in modern product design?',
      ['Optimizing the interaction between humans and system components to maximize safety, human comfort, usability, and task efficiency while minimizing physical strain',
       'Designing products to be as heavy as possible to prevent theft',
       'Ensuring products are packaged exclusively in recycled cardboard boxes',
       'Calculating the economic inflation rate of consumer household appliances'],
      0,
      'Ergonomics adapts technical devices to human biomechanics, cognitive limitations, and physiological capabilities.')

add_q(39, 'What is "Generative Design" in advanced engineering design systems?',
      ['An iterative design process using AI and evolutionary algorithms to automatically generate high-performance, organic geometric shapes that fulfill specified load, manufacturing, and spatial constraints',
       'A technique where junior interns sketch hand drawings for senior engineers',
       'Generating electricity from wind turbines connected to design computers',
       'Printing identical plastic parts using standard injection molding'],
      0,
      'Generative design explores thousands of topology-optimized configurations meeting specified structural loads and manufacturing constraints.')

add_q(39, 'What constitutes a "Design Failure Modes and Effects Analysis" (DFMEA) as opposed to a Process FMEA (PFMEA)?',
      ['DFMEA focuses on potential product malfunctions and design deficiencies originating from geometry, materials, and tolerances; PFMEA focuses on manufacturing and assembly process flaws',
       'DFMEA is done in universities; PFMEA is done in government patent offices',
       'DFMEA is for software; PFMEA is exclusively for civil bridges',
       'DFMEA requires no written documentation'],
      0,
      'DFMEA addresses vulnerabilities inherent in the design itself; PFMEA addresses risks arising from factory fabrication and assembly operations.')

# MODULE 40: Research Methodologies in Humanities & Social Sciences (Lecture 40)
add_q(40, 'What is the fundamental distinction between Quantitative Research and Qualitative Research in social science methodology?',
      ['Quantitative research analyzes numerical data using statistical modeling to test hypotheses; Qualitative research explores non-numerical phenomena (meanings, experiences, narratives) to generate understanding',
       'Quantitative research is used exclusively in engineering; Qualitative research is used exclusively in primary schools',
       'Quantitative research requires no data collection; Qualitative research requires supercomputers',
       'Quantitative research is always biased; Qualitative research is universally infallible'],
      0,
      'Quantitative methods measure, quantify, and model statistically; Qualitative methods interpret human meaning, social dynamics, and lived experiences.')

add_q(40, 'What is "Triangulation" in social science and mixed-methods research methodology?',
      ['Using multiple independent data sources, methods, investigators, or theoretical frameworks to cross-validate findings and mitigate single-method bias',
       'Surveying triangular parcels of agricultural land with a theodolite',
       'Requiring all research papers to be written by exactly three co-authors',
       'Dividing student survey respondents into three equal financial categories'],
      0,
      'Triangulation enhances research validity by cross-verifying findings through diverse data streams, observers, or methodological angles.')

add_q(40, 'In qualitative social science methodology, what is "Grounded Theory" (developed by Glaser and Strauss)?',
      ['A systematic inductive methodology where theoretical models are derived and constructed directly from the iterative collection and coding of empirical field data',
       'A theory explaining the electrical grounding of laboratory instruments',
       'A requirement that all research interviews be conducted sitting on the ground',
       'A theory that has been thoroughly disproven and buried in archives'],
      0,
      'Grounded theory builds theory from the ground up through constant comparative analysis of observational and interview data.')

add_q(40, 'What is an "Ethnographic" research study?',
      ['An in-depth, immersive qualitative study of the culture, practices, social interactions, and behaviors of a community or group in their natural environment over an extended period',
       'A statistical census of national voter registration records',
       'An archaeological excavation of ancient prehistoric stone tools',
       'A laboratory experiment measuring human heart rate under stress'],
      0,
      'Ethnography uses participant observation and immersive fieldwork to understand social practices from an insider\'s perspective.')

add_q(40, 'What is the "Likert Scale" commonly used in survey questionnaires in humanities and social sciences?',
      ['A psychometric rating scale where respondents indicate their level of agreement or disagreement with statements (e.g., Strongly Disagree to Strongly Agree)',
       'A geological scale measuring earthquake tremor intensity',
       'An optical scale measuring the transparency of polluted river water',
       'A scale used by university registrars to grade graduate student theses'],
      0,
      'Likert scales measure attitudes, opinions, and perceptions using structured, balanced response categories.')

add_q(40, 'State whether True or False: In social science surveys, "Convenience Sampling" (e.g., surveying friends and classmates) produces a sample that is statistically representative of the entire national population.',
      ['True', 'False'],
      1,
      'False. Convenience sampling is a non-probability method prone to severe selection bias and cannot be generalized to the broader population.')

add_q(40, 'What is the difference between "Structured", "Semi-Structured", and "Unstructured" interviews in social research?',
      ['Structured follows a rigid predetermined questionnaire; Semi-structured uses an open framework with conversational flexibility; Unstructured is an open-ended narrative exploration',
       'Structured interviews are conducted online; Semi-structured are conducted outdoors; Unstructured are illegal',
       'Structured is for children; Semi-structured is for adults; Unstructured is for professors',
       'Structured interviews have no questions; Unstructured interviews last 24 hours'],
      0,
      'Interview formats balance standardization (structured) with qualitative depth and exploratory flexibility (semi-structured/unstructured).')

add_q(40, 'What is "Thematic Analysis" in qualitative data processing?',
      ['A systematic qualitative method for identifying, analyzing, organizing, describing, and reporting repeated patterns of meaning (themes) within a dataset',
       'Arranging the furniture of an interview room according to an artistic theme',
       'Classifying research papers according to the font color of their headings',
       'Calculating the mathematical mean of qualitative audio recordings'],
      0,
      'Thematic analysis codes text/transcripts to synthesize underlying thematic patterns across qualitative datasets.')

add_q(40, 'In social science research ethics, why is "Anonymity and Confidentiality" of human participants paramount?',
      ['To safeguard participants from potential social, professional, legal, or psychological harm and ensure genuine, uninhibited responses',
       'To prevent participants from winning academic research awards',
       'Because government agencies do not permit human names in print',
       'To reduce the file size of survey database spreadsheets'],
      0,
      'Protecting participant privacy prevents personal repercussions, preserves trust, and upholds ethical research standards.')

add_q(40, 'What is "Reflexivity" in qualitative research methodology?',
      ['An explicit self-reflection where the researcher critically examines how their own personal background, biases, values, and presence influence data collection and interpretation',
       'The biological involuntary nerve reflex of human muscle tissue',
       'The reflection of light off the researcher’s computer eyeglasses',
       'The speed at which a researcher answers telephone calls from editors'],
      0,
      'Reflexivity acknowledges that the researcher is part of the social world being studied and makes researcher subjectivity transparent.')

out_path = r'd:\Interview\SAA\NPTEL\quiz_data\m31_40.json'
with open(out_path, 'w', encoding='utf-8') as f:
    json.dump(questions, f, indent=2)

print(f'Successfully generated {len(questions)} questions for Modules 31 to 40 in {out_path}')
