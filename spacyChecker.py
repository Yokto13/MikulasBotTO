import spacy
import contextualSpellCheck

nlp = spacy.load('cz')
contextualSpellCheck.add_to_pipe(nlp)
doc = nlp('Dobry den, jak s mate?')

print(doc._.performed_spellCheck) #Should be True
print(doc._.outcome_spellCheck) #Income was $9.4 million compared to the prior year of $2.7 million.
