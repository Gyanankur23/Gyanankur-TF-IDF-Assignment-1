import streamlit as st
import math

#docs
docs = [
    "Apples are tasty and good for health",                   
    "Python helps automate repetitive coding tasks",          
    "Dogs are loyal pets and playful companions",              
    "Books contain stories, knowledge and inspiration",        
    "Exercise improves strength and boosts energy",            
    "Coffee increases alertness during early mornings",        
    "Travel explores places and creates new memories",         
    "Music reduces stress and helps calm the mind",            
    "Data helps businesses make smart decisions",              
    "Sunlight provides warmth, light and supports growth"      
]

#ground_truth
ground_truth = [
    ["apples", "tasty", "health"],                 
    ["python", "automate", "coding", "tasks"],     
    ["dogs", "loyal", "pets"],                     
    ["books", "stories", "knowledge"],             
    ["exercise", "energy", "strength"],           
    ["coffee", "alertness", "mornings"],           
    ["travel", "places", "memories", "explores"],  
    ["music", "stress", "calm", "mind"],           
    ["data", "smart", "businesses"],               
    ["sunlight", "light", "warmth", "growth"]      
]

idf, tfidf_docs = {}, []
N = len(docs)

for doc in docs:
    for word in set(doc.lower().split()):
        idf[word] = idf.get(word, 0) + 1
for word in idf:
    idf[word] = round(math.log((N + 1) / (idf[word] + 1)) + 1, 3)

for doc in docs:
    words = doc.lower().split()
    tf = {word: round(words.count(word)/len(words), 3) for word in words}
    tfidf_docs.append({word: round(tf[word]*idf[word], 3) for word in tf})

def accuracy(pred, actual):
    match = len(set(pred) & set(actual))
    return round((match / len(actual)) * 100, 2)

st.title("TF-IDF Accuracy Checker")
choice = st.selectbox("Select a sentence:", options=range(len(docs)), format_func=lambda i: docs[i])

top_keywords = sorted(tfidf_docs[choice], key=tfidf_docs[choice].get, reverse=True)[:3]
score = accuracy(top_keywords, ground_truth[choice])

st.write("Sentence:", docs[choice])
st.write("Top TF-IDF Keywords:", top_keywords)
st.write("Expected Keywords:", ground_truth[choice])
st.metric(label="Accuracy Score", value=f"{score}%")
