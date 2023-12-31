# Roles for DBD randomizer but further drilled down by functionality
# for example, perks split up by function, aura, chase, gen slow down, etc
# Looking to use dictionaries in a list to allow the randomizer to choose random perks from the desired
# categories

# Lists will remain "survivor" and "killer" but house multiple dictionaries of perks based on their function
# categories: chase, aura, knowledge_gaining, gen_regression, gen_progression, etc

survivor = {
    "Survival": ["Windows of Opportunity", "Made for This", "Lithe", "Sprint Burst", "Dead Hard", "unbreakable", "Off the Record",  "Balanced Landing",  "Decisive Strike", "Quick & Quiet", "Blast Mine", "Iron Will", "Flash Bang", "Boil Over", "lightweight", "Deliverance", "Fixated", "Calm Spirit", "Head On", "Urban Evasion", "Spine Chill", "technician", "Flip Flop", "Plot Twist", "Tenacity", "Left Behind", "Lucky Break", "Overcome", "Desperate Measures", "Dramaturgy", "Power Struggle", "Slippery Meat", "Dance With Me", "Diversion", "Light-footed", "Smash Hit", "Small Game", "Deception", "Breakdown", "Troubleshooter", "Premonition", "Sole Survivor", "Residual Manifest", "Chemical Trap", "Resurgence", "This is Not Happening", "Parental Guidance", "No Mither", "Blood Rush", "Better Than New", "Cut Loose", "Pharmacy", "Poised"], 
    "Healing": ["Self-Care", "Botany Knowledge", "Inner Strength", "For the People", "Second Wind", "Reactive Healing", "Solidarity"], 
    "Aura": ["Deja Vu", "Bond", "Kindred", "Alert", "Empathy", "Buckle Up", "Wiretap", "Plunderer's Instinct", "Fogwise", "Dark Sense", "Detective's Hunch", "Object of Obsession", "Aftercare", "Scene Partner", "Licky Star", "Visionary", "Blood Pact", "Rookie Spirit", "Inner Focus"],
    "Teamwork": ["Resilience", "We'll Make It", "Background Player", "Saboteur", "Boon: Circle of Healing", "Borrowed Time", "Stake Out", "Any Means Necessary", "Built to Last", "Vigil", "Breakout", "Hyperfocus", "Bite the Bullet", "Reassurance", "Babysitter", "Boon: Shadow Step", "Leader", "We're Gonna Live Forever", "No One left Behind","Overzealous",  "Boon: Exponential", "Autodidact", "Streetwise", "Better Together", "open-Handed", "Ace in the Hole", "Soul Guard", "Clairvoyance", "Potential Energy", "Camaraerie",  "Mettle of Man", "Repressed A;;iance", "Counterforce", "Empathetic Connection", "Appraisal", "Scavenger", "Boon: Dark Theory", "Friendly Competition", "Quick Gambit", "Teamwork: Power of Two", "Red Herring",  "Up the Ante", "Corrective Action", "Teamwork: Collective Stealth"],
    "Endgame": ["Hope", "left Behind", "Adrenaline", "Wakeup!", "Fast Track", "Low Profile", "Self-Preservation"]
            }

killer = {
    "Chase": ["Save the Best for Last", "Bamboozle", "Shadowborn", "Brutal Strength", "Enduring", "Agitation", "Lightborn", "Rapid Brutality", "Iron Grasp", "Spirit Fury", "Franklin's Demise", "I'm All Ears", "Play With Your Food", "Coup de Grace", "Hex: Bloodfavor", "Monitor & Abuse", "Superior Anatomy", "Unrelenting", "Cruel Limits", "Starstruck", "Dissolution", "Nemesis", "Hubris", "Fire Up", "Mad Grit", "Scourge Hook: Monstrous Shrine", "Batteries Included", "Hex: Two Can Play", "Dragon's Grip", "Forced Hesitation", "Knockout", "Game Afoot", "Hex: Crowd Control", "Bloodhound", "Predator", "Overwhelming Presence"],
    "knowledge": ["Lethal Pursuer", "barbecue & Chili", "Nowhere to Hide", "Ultimate Weapon", "Discordance", "A Nurse's Calling", "Scourge Hook: Floods of Rage", "Thrilling Tremors", "Iron Maiden", "Darkness Revealed", "Bitter Murmur", "Hex: Undying", "Infectious Fright", "Spies from the Shadows", "Friends 'Til the End", "Hex: Face the Darkness", "Gearhead", "Alien Instinct", "Surveillance",  "Zanshin Tactics", "Rancor", "Make Your Choice", "Deerstalker", "Awakened Awareness", "Whispers", "Hex: Retribution", "THWACK!", "Deathbound", "Stridor", "Territorial Imperative", "Scourge Hook: Hangman's Trick", "Hoarder", "Shattered Hope"],
    "Regression": ["Scourge Hook: Pain Resonance", "Pop Goes the Weasel", "Surge", "Corrupt Intervention", "Deadlock",  "Eruption", "Overcharge", "Dead Man's Switch", "Call of Brine", "Hex: Ruin", "Merciless Storm", "Oppression", "Dying Light", "Unnerving Presence", "Grim Embrace"],
    "Stealth": ["Mindbreaker", "Hex: Plaything", "Tinker", "Trail of Torment", "Furtive Chase", "Hysteria", "Beast of Prey", "Dark Devotion", "Hex: The Third Seal", "Insidious", "Machine Learning"], 
    "Anti-Heal":["Sloppy Butcher", "Thanatophobia", "Distressing", "Scourge Hook: Gift of Pain", "Blood Echo", "Coulrophobia", "Terminus", "Forced Penance", "Leverage", "Genetic Limits", "Septic Touch"], 
    "Endgame": ["No Way Out", "Hex: No One Escapes Death", "Hex: Devour Hope", "Hex: Pentimento", "Blood Warden", "Hex: Huntress Lullaby", "Hex: Thrill of the Hunt", "hex: Haunted Ground",  "Remember Me"]
}

unrestricted_survivor = ["Windows of Opportunity", "Adrenaline", "Resilience", "Made for This", "Lithe", "Sprint Burst", "Deja Vu", "Dead Hard",
            "Bond", "Prove Thyself", "Distortion", "Unbreakable", "Kindred", "Off the Record", "Self-Care", "We'll Make It", "Hope",
            "Balanced Landing", "Botany Knowledge", "Inner Strength", "Decisive Strike", "Quick & Quiet", "Blast Mine", "Iron Will", 
            "Flashbang","Boil Over", "Background Player", "Alert", "Empathy", "Lightweight", "Deliverance", "Fixated", "Calm Spirit", 
            "Buckle Up", "Saboteur", "Head On", "Urban Evasion", "For the People", "Boon: Circle of Healing", "Spine Chill", "Borrowed Time"
            , "Technician", "Stake Out", "Flip-Flop", "Any Means Necessary", "Built to Last", "Plot Twist", "Vigil", "Breakout",
            "Hyperfocus", "Wiretap", "Second Wind", "Tenacity", "Bite the Bullet", "Reassurance", "Left Behind", "Plunderer's Instinct", 
            "Lucky Break", "Babysitter", "Fogwise", "Dark Sense", "Overcome", "Desperate Measures", "Dramaturgy", "Power Struggle", 
            "Slippery Meat", "Boon: Shadow Step", "Leader", "We're Gonna Live Forever", "No One Left Behind", "Dance With Me", "Overzealous", 
            "Diversion", "Boon: Exponential", "Light-footed", "Smash Hit", "Autodidact", "Small Game", "Better Together", "Streetwise", 
            "Wake Up!", "Deception", "Open-Handed", "Breakdown", "Troubleshooter", "Premonition", "Sole Survivor", "Residual Manifest", 
            "Chemical Trap", "Ace in the Hole", "Detective's Hunch", "Soul Guard", "Resurgence", "Reactive Healing", "Clairvoyance", 
            "This Is Not Happening", "Object of Obsession", "Potential Energy", "Camaraderie", "Aftercare", "Mettle of Man", "Parental Guidance", 
            "Fast Track", "Repressed Alliance", "Counterforce", "Empathic Connection", "No Mither", "Appraisal", "Scavenger", "Scene Partner", 
            "Lucky Star", "Boon: Dark Theory", "Friendly Competition", "Low Profile", "Solidarity", "Visionary", "Blood Rush", "Blood Pact",
            "Better Than New", "Cut Loose", "Rookie Spirit", "Quick Gambit", "Pharmacy", "Self-Preservation", "Poised", "Teamwork: Power of Two", 
            "Red Herring", "Inner Focus", "Up the Ante", "Corrective Action", "Teamwork: Collective Stealth"]

unrestricted_killer = ["Scourge Hook: Pain Resonance", "Pop Goes the Weasel", "Surge", "Corrupt Intervention", "Lethal Pursuer", "barbecue & Chili", "Save the Best for Last", 
          "Nowhere to Hide", "Sloppy Butcher", "Deadlock", "Bamboozle", "No Way Out", "Brutal Strength", "Hex: No One Escapes Death", "Shadowborn", "Ultimate Weapon", 
          "Eruption", "Discordance", "Enduring", "A Nurse's Calling", "Agitation", "Mindbreaker", "Overcharge", "Hex: Plaything", "Lightborn", "Dead Man's Switch", "Rapid Brutality", 
          "Call of Brine", "Tinker", "Hex: Devour Hope", "Hex: Ruin", "Thanatophobia", "Iron Grasp", "Spirit Fury", "Scourge Hook: Floods of Rage", "Franklin's Demise", "I'm All Ears", 
          "Thrilling Tremors", "Iron Maiden", "Play With Your Food", "Darkness Revealed", "Coup de Grace", "Bitter Murmur", "Hex: Pentimento", "Hex: Undying", "Trail of Torment", 
          "Infectious Fright", "Merciless Storm", "Blood Warden", "Spies from the Shadows", "Hex: Bloodfavor", "Distressing", "Friends 'Til the End", "Monitor & Abuse", "Scourge Hook: Gift of Pain", 
          "Superior Anatomy", "Hex: Face the Darkness", "Unrelenting", "Cruel Limits", "Blood Echo", "Starstruck", "Oppression", "Gearhead", "Hex: Huntress Lullaby", "Dissolution", "Alien Instinct", 
          "Furtive Chase", "Nemesis", "Hex: Thrill of the Hunt", "Hubris", "Surveillance", "Fire Up", "Zanshin Tactics", "Rancor", "hex: Haunted Ground", "Mad Grit", "Dying Light", "Scourge Hook: Monstrous Shrine", 
          "Unnerving Presence", "Make Your Choice", "Deerstalker", "Batteries Included", "Hex: Two Can Play", "Awakened Awareness", "Remember Me", "Coulrophobia", "Dragon's Grip", "Hysteria", "Forced Hesitation", 
          "Knockout", "Whispers", "Beast of Prey", "Terminus", "Dark Devotion", "Game Afoot", "Hex: The Third Seal", "Insidious", "Forced Penance", "Hex: Retribution", "THWACK!", "Hex: Crowd Control", "Grim Embrace", 
          "Bloodhound", "Machine Learning", "Predator", "Deathbound", "Stridor", "Leverage", "Overwhelming Presence", "Genetic Limits", "Territorial Imperative", "Scourge Hook: Hangman's Trick", "Septic Touch", "Hoarder", 
          "Shattered Hope"]