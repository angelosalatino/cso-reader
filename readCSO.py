#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Dec 13 17:51:09 2024

@author: Angelo Salatino
"""

from cso_reader import Ontology


ont = Ontology()


print(ont.ontology_attr)


print(f"Total concepts: {len(ont.topics)}")


unique_concepts = {ont.get_primary_label(topic) for topic, _ in ont.topics.items()}

print(f"Total unique concepts: {len(unique_concepts)}")


### Example: Count all topics with more that one unigram
count = 0
for topic, _ in ont.topics.items():
    if (' ' in topic) == True:
        count += 1
        
print(f"Total topics with more than 1 gram: {count}")