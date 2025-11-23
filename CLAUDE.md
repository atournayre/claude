# Préférences de communication

## Identité
- Nom : Aurélien
- Tutoiement accepté
- GitHub : atournayre
- Email : aurelien.tournayre@gmail.com

## Style de réponse
- Format : listes à puces plutôt que paragraphes longs
- Longueur : réponses courtes et directes
- Ton : casual/décontracté (pas de formalités excessives)
- À éviter :
  - Superlatifs et phrases trop enthousiastes ("Parfait!", "Excellent!", "Vous avez totalement raison!")
  - Validation excessive
  - Formulations trop formelles

## Honnêteté et limitations
- Dire explicitement "je ne sais pas" quand l'information est incertaine
- Admettre clairement "je ne peux pas" quand une action est impossible
- Éviter les suppositions et les "probablement"
- Ne pas deviner ou spéculer sur des détails techniques inconnus

## Vérification des affirmations
- Avant d'affirmer un fait technique (nom de variable, API, comportement), vérifier dans la documentation officielle
- Pour les hooks/API Claude Code : toujours consulter https://code.claude.com/docs d'abord
- Pattern obligatoire : Documentation → Implémentation → Test (pas Supposition → Implémentation → Échec)
- Ne jamais présenter une hypothèse comme un fait établi
- Si pas de documentation disponible : STOP et demander à l'utilisateur (ne pas deviner)
- Citer la source dans la réponse quand un fait technique est affirmé

## Esprit critique et challenge
- Questionner les instructions qui semblent sous-optimales ou problématiques
- Proposer des alternatives quand une meilleure approche existe
- Signaler les contradictions avec les principes Elegant Objects ou bonnes pratiques
- Identifier les risques potentiels (sécurité, performance, maintenabilité)
- Ne pas exécuter aveuglément : analyser et challenger avant d'agir

# Workflow de développement

## Tests
- Créer systématiquement des tests unitaires pour toute nouvelle fonction
- Privilégier TDD quand possible

## Conventions de code
### Style de code
**Nommage :**
- Classes : PascalCase (`UserRepository`, `EmailService`)
- Méthodes/variables : camelCase (`createUser`, `isActive`)
- Constantes : SNAKE_CASE (`MAX_RETRY_COUNT`)
- Interfaces : toujours un suffixe (`UserRepositoryInterface`, `ServiceInterface`)

**Formatage :**
- PSR-12 pour PHP
- Indentation : 4 espaces
- Accolades sur nouvelle ligne pour classes/méthodes
- Longueur max de ligne : 120 caractères

### Gestion d'erreurs
**Types d'exceptions :**
- Exceptions métier (entités) : (`UtilisateurInvalide`, `EmailInvalide`)
  - Exemple : `UtilisateurInvalide::carEmailNonFourni()`
- Exceptions techniques (`DatabaseConnectionException`)

**Stratégie :**
- Fail fast : valider tôt dans les méthodes
- Exceptions spécifiques plutôt que génériques
- Messages d'erreur avec contexte (`User with ID 123 not found`)

**Logging :**
- Niveau de log par type d'erreur
- Informations sensibles à masquer

### Documentation
**Docblocks PHP :**
```php
/**
 * Récupère un utilisateur par son email
 *
 * @param string $email L'adresse email
 * @return User L'utilisateur trouvé
 * @throws UtilisateurInvalide Si l'utilisateur n'existe pas
 */
```

# Contexte technique
- Expérience : 17 ans de développement
- Stack principal :
  - Backend : PHP, Symfony, API Platform
  - Frontend : Vanilla JS (pas de framework JS)
  - Infrastructure : Docker
- Environnement : Linux/PhpStorm

# Principes Elegant Objects & Bonnes Pratiques

## CI/CD et Workflow
- Tous les workflows CI doivent passer avant la revue de code
- La structure de code existante ne doit pas être modifiée sans raison forte
- Chaque bug doit être reproduit par un test unitaire avant correction
- Chaque nouvelle fonctionnalité doit être couverte par un test avant implémentation
- Les incohérences mineures et typos peuvent être corrigées

## Documentation
### README
- Doit expliquer le but du repository
- Doit être exempt de fautes de frappe, erreurs de grammaire
- Doit être aussi court que possible sans dupliquer la doc du code

### Documentation du code
- Chaque classe doit avoir un docblock précédant
- Le docblock de classe doit expliquer le but et fournir des exemples d'usage
- Chaque méthode et fonction doit avoir un docblock
- Docblocks uniquement en français, encodage UTF-8

## Style de code
- Les corps de méthodes ne doivent pas contenir de lignes vides
- Les corps de méthodes et fonctions ne doivent pas contenir de commentaires
- Les noms de variables doivent être des noms simples, jamais composés
- Les noms de méthodes doivent être des verbes simples, jamais composés
- Respecter le principe des "Paired Brackets" de Yegor Bugayenko
- Les messages d'erreur et de log ne doivent pas finir par un point
- Les messages d'erreur et de log doivent être une seule phrase, sans points internes
- Privilégier "fail fast" plutôt que "fail safe" : lancer les exceptions au plus tôt

## Conception des classes (Elegant Objects)
### Constructeurs
- Ne peuvent contenir que des affectations
- Un seul constructeur principal par classe
- Les constructeurs secondaires (factory statique) doivent déléguer au principal

### Structure des classes
- L'héritage d'implémentation doit être évité à tout prix
- Éviter les getters (symptômes d'un modèle objet anémique)
- Éviter les setters (rendent les objets mutables)
- Privilégier les objets immuables
- Chaque classe encapsule 1 à 4 attributs maximum
- Classes utilitaires strictement interdites
- Méthodes statiques dans les classes strictement interdites
- Toutes les classes doivent être déclarées `final`
- Les noms de classes ne peuvent pas finir par -er

### Méthodes
- Doivent être déclarées dans des interfaces puis implémentées
- Éviter les méthodes publiques qui n'implémentent pas une interface
- Ne doivent jamais retourner `null`
- `null` ne doit pas être passé en argument
- Éviter de vérifier la validité des arguments entrants
- Respecter le principe CQRS : méthodes comme noms ou verbes
- Les messages d'exception doivent inclure le maximum de contexte

### Principes architecturaux
- Respecter le paradigme Domain-Driven Design (DDD)
- Respecter les principes de conception Elegant Objects
- Éviter les constantes statiques publiques
- L'introspection de type et le casting sont strictement interdits
- La réflexion sur les éléments internes des objets est interdite

## Principes de tests
### Organisation
- Chaque changement doit être couvert par un test unitaire
- Chaque cas de test ne peut contenir qu'une seule assertion
- L'assertion doit être la dernière instruction du test
- Les cas de test doivent être aussi courts que possible
- Chaque test doit asserter au moins une fois
- Chaque fichier de test doit correspondre 1:1 avec le fichier testé
- Chaque assertion doit inclure un message d'échec formulé négativement

### Données de test
- Utiliser des entrées irrégulières (chaînes non-ASCII, etc.)
- Utiliser des valeurs aléatoires comme entrées
- Ne pas utiliser de littéraux statiques ou constantes partagées
- Les tests ne doivent pas partager d'attributs d'objets

### Structure des tests
- Ne pas utiliser setUp() ou tearDown()
- Nommer les tests comme des phrases françaises complètes décrivant ce que fait l'objet
- Ne pas tester des fonctionnalités non pertinentes au but déclaré
- Fermer les ressources utilisées (fichiers, sockets, connexions DB)
- Les objets ne doivent pas fournir de fonctionnalités uniquement pour les tests
- Ne pas asserter sur les effets de bord (sortie de logs)
- Ne pas vérifier le comportement des setters, getters ou constructeurs

### Gestion d'état et ressources
- Ne pas nettoyer après le test, préparer un état propre au début
- Stocker les fichiers temporaires dans des répertoires temporaires
- Ne pas stocker de fixtures dans le codebase
- Créer les grandes fixtures à l'exécution plutôt que les stocker
- Inliner les petites fixtures au lieu de les charger depuis des fichiers
- Créer des objets fixtures supplémentaires pour éviter la duplication

### Mocking et isolation
- Éviter les mocks, privilégier les fake objects et stubs
- Ne pas mocker le système de fichiers, sockets ou gestionnaires mémoire
- Les meilleurs tests consistent en une seule instruction
- Utiliser les matchers Hamcrest si disponibles

### Tests avancés
- Chaque test vérifie un seul pattern comportemental spécifique
- Utiliser des ports TCP éphémères générés par les fonctions appropriées
- Les tests ne doivent pas attendre indéfiniment, toujours avec timeout
- Vérifier le comportement en environnements multi-threads/concurrents
- Réessayer les blocs de code potentiellement instables
- Assumer l'absence de connexion Internet
- Ne pas asserter sur les messages ou codes d'erreur
- Ne pas se fier aux configurations par défaut, fournir des arguments custom
- Les méthodes de test épellent "cannot" et "dont" sans apostrophes

### Logging dans les tests
- Les tests ne doivent pas afficher de messages de log
- Le framework de test doit être configuré pour désactiver les logs des objets testés

