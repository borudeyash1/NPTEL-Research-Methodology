# -*- coding: utf-8 -*-
import json
import os

questions = []

def add_q(mod_id, q_text, options, answer, exp, q_type='single', passage=None):
    questions.append({
        'id': 400 + len(questions) + 1,
        'module': mod_id,
        'type': q_type,
        'question': q_text,
        'options': options,
        'answer': answer,
        'explanation': exp,
        'passage': passage
    })

# MODULE 41: Research in Mechanical Engineering & Thermal-Fluids (Lecture 41)
add_q(41, 'In advanced mechanical engineering research, what is the primary technical motivation for transitioning from internal combustion engines to EV powertrains and fuel cells?',
      ['Decarbonization, drastically higher energy conversion efficiency (tank-to-wheel), and elimination of criteria air pollutants (NOx, soot)',
       'EV powertrains have more moving mechanical pistons than IC engines',
       'Fuel cells do not require any electrochemical reactions',
       'EV batteries are lighter than an empty plastic fuel tank'],
      0,
      'Electric drivetrains and fuel cells deliver superior thermodynamic efficiency and zero tailpipe emissions, addressing climate and air quality mandates.')

add_q(41, 'In experimental fluid mechanics research, what does Particle Image Velocimetry (PIV) measure?',
      ['Instantaneous 2D or 3D full-field velocity vectors by tracking tracer particles illuminated by pulsed laser light sheets',
       'The electrical resistivity of copper heat pipes',
       'The molecular weight of liquid lubricants',
       'The noise level of high-speed passenger trains in decibels'],
      0,
      'PIV is an optical, non-intrusive method using double-pulsed laser sheets and CCD cameras to calculate instantaneous velocity vector fields.')

add_q(41, 'What is "Additive Manufacturing" (3D Printing) in advanced mechanical design and manufacturing research?',
      ['Layer-by-layer material deposition directly from CAD digital models, enabling complex internal cooling channels, topological optimization, and lightweighting',
       'Subtracting material from a large metal billet using computer numerical control milling machines',
       'Forging hot steel bars inside hydraulic drop hammers',
       'Casting molten iron into sand molds in a foundry'],
      0,
      'Additive manufacturing builds components additively, freeing designers from tooling constraints and enabling lattice structures.')

add_q(41, 'What is the role of Turbulence Modeling (e.g., Reynolds-Averaged Navier-Stokes - RANS vs Large Eddy Simulation - LES) in CFD research?',
      ['Resolving or modeling chaotic, multiscale turbulent eddy motions to predict aerodynamic drag, boundary layer separation, and heat transfer',
       'Calculating the financial cost of purchasing industrial air compressors',
       'Simulating the trajectory of space satellites in absolute vacuum',
       'Translating mechanical patent claims into German'],
      0,
      'Turbulence models approximate turbulent eddy dissipation across spatial/temporal scales where direct numerical simulation is computationally intractable.')

add_q(41, 'State whether True or False: In microchannel heat sinks for electronics cooling, transitioning from single-phase liquid flow to flow boiling drastically increases the heat transfer coefficient due to latent heat of vaporization.',
      ['True', 'False'],
      0,
      'True. Phase-change flow boiling exploits latent heat of vaporization, providing ultra-high heat flux dissipation at near-constant surface temperatures.')

add_q(41, 'What is "Tribology" in mechanical core engineering research?',
      ['The multidisciplinary science and technology of interacting surfaces in relative motion, encompassing friction, lubrication, and wear mechanisms',
       'The study of ancient tribal artifacts discovered during geological excavation',
       'The mathematical study of three-dimensional geometric triangles',
       'The engineering of structural trusses for railway bridges'],
      0,
      'Tribology investigates friction reduction, hydrodynamic/boundary lubrication, and surface wear degradation in mechanical systems.')

add_q(41, 'In robotics and multi-body dynamics research, what is the difference between "Forward Kinematics" and "Inverse Kinematics"?',
      ['Forward calculates end-effector position from given joint angles; Inverse calculates required joint angles to achieve a desired end-effector position',
       'Forward is for wheels; Inverse is exclusively for robotic grippers',
       'Forward is solved numerically; Inverse can only be guessed by trial and error',
       'Forward kinematics applies only to stationary robots; Inverse applies to drones'],
      0,
      'Forward kinematics computes tip coordinates from joint angles; Inverse kinematics determines joint positions required to reach a target coordinate.')

add_q(41, 'What is the "Coanda Effect" in aerodynamics and fluid flow manipulation research?',
      ['The physical tendency of a fluid jet to stay attached to a convex adjacent curved surface rather than following a straight path',
       'The sudden boiling of water when pressure is increased',
       'The reflection of acoustic waves off solid concrete walls',
       'The freezing of liquid droplets during supersonic flight'],
      0,
      'The Coanda effect causes fluid flow to adhere to adjacent curved surfaces, applied in lift generation and active boundary layer control.')

add_q(41, 'What is "Topology Optimization" in structural mechanical engineering research?',
      ['A mathematical method that optimizes material distribution within a given design domain for a specific set of loads, boundary conditions, and volume fraction constraints',
       'Surveying geographical topography using drone laser mapping',
       'Arranging machine tools on a factory floor layout',
       'Designing the user interface screens of CAD software'],
      0,
      'Topology optimization algorithmically redistributes density across finite elements to maximize stiffness-to-weight ratios.')

add_q(41, 'What is a "Digital Twin" in Industry 4.0 mechanical systems research?',
      ['A high-fidelity digital virtual simulation model that mirrors a physical machine in real-time using continuous sensor data feeds to predict maintenance and optimize operation',
       'A second identical physical spare part stored in a warehouse',
       'A photographic screenshot of an operating manual',
       'Two identical laboratory computers placed side by side'],
      0,
      'A Digital Twin couples real-time telemetry from physical assets with physics-based simulations to forecast health and performance.')

# MODULE 42: Research in Metallurgical & Materials Engineering (Lecture 42)
add_q(42, 'What are the four interconnected nodes of the classical "Materials Science and Engineering (MSE) Tetrahedron"?',
      ['Processing, Structure, Properties, and Performance',
       'Price, Popularity, Packaging, and Promotion',
       'Protons, Neutrons, Electrons, and Quarks',
       'Physics, Chemistry, Biology, and Geology'],
      0,
      'The central paradigm of materials science relates Processing -> Structure -> Properties -> Performance.')

add_q(42, 'In materials characterization research, what is the primary operational difference between SEM and TEM?',
      ['SEM raster-scans a focused electron beam across the surface to detect secondary/backscattered electrons for 3D topography; TEM transmits high-energy electrons through an ultra-thin specimen to reveal atomic/lattice crystal structure',
       'SEM uses X-rays; TEM uses sound waves',
       'SEM works only on biological cells; TEM works only on steel ingots',
       'SEM requires a specimen to be 10 meters thick; TEM requires no vacuum'],
      0,
      'SEM provides high-resolution 3D surface topography; TEM provides sub-angstrom transmission imaging of crystal lattices and defects.')

add_q(42, 'What does X-ray Diffraction (XRD) using Bragg’s Law (n * lambda = 2d * sin(theta)) determine in materials research?',
      ['Crystal structure, phase identification, lattice parameters, crystallite size, and residual stresses',
       'The exact monetary value of precious metal jewelry',
       'The speed of electrical current flow in copper wire',
       'The chemical toxicity of radioactive elements'],
      0,
      'XRD measures constructive interference of X-rays scattered by crystal planes to identify crystal symmetry and phases.')

add_q(42, 'What is a "High-Entropy Alloy" (HEA) in modern metallurgical engineering research?',
      ['An alloy composed of five or more principal metallic elements in near-equiatomic proportions, stabilized by high configurational entropy of mixing',
       'A scrap metal alloy with high chemical impurity levels',
       'An alloy that melts spontaneously at room temperature',
       'A steel bar that has been heated to 5,000 degrees Celsius'],
      0,
      'HEAs break traditional single-solvent metallurgy by blending multiple principal elements, achieving single-phase solid solutions with high strength and thermal stability.')

add_q(42, 'State whether True or False: In metals, the Hall-Petch relationship states that decreasing average grain size (grain refinement) simultaneously increases yield strength without sacrificing ductility.',
      ['True', 'False'],
      0,
      'True. Grain boundaries act as pinning barriers to dislocation glide: sigma_y = sigma_0 + k_y * d^(-1/2); grain refinement uniquely strengthens without embrittling.')

add_q(42, 'What is "Severe Plastic Deformation" (SPD), such as Equal Channel Angular Pressing (ECAP), used for in metallurgy?',
      ['Introducing massive plastic strain into bulk metals to produce ultra-fine-grained (UFG) or nanostructured materials without altering billet dimensions',
       'Melting metal scrap in an electric arc furnace',
       'Polishing the exterior surface of automobile bumpers',
       'Testing the explosive impact of artillery shells'],
      0,
      'SPD methods impart large hydrostatic shear strain to refine grain sizes down to the sub-micron/nanometer scale, yielding extraordinary mechanical strength.')

add_q(42, 'What is Energy-Dispersive X-ray Spectroscopy (EDS / EDX) coupled with an electron microscope used to measure?',
      ['Localized elemental chemical composition by detecting characteristic X-rays emitted when core-level electrons are ejected by the primary electron beam',
       'The acoustic sound frequency of ultrasonic transducers',
       'The optical transparency of thin polymer coatings',
       'The tensile fracture toughness of composite laminates'],
      0,
      'EDS measures energy spectra of characteristic X-rays emitted from the interaction volume to quantify elemental distribution.')

add_q(42, 'What is the "Glass Transition Temperature" (T_g) in polymer and amorphous materials science?',
      ['The temperature range where an amorphous material transitions from a hard, brittle, glassy state to a viscous, rubbery, flexible state upon heating',
       'The temperature where glass completely boils into vapor',
       'The freezing temperature of pure liquid water at standard pressure',
       'The ignition temperature where polymers catch fire in air'],
      0,
      'T_g is the thermal threshold where amorphous polymer chains gain segmental mobility, shifting from rigid glass to compliant rubber.')

add_q(42, 'What is the primary degradation mechanism of "Pitting Corrosion" in stainless steels exposed to marine environments?',
      ['Localized breakdown of the protective chromium oxide passive film caused by chloride ions, leading to rapid, deep autocatalytic microscopic cavity formation',
       'Uniform general surface rusting across the entire metal surface',
       'Electrochemical dissolution of copper wires by electric sparks',
       'Mechanical wear caused by high-velocity sand particles'],
      0,
      'Chloride ions penetrate passive Cr2O3 oxide layers locally, establishing localized galvanic cells that dig deep structural pits.')

add_q(42, 'In battery materials research, what defines a "Solid-State Battery" compared to conventional lithium-ion batteries?',
      ['Replacing the flammable liquid organic electrolyte and polymer separator with a solid inorganic/polymer ion-conducting solid electrolyte',
       'Making battery terminals out of solid concrete',
       'Eliminating all lithium ions from the battery chemistry',
       'Freezing liquid lithium batteries in dry ice during vehicle operation'],
      0,
      'Solid-state batteries replace combustible liquid electrolytes with solid ceramics or polymers, improving safety and energy density.')

# MODULE 43: Research in Ocean Engineering & Offshore Systems (Lecture 43)
add_q(43, 'What are the three environmental loading regimes that govern the structural design of offshore platforms in ocean engineering?',
      ['Wave, Wind, and Ocean Current hydrodynamic/aerodynamic forces',
       'Sunlight, Cloud cover, and Ambient humidity',
       'Rainfall, Lightning strikes, and Hailstones',
       'Fish migration, Seaweed growth, and Coral buildup'],
      0,
      'Offshore marine structures are engineered to resist simultaneous dynamic hydrodynamic wave forces, turbulent wind gusts, and ocean current drag.')

add_q(43, 'What is "Morison’s Equation" used for in ocean engineering hydrodynamic load calculations?',
      ['Calculating total hydrodynamic wave forces on slender cylindrical members as the sum of an inertia force (acceleration) and a drag force (velocity squared)',
       'Calculating the maximum financial insurance premium for container ships',
       'Predicting tsunami arrival times across the Indian Ocean',
       'Measuring the salinity of deep ocean trenches'],
      0,
      'Morison\'s equation calculates inline wave loads on slender offshore structural legs: F = F_inertia + F_drag.')

add_q(43, 'What is the primary operational distinction between a "Fixed Jacket Platform" and a "Tension Leg Platform" (TLP)?',
      ['Fixed Jacket is permanently pinned to the seabed by steel piles for shallow/intermediate water (< 400 m); TLP is a vertically tethered buoyant platform for ultra-deep water',
       'Fixed Jacket floats freely on surface waves; TLP is built out of stone blocks',
       'Fixed Jacket operates only on freshwater lakes; TLP operates in outer space',
       'Fixed Jacket has zero drilling capabilities; TLP is used only for tourism'],
      0,
      'Fixed steel jackets sit directly on the ocean floor; TLPs use vertical pre-tensioned tethers to suppress heave in deep ocean waters.')

add_q(43, 'In marine hydrodynamics, what does the dimensionless "Froude Number" (Fr = U / sqrt(g * L)) represent?',
      ['The ratio of inertial forces to gravitational forces, critical for wave-making resistance and ship hull model testing',
       'The ratio of fluid viscosity to heat conduction',
       'The ratio of ship cargo capacity to crew member count',
       'The ratio of water depth to atmospheric pressure'],
      0,
      'Froude number scaling governs free-surface gravity waves and hydrodynamic wave-making resistance in tow-tank ship testing.')

add_q(43, 'State whether True or False: In deepwater offshore riser engineering, "Vortex-Induced Vibration" (VIV) caused by periodic vortex shedding can trigger catastrophic fatigue failure if shedding frequency locks into the natural frequency.',
      ['True', 'False'],
      0,
      'True. Alternate vortex shedding creates periodic cross-flow lift forces; "lock-in" resonance causes rapid cyclical fatigue damage in underwater pipelines.')

add_q(43, 'What is "Ocean Thermal Energy Conversion" (OTEC) in renewable marine energy research?',
      ['Generating electricity by exploiting the temperature difference between warm surface seawater (around 25°C) and cold deep ocean water (around 5°C)',
       'Burning crude oil harvested from offshore ocean wells',
       'Extracting nuclear energy from ocean radioactive isotopes',
       'Using solar panels installed on top of marine lighthouses'],
      0,
      'OTEC runs thermodynamic Rankine cycles driven by solar-heated surface water and cold deep seawater pumped from 1,000 m depths.')

add_q(43, 'In coastal engineering, what is the role of a "Breakwater" structure?',
      ['Dissipating incident wave energy to create a sheltered, calm water basin for harbor navigation, port berthing, and coastal erosion control',
       'Pumping freshwater into the ocean during droughts',
       'Filtering microplastic particles out of seawater',
       'Providing a roadway for vehicular traffic across the ocean'],
      0,
      'Breakwaters reflect and dissipate incoming ocean swells, shielding harbor facilities and anchoring vessels from wave action.')

add_q(43, 'What does the "Significant Wave Height" (H_s or H_1/3) mean in ocean wave statistical characterization?',
      ['The average height of the highest one-third (33.3%) of all waves recorded in a given sea-state observation period',
       'The absolute highest single wave recorded during an entire century',
       'The average height of all waves divided by two',
       'The depth of the seabed below low-tide level'],
      0,
      'Significant wave height (H_1/3) approximates what an experienced maritime observer visually estimates as average wave height.')

add_q(43, 'What is "Biofouling" on marine structures, and how is it mitigated?',
      ['Accumulation of marine organisms (barnacles, algae, mussels) that increases surface roughness and hydrodynamic drag; mitigated by non-toxic fouling-release/antifouling coatings',
       'The corrosion of steel pipes by acidic rain',
       'The growth of tree roots inside offshore fuel storage tanks',
       'The accumulation of floating plastic trash around harbor docks'],
      0,
      'Biofouling increases offshore platform cross-sectional diameter and drag; fouling-release silicones or copper-free biocides mitigate accumulation.')

add_q(43, 'What is "Cathodic Protection" (using sacrificial anodes or impressed current) on offshore steel structures?',
      ['An electrochemical technique that prevents corrosion of steel by making the entire structure the cathode of an electrochemical cell (sacrificing aluminum/zinc anodes)',
       'Painting the steel with bright yellow fluorescent paint',
       'Passing high-voltage alternating current through ship hulls to kill bacteria',
       'Heating the steel legs to 100°C to evaporate seawater'],
      0,
      'Cathodic protection suppresses steel oxidation by coupling it to more reactive metals (zinc/aluminum) that corrode preferentially.')

# MODULE 44: Research in Management Studies & Operations (Lecture 44)
add_q(44, 'In operations management and supply chain research, what is the "Bullwhip Effect"?',
      ['The amplification of demand variability upstream in the supply chain from consumer to retailer, distributor, and manufacturer caused by order batching and lag',
       'A mechanical whip used to drive livestock in agricultural logistics',
       'The rapid increase in stock prices of manufacturing corporations',
       'A sudden physical breakdown of automated warehouse conveyor belts'],
      0,
      'The bullwhip effect describes how minor fluctuations in retail sales trigger wild swings in orders further up the supply chain.')

add_q(44, 'What is the "Economic Order Quantity" (EOQ) formula used to determine in inventory theory?',
      ['The optimal order quantity that minimizes total annual inventory holding costs and ordering/setup costs: EOQ = sqrt((2*D*S) / H)',
       'The maximum number of employees a corporation is legally allowed to hire',
       'The total sales revenue generated by retail stores during holidays',
       'The rate of corporate tax payable to national governments'],
      0,
      'EOQ balances fixed ordering costs against inventory holding costs to calculate the cost-minimizing batch size.')

add_q(44, 'What does the "Six Sigma" quality management methodology strive to achieve in manufacturing and service operations?',
      ['Process capability that produces no more than 3.4 defects per million opportunities (DPMO) using the DMAIC framework',
       'Reducing employee working hours to six hours per week',
       'Ensuring company executive boards have exactly six members',
       'Designing factories shaped as six-sided geometric hexagons'],
      0,
      'Six Sigma uses the DMAIC (Define, Measure, Analyze, Improve, Control) cycle to eliminate variance and achieve near-zero defects.')

add_q(44, 'In organizational behavior and human resource management research, what is "Transformational Leadership"?',
      ['A leadership style that inspires, motivates, and intellectually stimulates followers to innovate and exceed self-interests for the collective vision',
       'A manager who transfers employees to different geographic branch offices every month',
       'A leader who manages exclusively through financial fines and disciplinary punishment',
       'An automated artificial intelligence system that assigns work schedules'],
      0,
      'Transformational leaders empower teams through charisma, inspirational motivation, intellectual stimulation, and individualized consideration.')

add_q(44, 'State whether True or False: In empirical management research, "Common Method Bias" (CMB) occurs when both independent and dependent variables are gathered from the same survey respondent at the same time.',
      ['True', 'False'],
      0,
      'True. Collecting all perceptual data from single respondents at one time inflates spurious correlations due to respondent consistency bias.')

add_q(44, 'What does "Structural Equation Modeling" (SEM - e.g., PLS-SEM or CB-SEM) enable in empirical management studies?',
      ['Simultaneously testing complex networks of direct, indirect, and mediating relationships between multiple latent theoretical constructs and measured indicators',
       'Calculating the maximum tensile load a building pillar can support',
       'Automating the payroll processing software of corporate enterprises',
       'Generating random stock market ticker symbols for new startups'],
      0,
      'SEM blends factor analysis and multiple regression to estimate relationships among unobservable latent constructs (e.g., trust, loyalty).')

add_q(44, 'What is the "Resource-Based View" (RBV) of the firm in strategic management research?',
      ['A theory stating that sustainable competitive advantage stems from controlling valuable, rare, inimitable, and non-substitutable (VRIN) internal resources',
       'A theory stating that companies should purchase as much raw mining land as possible',
       'A philosophy advocating that corporations should have zero internal assets',
       'A framework focusing exclusively on government lobbying for subsidies'],
      0,
      'RBV posits that unique, bundled internal resources that satisfy VRIN criteria drive enduring corporate competitive advantage.')

add_q(44, 'In financial management research, what is the Capital Asset Pricing Model (CAPM) used to estimate?',
      ['The expected return on an asset based on its systematic market risk (Beta): E(R_i) = R_f + Beta_i * [E(R_m) - R_f]',
       'The cost of commercial building rent in major metropolitan cities',
       'The depreciation schedule of factory machinery over ten years',
       'The fee charged by banks for issuing international wire transfers'],
      0,
      'CAPM models the linear relationship between non-diversifiable systematic risk (Beta) and the expected rate of return on capital assets.')

add_q(44, 'What is "Lean Manufacturing" (derived from the Toyota Production System - TPS)?',
      ['A systematic operational philosophy focused on the relentless elimination of waste (Muda) and continuous improvement (Kaizen) to maximize customer value',
       'A corporate program forcing factory assembly line workers to lose weight',
       'Constructing factory buildings out of lightweight aluminum sheets',
       'Eliminating all quality inspection checks to speed up production lines'],
      0,
      'Lean targets seven forms of waste (overproduction, waiting, transport, overprocessing, inventory, motion, defects) to streamline value streams.')

add_q(44, 'What is a "Conjoint Analysis" in marketing research methodology?',
      ['A survey-based statistical technique used to determine how consumers value and trade off different attributes and features of a product or service',
       'A medical study examining the psychological health of marketing executives',
       'A legal procedure for merging two competing corporate conglomerates',
       'An analysis of financial bank statements conducted by tax auditors'],
      0,
      'Conjoint analysis evaluates part-worth utilities of product features by analyzing consumer choices across multi-attribute profiles.')

# MODULE 45: Research in Aerospace Engineering & Aerodynamics (Lecture 45)
add_q(45, 'In high-speed aerospace aerodynamics, what is the definition of the "Mach Number" (M)?',
      ['The ratio of the flow velocity to the local speed of sound in the fluid: M = U / a',
       'The ratio of aircraft wingspan to fuselage length',
       'The ratio of fuel weight to total aircraft takeoff weight',
       'The number of engines mounted on the aircraft wings'],
      0,
      'Mach number determines compressibility regimes: subsonic (M < 0.8), transonic (0.8 - 1.2), supersonic (1.2 - 5), and hypersonic (M > 5).')

add_q(45, 'What is an "Oblique Shock Wave" in supersonic aerodynamics?',
      ['A compressive shock wave inclined at an angle to the incoming supersonic flow direction, across which pressure, temperature, and density abruptly increase while Mach decreases',
       'A sound wave that travels along the ground during aircraft landing',
       'An acoustic vibration produced by airplane passenger cabin air conditioners',
       'A turbulence wave created when aircraft wheels touch the runway'],
      0,
      'Supersonic flow turning into itself produces oblique shock waves characterized by discontinuous jumps in pressure, temperature, and density.')

add_q(45, 'What is the "Scramjet" (Supersonic Combustion Ramjet) propulsion engine studied in aerospace research?',
      ['An airbreathing jet engine where combustion occurs in a supersonic airflow throughout the entire combustor without decelerating to subsonic speeds',
       'A rocket engine that carries liquid oxygen tanks into deep space',
       'A propeller engine powered by a small gasoline lawnmower motor',
       'An electric drone motor powered by lithium polymer batteries'],
      0,
      'Scramjets maintain supersonic flow through the combustor, enabling efficient airbreathing propulsion at hypersonic speeds (Mach 5 to 10+).')

add_q(45, 'In aircraft flight dynamics, what are the three primary rotational degrees of freedom and their respective control surfaces?',
      ['Roll (ailerons), Pitch (elevators), and Yaw (rudder)',
       'Heave, Surge, and Sway',
       'Ascent, Descent, and Hover',
       'Acceleration, Cruising, and Deceleration'],
      0,
      'Primary flight controls govern 3 axes: ailerons control roll (longitudinal axis), elevators control pitch (lateral), rudder controls yaw (vertical).')

add_q(45, 'State whether True or False: In subsonic aerodynamics, induced drag (vortex drag) is an unavoidable consequence of producing lift with a finite-span 3D wing.',
      ['True', 'False'],
      0,
      'True. Pressure differentials between lower and upper wing surfaces cause flow wrap-around at wingtips, creating wingtip vortices and downwash that induce drag.')

add_q(45, 'What is the primary function of "Winglets" installed on commercial aircraft wingtips?',
      ['To weaken wingtip vortices, reduce downwash, and decrease induced drag, thereby improving fuel efficiency',
       'To display airline advertising logos to passengers looking out windows',
       'To store emergency extra jet fuel during long transoceanic flights',
       'To act as physical hooks to grab airport arresting cables upon landing'],
      0,
      'Winglets diffuse wingtip vortex energy, reducing induced drag and saving 3% to 5% in cruise fuel consumption.')

add_q(45, 'What is "Aeroelastic Flutter" in aircraft structural research?',
      ['A dangerous dynamic instability where aerodynamic forces couple with structural vibration modes to extract energy from the airflow, causing catastrophic structural failure',
       'The gentle flapping of bird wings during thermal soaring flight',
       'The flickering of aircraft wing navigation lights at nighttime',
       'The vibration of passenger tray tables during cabin meal service'],
      0,
      'Flutter is a self-excited aeroelastic instability where aerodynamic lift feeds structural flexure-torsion vibration until structural breakup occurs.')

add_q(45, 'In orbital mechanics research, what is a "Hohmann Transfer Orbit"?',
      ['An elliptical orbital trajectory used to transfer a spacecraft between two circular coplanar orbits using two instantaneous impulsive engine burns with minimum energy',
       'A vertical trajectory where rockets fly in a straight line toward the moon',
       'A permanent stationary orbit located directly above the earth’s north pole',
       'A parabolic orbit that ejects spacecraft out of the solar system permanently'],
      0,
      'The Hohmann transfer is the two-impulse orbital maneuver that transitions a spacecraft between circular orbits with minimum delta-V consumption.')

add_q(45, 'What is the "Thermal Protection System" (TPS) on atmospheric re-entry space vehicles designed to withstand?',
      ['Extreme aerothermodynamic shock heating (> 1500°C) caused by severe compression and friction of hypersonic atmospheric shock layers',
       'The freezing sub-zero temperatures of space orbit',
       'Direct impacts from millimeter-sized micrometeorites in low earth orbit',
       'Corrosive oxidation caused by sea spray while stored in coastal hangars'],
      0,
      'Hypersonic atmospheric entry converts vehicle kinetic energy into intense aerothermodynamic shock heating, requiring ablative or ceramic tile shields.')

add_q(45, 'What is "Computational Aeroacoustics" (CAA) in aerospace engineering research?',
      ['The high-accuracy numerical simulation of aerodynamic noise generation and acoustic wave propagation (e.g., jet engine exhaust roar, landing gear aeroacoustic noise)',
       'Measuring sound insulation inside airline passenger headset earphones',
       'Playing recorded musical sounds to test aircraft pilot hearing acuity',
       'Designing public announcement speakers for airport departure terminals'],
      0,
      'CAA uses high-order low-dispersion numerical schemes to model unsteady turbulent flow structures that generate far-field acoustic radiation.')

# MODULE 46: Research in Biotechnology & Bioprocess Engineering (Lecture 46)
add_q(46, 'In bioprocess engineering, what are the four sequential phases of microbial cell growth in a batch bioreactor?',
      ['Lag phase, Exponential (Log) phase, Stationary phase, and Death phase',
       'Beginning phase, Middle phase, Advanced phase, and Final phase',
       'Hydration phase, Heating phase, Stirring phase, and Cooling phase',
       'Inoculation phase, Fermentation phase, Clarification phase, and Bottling phase'],
      0,
      'Microbial batch kinetics follow Monod growth: adaptation (lag), maximum specific growth rate (log), nutrient exhaustion (stationary), and lysis (death).')

add_q(46, 'What does the "Monod Equation" describe in bioprocess kinetics?',
      ['The relationship between specific microbial cell growth rate (mu) and the concentration of the growth-limiting nutrient substrate (S): mu = mu_max * [S / (K_s + S)]',
       'The rate of electricity consumption by bioreactor heating jackets',
       'The rate of evaporation of sterile water inside cleanrooms',
       'The mathematical relationship between DNA sequence length and RNA weight'],
      0,
      'Jacques Monod formulated this hyperbolic empirical equation relating specific growth rate to substrate availability.')

add_q(46, 'What is the primary role of "Downstream Processing" (DSP) in industrial biotechnology?',
      ['The separation, recovery, purification, and polishing of biological products (proteins, antibiotics, vaccines) from the crude fermentation broth',
       'Plowing agricultural fields downstream of a municipal river dam',
       'Cleaning the floor tiles underneath industrial fermentation tanks',
       'Shipping packaged biopharmaceutical medicines to retail pharmacy shops'],
      0,
      'Downstream processing encompasses cell lysis, centrifugation, ultrafiltration, and chromatography to isolate pure biologics from complex broths.')

add_q(46, 'What is CRISPR-Cas9 technology in genetic engineering and biotechnology research?',
      ['A targeted, RNA-guided molecular genome-editing tool that enables precise double-stranded DNA cleavage and targeted sequence modification in living cells',
       'An industrial machine that freezes agricultural potato chips',
       'A chemical reagent used to stain bacterial cells purple for optical microscopy',
       'A computer algorithm used to design three-dimensional protein websites'],
      0,
      'CRISPR-Cas9 uses a guide RNA to direct the Cas9 endonuclease to cut specific genomic loci, revolutionizing functional genomics and gene therapy.')

add_q(46, 'State whether True or False: In aerobic industrial bioreactors, maintaining adequate Dissolved Oxygen (DO) is challenging because oxygen has extremely low solubility in aqueous fermentation media.',
      ['True', 'False'],
      0,
      'True. O2 solubility in water is only ~8 mg/L at 25°C; intense sparging and agitation are mandatory to satisfy the Volumetric Mass Transfer Coefficient (k_L*a).')

add_q(46, 'What does the volumetric mass transfer coefficient (k_L*a) quantify in bioreactor design?',
      ['The gas-liquid oxygen mass transfer capability of the bioreactor system across the interface into the culture liquid',
       'The rate of liquid drainage through bottom harvest valves',
       'The electrical impedance of the motor driving the impeller',
       'The speed of light traveling through transparent glass bioreactor walls'],
      0,
      'k_L*a characterizes the oxygen transfer rate (OTR = k_L*a * (C* - C_L)), the defining bottleneck in high-density aerobic fermentations.')

add_q(46, 'What is "Polymerase Chain Reaction" (PCR) used for in molecular biotechnology?',
      ['In vitro enzymatic amplification of specific target DNA sequences through repeated cycles of denaturation, primer annealing, and polymerase extension',
       'Synthesizing synthetic plastic polymers from crude petroleum fractions',
       'Measuring the concentration of glucose in commercial soft drinks',
       'Sterilizing surgical scalpels using high-pressure steam autoclaves'],
      0,
      'Invented by Kary Mullis, PCR exponentially amplifies trace DNA molecules into billions of copies via thermal cycling with Taq polymerase.')

add_q(46, 'In protein purification chromatography, what is "Immobilized Metal Affinity Chromatography" (IMAC) used for?',
      ['Purifying recombinant proteins engineered with a polyhistidine tag (His-tag) by binding to immobilized transition metal ions (Ni2+ or Co2+)',
       'Extracting heavy gold and platinum metals from industrial wastewater',
       'Measuring the electrical conductivity of liquid buffer solutions',
       'Testing the magnetic properties of metal alloy surgical implants'],
      0,
      'His-tagged recombinant proteins coordinate with immobilized nickel or cobalt chelate matrices, eluted competitively using imidazole.')

add_q(46, 'What is "Metabolic Engineering" in industrial synthetic biology?',
      ['Optimizing and rewiring cellular genetic and regulatory networks to redirect metabolic flux toward the overproduction of specific desired chemical compounds',
       'Measuring human caloric metabolism while running on a treadmill',
       'Constructing chemical fertilizer plants near agricultural farms',
       'Designing automated pill-packaging machines for pharmaceutical factories'],
      0,
      'Metabolic engineering alters enzymatic, transport, and regulatory functions of cells using recombinant DNA to optimize biochemical pathway yields.')

add_q(46, 'What is the purpose of an "Air-Lift Bioreactor" compared to a traditional Mechanically Agitated Fermenter?',
      ['Providing gentle liquid circulation and oxygen transfer driven solely by rising gas bubbles, minimizing hydrodynamic shear damage to shear-sensitive cells (e.g., mammalian cells)',
       'Lifting heavy fermentation tanks using high-pressure compressed air cranes',
       'Operating bioreactors inside airplanes during international flights',
       'Cooling bioreactors by blowing refrigerated air onto the exterior stainless steel shell'],
      0,
      'Air-lift fermenters eliminate mechanical impellers, relying on draft-tube density differences to circulate fragile shear-sensitive mammalian or plant cells.')

# MODULE 47: Research in Chemical Sciences & Synthetic Chemistry (Lecture 47)
add_q(47, 'In organic synthesis research, what was the Nobel Prize-winning significance of "Palladium-Catalyzed Cross-Coupling Reactions" (Suzuki, Heck, Negishi)?',
      ['Enabling carbon-carbon (C-C) bond formation between functionalized organic fragments under mild conditions, transforming pharmaceutical synthesis',
       'Discovering that palladium metal can be melted into jewelry',
       'Proving that organic molecules contain hydrogen atoms',
       'Developing a method to convert lead into synthetic gold'],
      0,
      'Pd-catalyzed cross-coupling (Suzuki-Miyaura, Heck, Negishi) revolutionized medicinal chemistry by forging C-C bonds with exquisite chemo-selectivity.')

add_q(47, 'What does Nuclear Magnetic Resonance (NMR) spectroscopy exploit to determine 3D molecular structures?',
      ['The absorption and re-emission of radiofrequency electromagnetic radiation by nuclear spins (such as 1H, 13C, 31P) placed in an intense external magnetic field',
       'The bombardment of atomic nuclei with high-speed radioactive alpha particles',
       'The reflection of visible green laser beams off liquid solutions',
       'The measurement of sound waves emitted by vibrating chemical bonds'],
      0,
      'NMR probes nuclear spin transitions in a magnetic field; chemical shifts, J-coupling, and 2D NOESY elucidate atomic connectivity and 3D geometry.')

add_q(47, 'What is "Chirality" (Enantiomerism) in stereochemistry, and why is it critical in pharmaceutical drug design (e.g., the Thalidomide tragedy)?',
      ['Molecules that are non-superimposable mirror images of each other; one enantiomer may be therapeutically beneficial while the other is inactive or severely toxic',
       'Molecules that can only exist in gaseous form at room temperature',
       'Molecules that contain exactly twelve carbon atoms in a straight chain',
       'The property of chemical reagents to change color when exposed to air'],
      0,
      'Biological receptors are chiral; distinct enantiomers bind differently, requiring asymmetric synthesis and enantiomeric purity in drug discovery.')

add_q(47, 'What are the core foundational principles of "Green Chemistry" (introduced by Anastas and Warner)?',
      ['Designing chemical products and processes that reduce or eliminate the use and generation of hazardous substances, maximizing Atom Economy and minimizing E-factor',
       'Using green-colored plastic bottles for packaging laboratory chemicals',
       'Synthesizing chemicals exclusively from green leafy vegetables',
       'Painting the walls of chemical research laboratories with green paint'],
      0,
      'Green Chemistry provides 12 principles: atom economy, safer solvents, catalysis over stoichiometric reagents, waste prevention, and energy efficiency.')

add_q(47, 'State whether True or False: In chemical reaction thermodynamics, a catalyst increases the rate of reaction by shifting the chemical equilibrium constant K_eq to favor higher product yield.',
      ['True', 'False'],
      1,
      'False. Catalysts lower activation energy barrier (E_a) to accelerate rate, but NEVER alter thermodynamic equilibrium (K_eq) or Gibbs free energy (Delta G).')

add_q(47, 'What does Mass Spectrometry (MS) measure to identify chemical compounds and analyze molecular mass?',
      ['The mass-to-charge ratio (m/z) of gas-phase ions generated by ionization sources (e.g., ESI, MALDI, EI) and deflected in electric/magnetic fields',
       'The physical mass of a chemical powder weighed on a mechanical analytical balance',
       'The rate of gravitational settling of chemical crystals in a beaker',
       'The volume of helium gas displaced by an immersed solid sample'],
      0,
      'Mass spectrometers ionize analytes and separate them based on their mass-to-charge ratio (m/z) to determine exact molecular formula and fragments.')

add_q(47, 'What are Metal-Organic Frameworks (MOFs) in modern inorganic and materials chemistry research?',
      ['Crystalline, highly porous hybrid materials composed of metal ions/clusters coordinated to organic linker ligands, possessing ultra-high surface areas for gas storage/separation',
       'Steel frameworks used to construct chemical laboratory buildings',
       'Organic molecules that contain no metallic elements whatsoever',
       'Plastic picture frames used to hang university diplomas on office walls'],
      0,
      'MOFs feature record-breaking internal surface areas (up to 7,000 m^2/g) and customizable pores for hydrogen storage, CO2 capture, and catalysis.')

add_q(47, 'What is "Click Chemistry" (Barry Sharpless and Morten Meldal)?',
      ['Modular, wide-scope chemical reactions that join molecular building blocks quickly, reliably, and stereospecifically under mild conditions with high yield and no toxic by-products (e.g., CuAAC)',
       'Purchasing laboratory chemicals online using a computer mouse click',
       'An acoustic method of measuring the speed of sound inside chemical reactors',
       'Typing chemical equations rapidly on a mechanical keyboard'],
      0,
      'Click chemistry (like copper-catalyzed azide-alkyne cycloaddition) snaps molecular units together with bio-orthogonal reliability and near-quantitative yield.')

add_q(47, 'In physical chemistry, what does Cyclic Voltammetry (CV) investigate?',
      ['The electrochemical properties, redox potentials, electron transfer kinetics, and reversibility of chemical species by cycling working electrode potential linearly vs time',
       'The voltage output of automobile alternators during engine acceleration',
       'The speed of electrical lightning strikes during outdoor storms',
       'The electrical insulation resistance of laboratory power cables'],
      0,
      'CV sweeps electrode potential back and forth, recording current to analyze formal redox potentials, diffusion coefficients, and electrocatalytic mechanisms.')

add_q(47, 'What is "Computational Quantum Chemistry" (Density Functional Theory - DFT) used for in chemical research?',
      ['Solving the electronic Schrödinger equation (approximated via electron density) to predict molecular geometry, reaction transition states, bond energies, and vibrational spectra in silico',
       'Calculating the financial profits of commercial chemical manufacturing plants',
       'Designing graphics for chemical company marketing brochures',
       'Measuring the temperature of chemical reactions using optical pyrometers'],
      0,
      'DFT calculates ground-state electronic structure from electron density, predicting reaction energetics, reaction barriers, and orbital interactions computationally.')

# MODULE 48: Research in Electrical & Electronics Engineering (Lecture 48)
add_q(48, 'In semiconductor physics and VLSI design research, what does "Moore’s Law" empirically observe?',
      ['The observation that the number of transistors packed onto an integrated microchip doubles approximately every two years with shrinking cost per transistor',
       'The law stating that computer software programs get slower every year',
       'The legal requirement that electrical engineers must hold government licenses',
       'The rule that alternating current electricity always oscillates at 50 Hertz'],
      0,
      'Gordon Moore observed that photolithographic scaling doubles transistor density roughly every 18-24 months, driving semiconductor advances.')

add_q(48, 'What is the "FinFET" (3D Fin Field-Effect Transistor) architecture developed to overcome in sub-20nm silicon nodes?',
      ['Short-Channel Effects (SCE) and sub-threshold leakage current by wrapping a thin 3D silicon fin with a gate on three sides for superior electrostatic channel control',
       'The physical weight of silicon wafers during transport',
       'The acoustic noise produced by computer cooling fans',
       'The cost of purchasing copper wiring for motherboard circuits'],
      0,
      'FinFETs replace planar gates with a 3D fin channel gated on three sides, suppressing drain-induced barrier lowering and off-state leakage.')

add_q(48, 'What is a "Smart Grid" in modern electrical power systems research?',
      ['An intelligent electrical grid leveraging bidirectional power flows, advanced sensing (Phasor Measurement Units), IoT communication, and automated control to integrate renewables',
       'A standard electrical power line painted with reflective white paint',
       'A power plant that operates exclusively without human engineers',
       'An electrical grid that charges consumers double rates during summer months'],
      0,
      'Smart grids combine wide-area digital telemetry, demand response, and energy storage to manage bidirectional distributed generation and intermittent renewables.')

add_q(48, 'What is the primary role of a Phase-Locked Loop (PLL) circuit in communications and electronic systems?',
      ['A closed-loop feedback control circuit that generates an output signal whose phase and frequency are precisely locked to an incoming reference signal',
       'A mechanical lock that secures the laboratory electrical circuit breaker box',
       'A circuit that converts high-voltage alternating current into heat',
       'A software loop that formats text paragraphs in Microsoft Word'],
      0,
      'PLLs synchronize phase/frequency for clock generation, frequency synthesis, carrier recovery, and demodulation in wireless transceivers.')

add_q(48, 'State whether True or False: Wide Bandgap (WBG) semiconductors (e.g., Gallium Nitride - GaN and Silicon Carbide - SiC) allow power electronics converters to operate at higher voltages, temperatures, and switching frequencies with lower losses than traditional Silicon.',
      ['True', 'False'],
      0,
      'True. GaN and SiC have large bandgaps, high critical electric fields, and high electron mobility, revolutionizing high-efficiency power converters.')

add_q(48, 'What does the Shannon-Hartley Theorem define in digital communications and information theory?',
      ['The maximum theoretical error-free data channel capacity (C) in the presence of Gaussian noise: C = B * log2(1 + SNR)',
       'The maximum length of an underground electrical power cable in kilometers',
       'The minimum salary paid to telecommunication network engineers',
       'The volume of acoustic sound produced by wireless radio speakers'],
      0,
      'Shannon\'s channel capacity theorem sets the fundamental theoretical limit on reliable data transmission rate for a given bandwidth and SNR.')

add_q(48, 'What is "Massive MIMO" (Multiple-Input Multiple-Output) technology in 5G wireless network research?',
      ['Deploying antenna arrays with dozens or hundreds of antennas at the base station to serve multiple users simultaneously via fine-grained spatial beamforming',
       'Connecting multiple smartphones together using audio cables',
       'Broadcasting television signals using high-power analog transmitters',
       'Building massive physical cell phone towers shaped like pyramids'],
      0,
      'Massive MIMO exploits large antenna arrays at base stations to focus narrow directional RF energy beams, multiplying spectral efficiency.')

add_q(48, 'In control systems engineering research, what does the "Kalman Filter" compute?',
      ['An optimal recursive mathematical algorithm that estimates the unobservable internal states of a linear dynamic system from a series of noisy measurements over time',
       'A physical paper filter used to remove dust particles from cooling fans',
       'A circuit that filters out 50 Hz electrical hum from audio amplifiers',
       'A computer algorithm that deletes duplicate files from hard drives'],
      0,
      'The Kalman filter computes statistically optimal state estimates for dynamic systems in the presence of Gaussian process and measurement noise.')

add_q(48, 'What is a "Field-Programmable Gate Array" (FPGA) in hardware design research?',
      ['An integrated circuit designed to be configured and reprogrammed by a designer in the field after manufacturing using Hardware Description Languages (VHDL/Verilog)',
       'A microchip that can only be programmed once in a cleanroom factory and never changed',
       'An agricultural field equipped with solar-powered electric fencing',
       'A software emulator that runs exclusively inside web browsers'],
      0,
      'FPGAs contain arrays of programmable logic blocks and reconfigurable interconnects, allowing custom hardware implementation and rapid prototyping.')

add_q(48, 'In electromagnetic metamaterials research, what is a "Negative Refractive Index" material (left-handed material)?',
      ['An engineered artificial composite material where both electrical permittivity (epsilon) and magnetic permeability (mu) are simultaneously negative, bending light backward',
       'A material that cannot reflect or absorb any light rays',
       'A glass lens that is manufactured with a cracked surface',
       'A material that can only be handled with the left hand in the laboratory'],
      0,
      'Veselago proposed negative-index metamaterials (simultaneous negative permittivity and permeability) that exhibit reverse Snell\'s law, enabling super-lenses.')

# MODULE 49: Research in Mathematical Sciences & Applied Maths (Lecture 49)
add_q(49, 'In pure mathematics and topology research, what is a "Topological Space"?',
      ['A set of points equipped with a collection of open sets that satisfies axioms defining spatial properties (connectivity, compactness, continuity) invariant under continuous deformation (homeomorphism)',
       'A physical storage room on a university campus used to store math textbooks',
       'A computer monitor screen displaying 3D geometrical shapes',
       'A geometric coordinate system that only contains right angles'],
      0,
      'Topology studies qualitative geometric properties that remain unchanged when objects are continuously stretched, twisted, or crumpled without tearing.')

add_q(49, 'What is the Millennium Prize Problem concerning "P vs NP" in theoretical computer science and mathematics?',
      ['Whether every computational problem whose solution can be verified quickly (polynomial time) can also be solved quickly (polynomial time) by a deterministic algorithm',
       'Whether prime numbers are more numerous than non-prime numbers',
       'Whether parallel lines intersect at the edge of the universe',
       'Whether mathematical equations can be solved without using calculus'],
      0,
      'P vs NP investigates whether problems with efficiently verifiable solutions (NP) also possess efficiently discoverable algorithms (P).')

add_q(49, 'In applied mathematics and fluid mechanics, what are the Navier-Stokes Existence and Smoothness Millennium problems seeking to prove?',
      ['Whether smooth, physically reasonable mathematical solutions (without finite-time singularities) always exist for the 3D incompressible Navier-Stokes equations for all initial conditions',
       'Whether water freezes into ice at zero degrees Celsius in all countries',
       'Whether fluid velocity can be measured with electronic flow meters',
       'Whether ocean waves can be photographed with digital cameras'],
      0,
      'The Clay Millennium Navier-Stokes problem asks for rigorous proof that smooth solutions exist globally in time without blowing up.')

add_q(49, 'In functional analysis, what is a "Hilbert Space"?',
      ['A complete vector space equipped with an inner product, which defines a distance metric and allows concepts of vector length, angle, and orthogonality in infinite dimensions',
       'A hotel building constructed in Germany with an infinite number of rooms',
       'A two-dimensional sheet of paper used for drawing graphs',
       'A computer processor that has 64 gigabytes of memory'],
      0,
      'Hilbert spaces generalize Euclidean geometry to infinite-dimensional function spaces with an inner product, foundational to quantum mechanics and Fourier analysis.')

add_q(49, 'State whether True or False: The Riemann Hypothesis posits that all non-trivial zeros of the Riemann Zeta Function have a real part equal to 1/2.',
      ['True', 'False'],
      0,
      'True. Formulated by Bernhard Riemann in 1859, the hypothesis concerning the critical line Re(s) = 1/2 governs the distribution of prime numbers.')

add_q(49, 'What is the "Curse of Dimensionality" in applied computational mathematics and high-dimensional data analysis?',
      ['The exponential increase in volume, data sparsity, and computational complexity that occurs when adding mathematical dimensions / variables to a space',
       'A superstition that mathematicians should never write equations with more than 3 variables',
       'The failure of computer monitors to display more than three physical spatial dimensions',
       'A mathematical error that occurs when dividing numbers by negative one'],
      0,
      'Coined by Richard Bellman, the curse of dimensionality highlights how high-dimensional volume grows exponentially, making grid-based numerical methods intractable.')

add_q(49, 'What is "Compressed Sensing" (Compressive Sampling - Candès, Romberg, Tao, Donoho) in applied mathematics?',
      ['A mathematical signal processing technique that reconstructs sparse signals perfectly from far fewer measurements than required by the traditional Nyquist-Shannon sampling theorem',
       'A file compression algorithm used to zip JPEG photographs',
       'Compressing metal springs using hydraulic mechanical presses',
       'A technique for typing mathematical papers using smaller font sizes'],
      0,
      'Compressed sensing exploits signal sparsity and L1-norm minimization to reconstruct signals from sub-Nyquist non-adaptive random measurements.')

add_q(49, 'What is "Bifurcation Theory" in non-linear dynamic systems research?',
      ['The mathematical study of qualitative or topological changes in the structure of solutions (e.g., fixed points, limit cycles) as a system control parameter crosses critical thresholds',
       'The division of a road into two separate highway lanes in traffic engineering',
       'Splitting a single mathematical equation into two separate lines of text',
       'A method for drawing fractal geometric patterns using colored pencils'],
      0,
      'Bifurcations represent points where smooth parameter variations trigger abrupt structural shifts in system dynamics (e.g., pitchfork, Hopf bifurcations to chaos).')

add_q(49, 'In numerical analysis, what is the "Condition Number" of a mathematical matrix problem (kappa(A) = ||A|| * ||A^-1||)?',
      ['A measure of how sensitive the solution of a linear equation system is to small perturbations or round-off errors in the input data (ill-conditioned if kappa >> 1)',
       'The physical temperature of the computer hard drive during calculation',
       'The number of rows multiplied by the number of columns in the matrix',
       'The font size of matrix numbers printed in a math textbook'],
      0,
      'A large condition number indicates an ill-conditioned system where tiny data errors or floating-point truncation produce massive errors in the solution.')

add_q(49, 'What does the "Central Manifold Theorem" enable mathematicians to do in the stability analysis of non-linear differential equations?',
      ['Reduce the high-dimensional stability analysis of a system near a non-hyperbolic equilibrium point to an equivalent lower-dimensional invariant manifold',
       'Convert all non-linear equations into simple linear addition problems',
       'Prove that all differential equations have zero solutions',
       'Eliminate the need for calculating eigenvalues or eigenvectors'],
      0,
      'Center manifold theory isolates the critical center subspace where linear terms fail, projecting high-dimensional dynamics onto lower-dimensional manifolds.')

# MODULE 50: Research in Physical Sciences & Experimental Physics (Lecture 50)
add_q(50, 'In modern quantum condensed matter physics, what is a "Topological Insulator"?',
      ['A material that behaves as an electrical insulator in its bulk interior, but possesses robust, gapless symmetry-protected conducting metallic states on its surface/edges',
       'A rubber glove used by electricians to handle live electrical cables',
       'A plastic thermal insulator wrapped around cryogenic liquid helium tanks',
       'A material that conducts electricity only when heated above 2000°C'],
      0,
      'Topological insulators have an insulating bulk bandgap but host spin-momentum-locked metallic surface states protected by time-reversal symmetry.')

add_q(50, 'What does a SQUID (Superconducting Quantum Interference Device) sensor measure in experimental physics?',
      ['Extremely subtle, minute magnetic fields (as low as 10^-15 Tesla) based on superconducting loops containing Josephson junctions and flux quantization',
       'The physical swimming speed of giant biological marine squids',
       'The mechanical stress on submarine hulls in deep ocean water',
       'The concentration of heavy radioactive minerals inside deep mines'],
      0,
      'SQUIDs exploit Josephson quantum tunneling and magnetic flux quantization to achieve unparalleled magnetic field sensitivity (e.g., measuring brain neural magnetic signals).')

add_q(50, 'What did the Laser Interferometer Gravitational-Wave Observatory (LIGO) physically measure to detect gravitational waves in 2015?',
      ['Sub-atomic fractional differential changes in the 4-km arm lengths of laser interferometers (smaller than 1/10,000th the diameter of a proton) caused by passing ripples in spacetime',
       'Ocean tidal water level changes along the California coastline',
       'Radio signals broadcast by extra-terrestrial alien civilizations',
       'Sound waves emitted when volcanoes erupt underwater'],
      0,
      'LIGO measured minute strain fluctuations in spacetime metric (h ~ 10^-21) caused by binary black hole mergers using ultra-stable Michelson laser interferometers.')

add_q(50, 'What is the "Higgs Boson" discovered at CERN’s Large Hadron Collider (LHC) in 2012?',
      ['The excitation of the Higgs quantum scalar field that imparts mass to fundamental elementary particles (quarks and leptons) through electroweak symmetry breaking',
       'A subatomic particle that travels faster than the speed of light in vacuum',
       'A theoretical mathematical concept that has zero physical existence',
       'A new chemical element added to row 8 of the periodic table'],
      0,
      'The Higgs field permeates the universe, interacting with W/Z bosons and fermions to generate their fundamental inertial rest masses.')

add_q(50, 'State whether True or False: In quantum mechanics, the Heisenberg Uncertainty Principle (Delta_x * Delta_p >= hbar / 2) arises from experimental instrument imperfections and can be eliminated with more precise laser sensors.',
      ['True', 'False'],
      1,
      'False. The uncertainty principle is a fundamental mathematical property of non-commuting quantum operators and wave mechanics, NOT a limitation of measurement tools.')

add_q(50, 'What is "Bose-Einstein Condensation" (BEC) achieved in ultra-cold atomic physics research (Nobel Prize 2001)?',
      ['A state of matter where a dilute gas of bosons cooled to near absolute zero collapses into the lowest quantum ground state, exhibiting macroscopic quantum wave phenomena',
       'The condensation of water vapor on cold windows during winter',
       'The freezing of liquid mercury in clinical thermometers',
       'A chemical reaction between liquid helium and gaseous hydrogen'],
      0,
      'At micro-Kelvin temperatures, de Broglie wavelengths of bosonic atoms overlap, forming a macroscopic giant matter wave occupying a single quantum ground state.')

add_q(50, 'In photonics and optical physics research, what is a "Photonic Crystal"?',
      ['A periodic nanostructured optical material whose refractive index modulation creates a "photonic bandgap" that forbids the propagation of specific wavelengths of light',
       'A natural mineral gemstone polished into jewelry crystals',
       'A transparent glass window used in laboratory fume hoods',
       'A chemical liquid that changes color when exposed to electrical sparks'],
      0,
      'Photonic crystals possess periodic dielectric constants analogous to atomic lattices, blocking certain optical frequencies and enabling sub-wavelength light manipulation.')

add_q(50, 'What is "Quantum Entanglement" in fundamental physics research (Nobel Prize 2022 to Aspect, Clauser, Zeilinger)?',
      ['A quantum phenomenon where two or more particles share an intertwined quantum state such that measuring one instantaneously determines the state of the other, violating Bell’s inequalities',
       'The mechanical knotting of optical fiber cables inside laboratory storage boxes',
       'The electromagnetic interference between two adjacent Wi-Fi routers',
       'A theoretical error made by Albert Einstein in his original 1905 paper'],
      0,
      'Entanglement displays non-local correlations that violate classical local realism, confirmed experimentally by Bell inequality tests and driving quantum computing.')

add_q(50, 'What does Synchrotron Radiation (produced in electron storage rings) provide to experimental material and physical scientists?',
      ['Extremely intense, tunable, highly polarized, and collimated electromagnetic radiation across a continuous spectrum from infrared to hard X-rays for advanced crystallography and spectroscopy',
       'High-voltage alternating current electricity to power particle accelerators',
       'A source of radioactive uranium isotopes for nuclear reactors',
       'An optical green laser pointer used for lecture presentations'],
      0,
      'Synchrotrons accelerate relativistic electrons around curved magnetic trajectories to produce brilliant, tunable X-ray beams for structural determination.')

add_q(50, 'In experimental physics, what is the "Johnson-Nyquist Noise" generated inside an electrical resistor?',
      ['Thermal noise generated by the random thermal agitation of charge carriers (electrons) inside an electrical conductor at non-zero thermodynamic temperature: V_n^2 = 4*k_B*T*R*Delta_f',
       'Acoustic clicking sounds made by mechanical electrical switches',
       'Electronic hum picked up from overhead 50 Hz fluorescent light fixtures',
       'Errors caused by writing down measurement numbers in pencil'],
      0,
      'Johnson-Nyquist thermal noise is an inescapable white noise present in all resistive conductors, directly proportional to absolute temperature T.')

# MODULE 51: Personal Transformation, Philosophy of PhD & Career Trajectories (Lecture 51)
add_q(51, 'According to Lecture 51 on the Philosophy of the PhD, what is the ultimate transformational outcome of completing a doctoral degree?',
      ['Scholarly maturity: transforming from a consumer of existing knowledge into an independent, rigorous, and self-directed creator of new knowledge',
       'Acquiring a framed paper certificate to hang on an office wall',
       'Memorizing every equation in undergraduate textbooks',
       'Receiving a lifetime exemption from reading scientific papers'],
      0,
      'A PhD is fundamentally a transformation in mindset: developing autonomous inquiry, critical discernment, and the ability to pioneer knowledge.')

add_q(51, 'What is the "Imposter Syndrome" frequently experienced by graduate research scholars, and how should it be managed?',
      ['A psychological phenomenon where high-achieving scholars doubt their own abilities and fear being exposed as a fraud; managed by recognizing it is universal, seeking mentorship, and focusing on incremental progress',
       'A medical condition caused by drinking too much laboratory coffee',
       'A legal crime involving falsifying academic degree certificates',
       'A software bug in thesis formatting software'],
      0,
      'Imposter syndrome is common in research due to the constant confrontation with deep unknown frontiers; normal peer discussion and mentorship alleviate it.')

add_q(51, 'In the post-PhD career trajectory, what distinguishes a Postdoctoral Fellowship (Postdoc) from the doctoral degree experience?',
      ['Deeper independent research leadership, broadening into new methodological domains, managing grant proposals, and mentoring junior graduate students without course requirements',
       'Repeating the doctoral dissertation from scratch at the same university',
       'Taking introductory undergraduate calculus examinations',
       'Working exclusively as an administrative office receptionist'],
      0,
      'Postdoctoral training broadens intellectual versatility, builds independent research agendas, and strengthens competitiveness for faculty or senior R&D roles.')

add_q(51, 'What role does building an international "Scholarly Network" play at research conferences during a PhD?',
      ['Establishing collaborative research partnerships, discovering postdoc/faculty opportunities, exchanging fresh methodologies, and gaining constructive peer feedback',
       'Collecting free commercial promotional pens and stationery from vendor booths',
       'Avoiding attending technical keynote sessions in the conference auditorium',
       'Ensuring that researchers only speak to colleagues from their own home department'],
      0,
      'Conferences are ecosystems for professional socialization, forming inter-institutional alliances, and gaining visibility for work.')

add_q(51, 'State whether True or False: In the modern knowledge economy, the analytical and problem-solving skills honed during a PhD in engineering/science are valuable exclusively in academia and useless in industry or entrepreneurship.',
      ['True', 'False'],
      1,
      'False. Doctoral skills—deconstructing ambiguous problems, quantitative modeling, perseverance, and data synthesis—are prized in industrial R&D, tech leadership, policy, and startups.')

add_q(51, 'What is the "Dunning-Kruger Effect" in research and cognitive psychology?',
      ['A cognitive bias where novices with minimal knowledge severely overestimate their competence, while genuine domain experts tend to underestimate their relative expertise and recognize the vastness of the unknown',
       'The rate at which computer processors decrease in price over time',
       'A psychological theory explaining why researchers prefer working at night',
       'A physical law governing the evaporation of solvents in fume hoods'],
      0,
      'Dunning-Kruger illustrates that initial learning gives false confidence, whereas deep research reveals the vast complexity of knowledge, fostering true intellectual humility.')

add_q(51, 'What constitutes effective "Science Communication" (SciComm) for doctoral researchers addressing the general public or policymakers?',
      ['Translating complex technical concepts into accessible, engaging, and accurate narratives without using impenetrable jargon, highlighting societal relevance and ethics',
       'Reading verbatim mathematical proofs in monotone voices to non-technical audiences',
       'Exaggerating and sensationalizing experimental findings to gain social media followers',
       'Refusing to explain research findings to anyone without a doctoral degree'],
      0,
      'Effective public engagement bridges the ivory tower and society, explaining the why, how, and impact of scientific discovery with clarity.')

add_q(51, 'What is "Interdisciplinary Research", and why is it increasingly emphasized by global funding agencies (e.g., NSF, DST)?',
      ['Integrating perspectives, methodologies, and concepts from multiple distinct academic disciplines to solve complex real-world grand challenges (e.g., climate, health, clean energy)',
       'Conducting research without using any scientific methodology',
       'Enrolling in undergraduate classes in five different universities simultaneously',
       'Publishing identical papers in journals belonging to different departments'],
      0,
      'Grand challenges (pandemics, climate, sustainability) resist single-discipline solutions, requiring collaborative synthesis across domains.')

add_q(51, 'How should a researcher maintain "Intellectual Humility and Openness" throughout a long scientific career?',
      ['Actively seeking disconfirming evidence, welcoming rigorous peer scrutiny, and remaining willing to revise or discard cherished theories when contradicted by data',
       'Defending one’s initial theories aggressively and suppressing contradictory findings',
       'Refusing to read papers published by younger or less experienced researchers',
       'Insisting that one\'s own published papers contain zero errors'],
      0,
      'Science progresses through self-correction; intellectual humility embraces constructive critique and follows empirical evidence wherever it leads.')

add_q(51, 'What is the ultimate ethical responsibility of a scientist or engineer to society?',
      ['Pursuing truth with unyielding integrity, upholding safety and human dignity, and directing technical knowledge toward the equitable advancement and well-being of humanity',
       'Maximizing personal financial wealth through patent litigation',
       'Hiding scientific knowledge to maintain exclusive personal power',
       'Ensuring that technology is developed without considering social consequences'],
      0,
      'Scientific discovery carries profound societal impact; researchers bear a moral obligation to practice integrity and serve human welfare.')

out_path = r'd:\Interview\SAA\NPTEL\quiz_data\m41_51.json'
with open(out_path, 'w', encoding='utf-8') as f:
    json.dump(questions, f, indent=2)

print(f'Successfully generated {len(questions)} questions for Modules 41 to 51 in {out_path}')
