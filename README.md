
 
![banner_main](https://raw.githubusercontent.com/epicalekspwner/miscellaneous/main/groupAmazon_banner_main_v2.svg)

<p align="center">
  <img src="https://raw.githubusercontent.com/epicalekspwner/miscellaneous/main/groupAmazon_central_banner.gif" />
</p>


![banner_team](https://raw.githubusercontent.com/epicalekspwner/miscellaneous/main/groupAmazon_banner_team.svg)

### 🕵️ Project Description

<p align="justify"> 
  <strong>To improve one’s skills in a new foreign language, it is important to read texts in this language.</strong> But in order to make learning really effective, these text have to be at the reader’s language level. However, it is difficult to find texts that are close to someone’s knowledge level (A1 to C2).
</p>

<p align="justify"> 
  This project aims to build a model for English speakers that <strong>predicts the difficulty of a French written text</strong>. This can be then used, e.g., in a recommendation system, to recommend texts that are appropriate for someone’s language level. If someone is at A1 French level, it is inappropriate to present a text at B2 level, as she won’t be able to understand it. Ideally, a text should have many known words and may have a few words that are unknown so that the person can improve.
</p>

<p align="justify">
  This project is <strong>iterative</strong> and will be conducted in <strong>multiple milestones</strong> that are due throughout the semester:
</p>

- **Milestone 1** (due March 15) - Reading/Thinking & Gathering the data 
- **Milestone 2** (due April 13) - Creating/Evaluating the model
- **Milestone 3** (due May 10) - Iterate & Improve 

### 📚 Review of the Existing Literature

🥨 **Learning German** 
- [Vlachos, Michalis & Lappas, Theodoros. 2011. "Ranking German texts by comprehensibility for foreign document retrieval." *Proceedings of the 34th international ACM SIGIR conference on enriching in Information Retrieval*.](http://alumni.cs.ucr.edu/~mvlachos/pubs/ENIR2011.pdf)

🥖 **Learning French**
- [Mesnager, Jean. 2011. "Le vocabulaire et son enseignement : Le vocabulaire et son enseignement." *Ministère de l'Éducation nationale, de la Jeunesse et des Sports*.](https://cache.media.eduscol.education.fr/file/Dossier_vocabulaire/57/4/Jean_Mesnager_111202_C_201574.pdf)

🐟 **Learning Portuguese**
- [Curto, Pedro & Mamede, Nuno & Baptista, Jorge. 2015. "Automatic text difficulty classifier." *Assisting the selection of adequate reading materials for European Portuguese teaching. Proceedings of CSEDU*: 36-44.](https://www.inesc-id.pt/publications/11043/pdf)

### 💭 How Do We Intend to Solve the Problem?

<p align="justify"> 
 After much thought, we plan to approach this project as a <strong>classification problem</strong>. After building our model and training it, the output of out model is to <strong>predict a discrete class label</strong>, i.e., in our case, <strong>predict the difficulty of a unlabelled sentence</strong> (from A1 to C2). Modeling this problem as a classification problem will also allow us to evaluate the model in terms of <strong>accuracy</strong>, whose interpretation is intuitive in our case.
 
 The <strong>feature engineering</strong> we wish to explore can be reprensented by the following points:
</p>

📃 **Words**
- Categorize the **different types of words** (Part-Of-Speech Tagger)
- Count the **word frequency** for each categorie (i.e., the more frequent a word is, the easier it should be to be assimilated)
- Create a **dictionary** for each level that contains the **most frequent words**
- Analyze the **grouping of letters**
- Deal with **deceptive cognates** (i.e. words that resemble French ones, but do not have the same meaning) (list of 139 most common deceptive cognates)
- Deal with **cognates** (i.e. words that resemble French ones and from which one can deduce the meaning): 2 possible options
- **1<sup>st</sup> solution**: list of 58,000 english words (need to be translated into French and then lemmetized both to obtain similar roots)
- **2<sup>nd</sup> solution**: look at the suffixes (e.g. words ending by "tion" have a high probabilty to have a straightforward translation in English)

📃 **Sentences**
- Measure the **length of sentences** (i.e., the shorter the sentence, the easier it is to understand and vice versa)
- Count **punctuation** (i.e., a more complex sentence will tend to contain more punctuation to handle grammatical difficulty)
- Count the **different types of words** (i.e., a complex sentence will tend to be composed of a combination of several different types of words (noun, verb, adverb, pronoun, preposition, conjunction, etc.)

🤖 **Potential Algorithms**

- **Logistic Regression**
- **Naive Bayes Classifier**
- **K-nearest Neighbors**
- **Decision Tree**

📦 **Libraries We Intend to Use**
- NLTK Snowball (Stemmer)
- Spacy French LEFFF
- French specific libraries
- And more 😉


### Milestone 2 - Creating/Evaluating the model

`Dataset used: Team Amazon dataset`

####  **First model using: Text Classification in Google Cloud Natural Language Automl**

- Model type: **Single-label classification**
- Test items: **102**
- Precision: **80%**
- Recall: **35.29%**

🗜️ **Confusion matrix**

![Confusion matrix](https://user-images.githubusercontent.com/71261918/114360514-643b0300-9b75-11eb-9e1f-ae019275a54b.png)

**Note 1**: We can see that the model has difficulties at predicting B2 and C1 levels. One of the reasons might be the assessment of these levels by our team. One solution could be reevaluating these two levels more carefully.

**Note 2**: Our model is super sensible to the length of the sentence. If we put mutiple times a really simple sentence it will end up with a C2 level.we need to reevaluate !

####  **Custom model: Features Engineering**

|Done| Feature Name | Method |
|---|---------------------         |-------------------------------------------------------------------------|
|✔️| *Sentences lengths*           |  Return the length of the sentence                             |
|✔️| *Type of words*               |  Return a dict {"Word": "Type of word"}                        | 
|✔️| *Number of punctuation*       |  Return the number of punctuation there is in the sentence |
|✔️| *Deceptive cognates*          |  Return the number of deceptive cognomes there is in the sentence (see graph (a)) | 
|✔️| *Cognates*                    |  Return list of 14k possible cognates and the similarity between the two roots (french and english)|
|❌| *Common words for each category*     |  Creation of list with the most common words for each category.| |

**Deceptive cognomes graphic (a):**

![Avg_Dcognate_plot](https://user-images.githubusercontent.com/71261918/114367569-da8f3380-9b7c-11eb-8e36-ec9dfb26e051.PNG)

We can see on the above graph that the more complex a sentence is, the more deceptive cognates (aka false friends) there are.

### Milestone 3 - Iterate & Improve

`Dataset used: TAs' dataset`

![am0ngsusxh-45](https://user-images.githubusercontent.com/71261918/117670351-17fcd600-b1a8-11eb-9602-d74bc92eb7ff.gif)

**Our application**: [!!!!!! Click-here !!!!!!](https://epicalekspwner-bsa2021.uc.r.appspot.com/)


==> We used the datatset provided by the TAs to do the models (previsously (M2) we used our dataset which was biased)


We used several models from basic one (linear regression) to more complex ones (GC). From the various models we used the model from Google Cloud Natural language classification model is the BEST with an accuracy on Aicrowd of 53.3%. We tried a few combination but unfortunatly it did not improve our ranking on Aicrowd.

**What did we use as librairies or services?**
- Cloud services: Google AutoML (Regression and NLP), Google colab
- NLP Librairies: Spacy(Multi-langual package), NLTK (Multi-langual package), Camembert (French package)
- Machine Learning librairies: SKlearn
- App: Flask

**General architecture:**

![image](https://user-images.githubusercontent.com/71261918/119941219-9a4f0d80-bf90-11eb-9c0a-ad5392bb9da6.png)

**Cognates problem**:

The idea: when we were young our teachers gave us some "tips" on how to detect cognates from french to english. We had to look for the suffixes...

![image](https://user-images.githubusercontent.com/71261918/119940404-6aebd100-bf8f-11eb-8357-8697452d556f.png)

**Deceptive cognates**

We also took into account false friends and created a function that count the number of deceptive cognates in order to integrate it into our models.


**Models evaluation**

| **Model**                   | **Parameters**                                                      |**Internal Accuracy/R² or Google Cloud Precision/Recall/R²**|  **Accuracy Aicrowd submission**|**Evaluation**|**Note**|
|----------------------------------------------------------|-------------------------------------------------------------------------------|------------------------|------------|-----------------|---------|
**Regression Algo (RA) 📈 📉**   
| `**Linear regression (1)**`  |param: `None`|R²: 0.31|`None`|`None`|bLABLAH|
| `**Logistic regression (2)**`    |param: standardization, penalty = 'l2',solver='lbfgs', cv=8, max_iter=3000, random_state=72|R²: 0.37|`None`|`None`|bLABLAH|             
| `**Support vector machine Regression (3)**` |param: StandardScaler(), SVR(C=5, epsilon=0.8), round()|R²: 0.46|Accuracy: 0.49|`None`|bLABLAH|
|||||||
**Regression Algo Camembert package (RACAM) 📈 📉 🧀**   
| `**Linear regression (1)**`  |param: `None`|R²: 0.36|`None`|`None`|bLABLAH|
| `**Logistic regression (2)**`    |param: standardization, penalty = 'l2',solver='lbfgs', cv=8, max_iter=3000, random_state=72|R²: 0.41|`None`|  `None`|bLABLAH|           
| `**Support vector machine Regression (3)**` |param: StandardScaler(), SVR(C=1, epsilon=1), round()|R²: 0.54|`None`|`None`|bLABLAH|
|||||||
**Classification Algo 📁📂(CA)**        
| `**Support vector classifier (1)**`  |param: C=6|F1: 41%|`None`|![image](https://user-images.githubusercontent.com/71261918/119943463-5dd0e100-bf93-11eb-9d06-b278cb46eb40.png)|bLABLAH|
| `**Support vector classifier Camembert (1.2)**`  |param: C=3|F1: 45%|`None`|![image](https://user-images.githubusercontent.com/71261918/119943653-9cff3200-bf93-11eb-9214-45b9a0b23c56.png)|bLABLAH|
| `**Logistic Regression (2)**`  |param: 'LR__C': 6, 'LR__max_iter': 1000 |F1: 39%|`None`|![image](https://user-images.githubusercontent.com/71261918/119943715-b1dbc580-bf93-11eb-83c7-c9dfa600d3d0.png)|bLABLAH|
| `**KNNeighbours (3)**`  |param: 'knn__leaf_size': 10, 'knn__n_neighbors': 17, 'knn__p': 1, 'knn__weights': 'uniform' |F1: 38%|`None`|![image](https://user-images.githubusercontent.com/71261918/119943752-bbfdc400-bf93-11eb-8fba-0f16ea7ce4f7.png)|bLABLAH|
| `**Decision Trees (4)**` |param: 'DT__max_depth': 3, 'DT__min_samples_split': 5 |F1: 33%|`None`|![image](https://user-images.githubusercontent.com/71261918/119943773-c4ee9580-bf93-11eb-9c6f-253fba7dea2b.png)|bLABLAH|
| `**Random Forest (5)**` |param: 'RF__bootstrap': True, 'RF__criterion': 'entropy', 'RF__n_estimators': 18|F1: 45%|`None`|![image](https://user-images.githubusercontent.com/71261918/119943791-cddf6700-bf93-11eb-8acd-453115e39a29.png)|bLABLAH|
||||||
**Google Cloud ⛅️(GC)** 
| `**Classification problem (1)**`  |param: `None` |Precision: 58.51% & Recall: 35.41% & F1: 44%| Accuracy: **53.3%**|![image](https://user-images.githubusercontent.com/71261918/119943928-f4050700-bf93-11eb-9d57-6d096bd3234a.png)|bLABLAH|
| `**Classification problem lemma(2)**`  |param:`None`|Precision: 60.94% & Recall: 29.96% & F1: 40%|`None`|![image](https://user-images.githubusercontent.com/71261918/119944244-50682680-bf94-11eb-8135-759e2c1ce622.png)|bLABLAH|
| `**Regression problem (3)**` |param: `None`|R²: 0.497|`None`|`None`|bLABLAH|
| `**Classification problem (3)**`  |param: dataset sentence length reduced |Precision: 61.6% & Recall: 43.02% & F1: 51%| Accuracy: 51.1%|![image](https://user-images.githubusercontent.com/71261918/119944124-2e6ea400-bf94-11eb-83b6-c613fb14b760.png)|bLABLAH|
|||||||
**Algo combination** 
| `**GC (1) + GC (2)**`  |param: (1): A2,B1,C1 & (2): A1,B2,C2|`None`|Accuracy:  51.5% (base (2)) & 52.8% (base (1))|`None`||
| `**GC (1) + RA (3)**`  |param: `None`|`None`|Accuracy: 44%|`None`||


### Sources

#### Cognates

- English word list: https://github.com/dwyl/english-words/blob/master/words_alpha.txt
- English/French suffixes: 'Code de Traduction' https://www.anglaisfacile.com/exercices/exercice-anglais-2/exercice-anglais-70779.php
- Deceptive cognates: https://www.laurentbloch.net/MySpip3/Faux-amis-Deceptive-Cognates
- French stop words (We did some modification and removed/added some element): https://github.com/stopwords-iso/stopwords-fr/blob/master/stopwords-fr.txt

#### Dataset

📗 **Books**

- Barnes, Djurna. 1986. *Le Bois de la nuit*. Points roman.
- Césaire, Aimé. 1939. *Cahier d'un retour au pays natal*. Paris: Pierre Bordas.
- De Beauvoir, Simone. 1949. *Le Deuxième Sexe*. Paris: NRF.
- De La Fontaine, Jean. 1778. *Fables de La Fontaine*. Fides.
- De Maupassant, Guy. 1885. *Bel-Ami*. Paris: Victor Havard.
- De Maupassant, Guy. 1887. *Le Horla*. Paris: Paul Ollendorff.
- De Saint-Exupéry, Antoine. 1943. *Le petit prince*. Paris: Gallimard.
- Diome, Fatou. 2003. *Le ventre de l'Atlantique*. Paris: Anne Carrière.
- Flaubert, Gustave. 1857. *Madame Bovary*. Paris: Michel Lévy frères.
- Echenoz, Jean. 2001. *Jérôme Lindon*. Paris: Éditions de Minuit.
- Pennac, Daniel. 2007. *Chagrin d'école*. Paris: Éditions Gallimard.
- Proust, Marcel. 1913. *Du côté de chez Swann*. Paris: Bernard Grasset.
- Proust, Marcel. 1918. *À l'ombre des jeunes filles en fleurs*. Paris: Éditions Gallimard.
- Queneau, Raymond. 1947. *Exercices de style*. Paris: Gallimard.
- Rostand, Edmond. 1898. *Cyrano de Bergerac*. Paris: Charpentier et Fasquelle.
- Schmitt, Éric-Emmanuel. 2001. *Monsieur Ibrahim et les fleurs du Coran*. Paris: Albin Michel.
- Verne, Jules. 1896. *Vingt mille lieues sous les mers*. Paris: Hetzel.
- Voltaire. 1759. *Candide*. Genève: Gabriel Cramer.
- Zola, Émile. 1883. *Au bonheur des dames*. Paris:	Georges Charpentier.
- Zola, Émile. 1877. *L’Assommoir*. Paris:	Georges Charpentier.

🔬 **Studies**

- [Klaus, Jacopo. 2019. "Les défis de l'aménagement du territoire dans un système fédéral. L'évolution du rôle des cantons et des communes suisses entre limitations quantitatives et enjeux qualitatifs de l'urbanisation" *Thesis, University of Lausanne*.](https://serval.unil.ch/resource/serval:BIB_4078770716B1.P001/REF)
- [OECD. 2019. *Études économiques de l’OCDE : Sythèse sur la Suisse*.](http://www.oecd.org/fr/economie/etudes/Suisse-2019-OCDE-etudes-economique-synthese.pdf)
- [Office fédéral de la statistique. 2020. *Endettement : Arriérés de paiement en 2019*.](https://www.bfs.admin.ch/bfs/fr/home/statistiques/situation-economique-sociale-population/revenus-consommation-et-fortune/endettement.html)
- [Office fédéral de la statistique. 2019. *Énergie : Aspects économiques*.](https://www.bfs.admin.ch/bfs/fr/home/statistiques/energie/aspects-economiques.html)
- [Office fédéral de la statistique. 2020. *Enquête suisse sur la santé (ESS) 2017 : Santé et genre*.](https://www.bfs.admin.ch/asset/fr/213-1719)
- [Office fédéral de la statistique. 2020. *Le système d'indicateurs «Mesure du bien-être»*.](https://www.bfs.admin.ch/asset/fr/1877-2000)
- [Office fédéral de la statistique. 2020. *Panorama de la société suisse 2020*.](https://www.bfs.admin.ch/asset/fr/2016-2000)
- [Office fédéral de la statistique. 2020. *Transport routier, ferroviaire et aérien : Coûts et financement des transports 2017*.](https://www.bfs.admin.ch/asset/fr/812-1700)
- [Pauchard, Nicolas. 2019. "Gouverner les ressources génétiques. Les stratégies des acteurs face aux droits de propriété et aux règles sur l'accès et le partage des avantages" *Thesis, University of Lausanne*.](https://serval.unil.ch/resource/serval:BIB_9DBCC86F5780.P002/REF)

📰 **Online Articles**

- [AFP. 2021. "Spotify se lance dans plus de 80 nouveaux pays." *Le Temps*, February 23, 2021.](https://www.letemps.ch/economie/spotify-se-lance-plus-80-nouveaux-pays)
- [ATS. 2021. "Plus d'un tiers des appartements suisses sont occupés par des personnes seules." *Le Temps* February 25, 2021.](https://www.letemps.ch/suisse/plus-dun-tiers-appartements-suisses-occupes-personnes-seules)
- [Bazin, Xavier. 2021. "Vaccin en Israël : des chiffres troublants." *FranceSoir*, February 25, 2021.](https://www.francesoir.fr/opinions-tribunes/vaccin-en-israel-des-chiffres-troublants)
- [Colleu, Yannick. 2021. "COVID 19 : les données de Santé Publique France sont-elles fiables ?" *FranceSoir*, February 24, 2021.](https://www.francesoir.fr/opinions-tribunes/les-donnees-de-sante-publique-france-sont-elles-fiables)
- [Etienne, Richard. 2021. "Genève accorde un prêt historique de 200 millions à l’aéroport de Cointrin." *Le Temps*, February 25, 2021.](https://www.letemps.ch/economie/geneve-accorde-un-pret-historique-200-millions-laeroport-cointrin)
- [Favre, Laurent. 2021. "Novak Djokovic est imbattable, la preuve par neuf." *Le Temps*, February 21, 2021.](https://www.letemps.ch/sport/novak-djokovic-imbattable-preuve-neuf)
- [FranceSoir, AFP. 2021. "Pays-Bas : le couvre-feu, objet d'un bras de fer judiciaire." *FranceSoir*, February 17, 2021.](https://www.francesoir.fr/politique-monde/covid19-au-pays-bas-la-levee-du-couvre-feu-suspendue-une-decision-de-justice)
- [FranceSoir. 2021. "Les néonicotinoïdes : une menace pour les mammifères." *FranceSoir*, February 21, 2021.](https://www.francesoir.fr/societe-environnement/les-neonicotinoides-une-menace-pour-les-mammiferes)
- [Genecand, Marie-Pierre. 2021. "La médiation de voisinage, comme si vous y étiez." *Le Temps*, February 8, 2021.](https://www.letemps.ch/societe/mediation-voisinage-y-etiez)

🌐 **Other Websites**

- [Bernard, Emeline. 2021. "10 erreurs à ne pas faire avec son chien selon les vétérinaires." *Ohmymag*, March 2, 2021.](https://www.ohmymag.com/animaux/10-erreurs-a-ne-pas-commettre-avec-son-chien_art141138.html)
- [Bourrelly, Pierre & Lefeuvre, Jean Claude. "CYANOBACTÉRIES ou CYANOPHYCÉES, anc. ALGUES BLEUES" *Encyclopædia Universalis*.](https://www.universalis.fr/encyclopedie/cyanobacteries-cyanophycees-algues-bleues/)
- ["French Texts for Beginners". *Lingua*.](https://lingua.com/french/reading/)
- [La Dépêche. 2021. "Tout savoir avant d’adopter un chat." *La Dépêche*, February 24, 2021.](https://www.ladepeche.fr/2021/02/24/tout-savoir-avant-dadopter-un-chat-9391356.php)
- [Lavorel, Jean & Mazliak, Paul & Moyse, Alexis. "PHOTOSYNTHÈSE" *Encyclopædia Universalis*.](https://www.universalis.fr/encyclopedie/photosynthese/)

