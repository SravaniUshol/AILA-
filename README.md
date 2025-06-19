# AILA-
INTRODUCTION

In countries following the Common Law system (e.g. UK, USA, Canada, Australia, India), there are two primary sources of law – Statutes and Precedents. Statutes are the prior cases decided in courts of law while Precedents are established laws, such as the Constitution of a country.

Statutes deal with applying legal principles to a situation (facts /scenario / circumstances which lead to filing the case).

Precedents or prior cases help a lawyer understand how the Court has dealt with similar scenarios in the past, and prepare the legal reasoning accordingly.

MOTIVATION

When a lawyer is presented with a situation (that will potentially lead to filing of a case), it will be very beneficial to one if there is an automatic system that identifies a set of related prior cases involving similar situations as well as statutes/acts that can be most suited to the purpose in the given situation.

APPLICATIONS

Such a system shall not only help a lawyer but also benefit a common man, in a way of getting a preliminary understanding of the legal aspects pertaining to a situation, even before one approaches a lawyer. The system can assist one in identifying where one's legal problem fits, what legal actions one can proceed with (through statutes) and what were the outcomes of similar cases (through precedents).

Motivated by the above scenario, the FIRE 2019 track on ‘Artificial Intelligence for Legal Assistance’ (AILA) proposed two tasks:

Identifying relevant prior cases for a given situation (Precedent Retrieval)
Identifying most relevant statutes for a given situation (Statute Retrieval).

Domain : This is a task in the domain of Natural Language Processing, Information Retrieval and Data Mining.


This repository contains python implimentations of the various methods described in the paper which include the following main techniques:
1. BERT
2. TF-IDF
   
 OBJECTIVES  
The AI Legal Assistance Project aims to create a user-friendly legal information system that 
will help both lawyers and everyday individuals find relevant legal information for their 
specific situations or questions. Here are the main goals of the project: 
1. Intelligent Information Retrieval : We want to design a system that makes it easier for 
users to identify legally relevant information tailored to their needs, whether they are legal 
professionals or not. 
2. Automated Case Retrieval : The project will include a mechanism that automatically 
fetches the most relevant past court cases from a database of Supreme Court of India 
judgments. This will be based on the specifics of a user’s legal query. 
3. Statutory Provision Identification : Our goal is to help users understand the applicable 
laws for their situation by identifying the relevant sections of Indian statutes, clarifying the 
legal foundations of their issues. 
4. Case Retrieval Modeling : We will approach case retrieval as a semantic matching 
problem. This means we will focus on ensuring that our system provides results that closely 
mirror how courts have handled similar cases in the past. 
5. Statute Identification Modeling : For statute identification, we will explore two 
approaches: an unsupervised method based on semantic similarity, or a supervised approach 
that uses labeled training data to detect relevance. 
6. Bridging the Legal Knowledge Gap : One of our key aims is to make legal expertise 
more accessible. We want to create a preliminary legal analysis tool that helps users 
comprehend how their issues fit within the broader legal landscape, what actions they might 
take, and the outcomes from similar cases in history. 
7. Enhancing Legal Accessibility : By leveraging natural language processing (NLP) and 
machine learning, we plan to improve efficiency in the legal field, allowing us to process 
extensive amounts of legal texts, statutes, and case law specific to the Indian context 
efficiently.
