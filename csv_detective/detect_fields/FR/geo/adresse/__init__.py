from csv_detective.process_text import _process_text

PROPORTION = 0.6

def _is(val):
    '''Repere des adresses'''
    voies = [
        'Aire',
        'Allée',
        'Avenue',
        'Base',
        'Boulevard',
        'Cami',
        'Carrefour',
        'Chemin',
        'Cheminement',
        'Chaussée',
        'Cité',
        'Clos',
        'Coin',
        'Corniche',
        'Cote',
        'Cour',
        'Cours',
        'Domaine',
        'Descente',
        'Ecart',
        'Esplanade',
        'Faubourg',
        'Gare',
        'Grande Rue',
        'Hameau',
        'Halle',
        'Ilôt',
        'Impasse',
        'Lieu dit',
        'Lotissement',
        'Marché',
        'Montée',
        'Parc',
        'Passage',
        'Place',
        'Plan',
        'Plaine',
        'Plateau',
        'Pont',
        'Port',
        'Promenade',
        'Parvis',
        'Quartier',
        'Quai',
        'Résidence',
        'Ruelle',
        'Rocade',
        'Rond Point',
        'Route',
        'Rue',
        'Sente - Sentier',
        'Square',
        'Tour',
        'Terre-plein',
        'Traverse',
        'Villa',
        'Village',
        'Voie',
        'Zone artisanale',
        'Zone d’aménagement concerté',
        'Zone d’aménagement différé',
        'Zone industrielle',
        'Zone'
    ]

    val = _process_text(val)
    a = any([x.lower() in val for x in voies])
    return a
