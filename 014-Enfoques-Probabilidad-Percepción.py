import numpy as np  # Agregamos la importación de NumPy

class NaiveBayesClassifier:
    def __init__(self, categories):
        self.categories = categories
        self.word_counts = {category: {} for category in categories}
        self.category_counts = {category: 0 for category in categories}
        self.total_documents = 0

    def train(self, documents, labels):
        for document, label in zip(documents, labels):
            self.category_counts[label] += 1
            self.total_documents += 1
            for word in document.split():
                if word not in self.word_counts[label]:
                    self.word_counts[label][word] = 1
                else:
                    self.word_counts[label][word] += 1

    def predict(self, document):
        best_category = None
        max_probability = -1
        for category in self.categories:
            category_probability = self.category_counts[category] / self.total_documents
            log_probability = 0
            for word in document.split():
                if word in self.word_counts[category]:
                    word_probability = (self.word_counts[category][word] + 1) / \
                                       (sum(self.word_counts[category].values()) + len(self.word_counts[category]))
                else:
                    word_probability = 1 / (sum(self.word_counts[category].values()) + len(self.word_counts[category]))
                log_probability += np.log(word_probability)
            combined_probability = np.log(category_probability) + log_probability
            if combined_probability > max_probability:
                max_probability = combined_probability
                best_category = category
        return best_category

# Ejemplo de uso
documents = [
    "buen clima agradable",
    "horrible malo triste",
    "divertido alegre positivo",
    "terrible desastroso negativo"
]
labels = ["positivo", "negativo", "positivo", "negativo"]

classifier = NaiveBayesClassifier(categories=["positivo", "negativo"])
classifier.train(documents, labels)

test_document = "clima agradable y divertido"
predicted_category = classifier.predict(test_document)
print(f"El documento '{test_document}' fue clasificado como '{predicted_category}'")
