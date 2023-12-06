# Roles for DBD randomizer but further drilled down by functionality
# for example, perks split up by function, aura, chase, gen slow down, etc
# Looking to use dictionaries in a list to allow the randomizer to choose random perks from the desired
# categories

# Lists will remain "survivor" and "killer" but house multiple dictionaries of perks based on their function
# categories: chase, aura, knowledge_gaining, gen_regression, gen_progression, etc

survivor = {"Survival": ["Windows of Opportunity", "Made for This", "Lithe", "Sprint Burst", "Dead Hard", "unbreakable", "Off the Record",  "Balanced Landing",  "Decisive Strike", "Quick & Quiet", "Blast Mine", "Iron Will", "Flash Bang", "Boil Over", "lightweight", "Deliverance", "Fixated", "Calm Spirit", "Head On", "Urban Evasion", "Spine Chill", "technician", "Flip Flop", "Plot Twist", "Tenacity", "Left Behind", "Lucky Break", "Overcome", "Desperate Measures", "Dramaturgy", "Power Struggle", "Slippery Meat", "Dance With Me", "Diversion", "Light-footed", "Smash Hit", "Small Game", "Deception", "Breakdown", "Troubleshooter", "Premonition", "Sole Survivor", "Residual Manifest", ],
            "Healing": ["Self-Care", "Botany Knowledge", "Inner Strength", "For the People", "Second Wind", ],
            "Aura": ["Deja Vu", "Bond", "Kindred", "Alert", "Empathy", "Buckle Up", "Wiretap", "Plunderer's Instinct", "Fogwise", "Dark Sense", ],
            "Teamwork": ["Resilience", "We'll Make It", "Background Player", "Saboteur", "Boon: Circle of Healing", "Borrowed Time", "Stake Out", "Any Means Necessary", "Built to Last", "Vigil", "Breakout", "Hyperfocus", "Bite the Bullet", "Reassurance", "Babysitter", "Boon: Shadow Step", "Leader", "We're Gonna Live Forever", "No One left Behind","Overzealous",  "Boon: Exponential", "Autodidact", "Streetwise", "Better Together", "open-Handed", ],
            "Endgame": ["Hope", "left Behind", "Adrenaline", "Wakeup!", ]

            }