from candidate import Candidate, Experience


Joseph_Marchese = Candidate('Joseph Marchese')
Joseph_Marchese.add_education(
'''Lycoming College, Williamsport, PA: Fall 2008 - Spring 2012
   Bachelor of Arts in Music Cum Laude GPA: 3.64/4.0''',
'''Dean’s List earned by semester GPA of 3.5 or higher: Fall 2009 - Fall 2010, Spring 2012
   The William T. and Ruth S. Askey Music Prize''')

AV = Experience('Audio/Visual Specialist', 'Pennsylvania College of Technology', 'Fall 2016 - Present')
AV.add_responsibilities(
['Set up, operate, and retrieve requested audio/visual equipment (sound systems, projection systems) to and from College facilities.',
'Support the audio/visual needs of staff, faculty, students, and visitors.',
'Diagnose and make routine repairs to mechanical and electronic equipment; report and monitor the repair of major equipment failures.',
'Assist the manager in directing the activities of work-study students and part-time staff.',
'Provide on-site electronic support services during campus events.',])
Joseph_Marchese.add_experience(AV)

CIT = Experience('Coordinator of Instructional Technology', 'Lycoming College','Fall 2016')
CIT.add_responsibilities(
['Provide services and support for technology use and integration in teaching and learning.',
'Demonstrate new and emerging technology to faculty and staff and encourage best practices.',
'Document audio-visual and instructional technology best practices and create reference materials and internal user guides to assist in their implementation.',
'Coordinate with, manage, and direct student workers.',
'Inventory, loan, and set up emerging technology and audio-visual equipment for faculty, staff, and students.',
'Configure and maintain Extron control systems and projectors for classroom and administrative use.'
'Provide audio-visual setups for campus events.'])
Joseph_Marchese.add_experience(CIT)


INT = Experience('Intern', 'GSE Systems', 'Fall 2014 - Fall 2015')
INT.add_responsibilities(
['Use proprietary software to create, design, test and debug control panel simulations for active power plants.',
'Design customized icons (switches, knobs, meters, lights) for power plant control panels using graphical editing programs.',
'Design and code icons functionality using JADE fortran/VB codegen.',
'Work with customers to resolve discrepancy reports on high priority projects.',
'Lend support to a team of engineers as an administrative Intern.',
'Use Access database and Mantis DR tracking software.',
'Create programs using Python to automate routine tasks.',
'Assist in data acquisition from FTP sites and Sharepoint databases.',
'Work on entering, maintaining and tracking a database of discrepancy reports.',
'Assist in the creation of technical documents and deliverables such as:',
'Functional design specifications, which help define the scope of work on a project.',
'Model development document, a document that indexes all code created for a project for the customer.'])
Joseph_Marchese.add_experience(INT)

Joseph_Marchese.add_projects({
'GSE Systems': ['FirstEnergy Fossil Energy Plants. Design and implementation of plant control panels.',
                'Bettis Electric Plant Trainer. (Nuclear Submarine) Software customization and design.',
                'Qurrayah Combined Cycle Power Plant. Control logic debugging and troubleshooting.'],
'JetSet Gypsy Jazz': ['Guitarist'],
'Beach Bumz Band': ['Bass Guitarist', 'Vocalist'],
'Clouds Make Sounds': ['Clouds Make Sounds (2011) Album. Bassist, Mixing Support',
                       'Clouds Make Sounds: The Seasons Full Scale-Musical Production (2011)',
                       'Patchwork Vessel (2013) Album. Bassist, Lyrics, Mixing Lead, Mastering']})

Joseph_Marchese.add_other_experience(
'Guitar Instructor - Robert M. Sides - Winter 2010 - Fall 2011',
'Guitar Instructor - The Uptown Music Collective - Winter 2010 - Winter 2012',
'Guitar Instructor - Limelight Music - Fall 2014 - Fall 2015')

Joseph_Marchese.add_skills(['Python', 'Git', 'Flask', 'GUI design', 'Microsoft Access',
'Microsoft Excel', 'PowerShell', 'Diagramming Programs', 'G Suite', 'Networking',
'Cybersecurity', 'Data Analysis and Visualization', 'Windows', 'Debian Linux',
'Music Performance', 'Music Theory', 'Music Instruction', 'Adobe Photoshop CS6'])
