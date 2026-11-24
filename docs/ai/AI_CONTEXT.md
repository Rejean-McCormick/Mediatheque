<!-- kOA Doc Server · Docs IA · lot 02 · rédaction dérivée d’une capture, à valider par le propriétaire -->
# Navigation IA — mediatheque

**Rôle observé :** Moteur partagé de garde de sources, versions, représentations et reçus d'intégrité.

**Autorité :** Chaque instance détient son contenu et ses permissions; le moteur n'est ni Kristal ni autorité sémantique.

**Provenance :** `SmartDump_20261120_221507.zip` → `mediatheque_Code_snapshot.zip` (20 novembre 2026). Cette capture ne prouve ni la présence actuelle du dossier Windows, ni un déploiement, ni une qualification.

## Objet et état de cette fiche

La description ci-dessous est rattachée au `README.md` du snapshot; vérifier le code actif sur le poste. Cette fiche est un **guide de navigation**, non une spécification normative ni une validation de maturité.

## Processus conseillé

1. **Identifier la source et le profil.** Configurer une instance sœur et son content root, examiner les contrats, puis vérifier intégrité et isolation.
2. **Contrôler l’autorité.** Chaque instance détient son contenu et ses permissions; le moteur n'est ni Kristal ni autorité sémantique.
3. **Préparer un environnement de test.** Utiliser les fichiers réels de la révision étudiée et des données fictives ou autorisées.
4. **Vérifier sans promouvoir.** Documenter commandes, périmètre, résultat, chemins et empreintes; ne jamais transformer une observation locale en preuve historique validée.
5. **Revue propriétaire.** Une publication, activation, import ou effet externe nécessite l’accord du propriétaire et les gates correspondants.

## Garde-fous particuliers

- Ne jamais copier le moteur dans une instance ni confondre un reçu source avec un droit de publication.
- N’inclure aucun secret, donnée personnelle, sauvegarde privée ou sortie de diagnostic non autorisée dans les exports Doc Server.
- Préserver l’intégrité des sources et des états historiques; éviter toute réécriture automatique des références.

## Sources d’orientation vérifiables dans le snapshot

1. [`README.md`](../../README.md) — source propriétaire présente dans le snapshot.
2. [`docs/03_folder_architecture.md`](../../docs/03_folder_architecture.md) — source propriétaire présente dans le snapshot.
3. [`docs/09_json_validation.md`](../../docs/09_json_validation.md) — source propriétaire présente dans le snapshot.
4. [`docs/10_ps7_contract.md`](../../docs/10_ps7_contract.md) — source propriétaire présente dans le snapshot.
5. [`docs/20_kristal_source_validation_20261002.md`](../../docs/20_kristal_source_validation_20261002.md) — source propriétaire présente dans le snapshot.
6. [`docs/21_deployment_modes.md`](../../docs/21_deployment_modes.md) — source propriétaire présente dans le snapshot.
7. [`docs/UPDATE_0.5.1_VALIDATION_FR.md`](../../docs/UPDATE_0.5.1_VALIDATION_FR.md) — source propriétaire présente dans le snapshot.
8. [`docs/00_START_HERE.instructions.md`](../../docs/00_START_HERE.instructions.md) — source propriétaire présente dans le snapshot.

## Compatibilité Framework

S’il y a une dépendance Kristal, lire la révision du Framework et le profil **effectivement adoptés** par ce dépôt. Les nouvelles conventions v11 (identités sémantiques, dictionnaires séparés, provenance) servent de référence lorsque compatibles; **ne pas bloquer** la navigation IA ni imposer la migration de données historiques pour cette seule raison.
