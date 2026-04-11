# lime.py
#
# Simple LIME-style local explanation demo
# Uses Naive Bayes on the Play Tennis-style dataset
# Explains predictions by checking how feature changes affect the output

import math
import random

# ----------------------- Dataset -----------------------
# Each row: [Outlook, Temp, Play]
dataset = [
    ['Sunny', 'Hot', 'No'],
    ['Sunny', 'Hot', 'No'],
    ['Overcast', 'Hot', 'Yes'],
    ['Rain', 'Mild', 'Yes'],
    ['Rain', 'Cool', 'Yes'],
    ['Rain', 'Cool', 'No'],
    ['Overcast', 'Cool', 'Yes'],
    ['Sunny', 'Mild', 'No'],
    ['Sunny', 'Cool', 'Yes'],
    ['Rain', 'Mild', 'Yes'],
    ['Sunny', 'Mild', 'Yes'],
    ['Overcast', 'Mild', 'Yes'],
    ['Overcast', 'Hot', 'Yes'],
    ['Rain', 'Mild', 'No']
]

features = ["Outlook", "Temp"]  # feature names


# ----------------------- Naive Bayes -----------------------
def train_naive_bayes(data):
    label_counts = {}      # e.g., {'Yes': 9, 'No': 5}
    feature_counts = {}    # nested dict

    for row in data:
        outlook, temp, label = row

        # label count
        label_counts[label] = label_counts.get(label, 0) + 1

        if label not in feature_counts:
            feature_counts[label] = {"Outlook": {}, "Temp": {}}

        feature_counts[label]["Outlook"][outlook] = \
            feature_counts[label]["Outlook"].get(outlook, 0) + 1

        feature_counts[label]["Temp"][temp] = \
            feature_counts[label]["Temp"].get(temp, 0) + 1

    return label_counts, feature_counts


def predict_naive_bayes(x, label_counts, feature_counts):
    """
    x = [Outlook, Temp]
    returns predicted label ("Yes"/"No")
    """
    total_samples = sum(label_counts.values())
    probs = {}

    for label in label_counts:
        # prior log P(label)
        probs[label] = math.log(label_counts[label] / total_samples)

        for i, feature in enumerate(features):
            value = x[i]
            count = feature_counts[label][feature].get(value, 0)
            total_feature_count = label_counts[label]
            unique_vals = len(feature_counts[label][feature])

            # Laplace smoothing
            likelihood = (count + 1) / (total_feature_count + unique_vals)
            probs[label] += math.log(likelihood)

    return max(probs, key=probs.get)


# ----------------------- Helper: possible values -----------------------
def get_possible_values(data):
    """
    Return all possible values for each feature from the dataset.
    """
    values = {f: set() for f in features}
    for row in data:
        outlook, temp, label = row
        values["Outlook"].add(outlook)
        values["Temp"].add(temp)
    return {f: list(vs) for f, vs in values.items()}


possible_values = get_possible_values(dataset)


# ----------------------- LIME-style explanation -----------------------
def generate_neighbor(instance):
    """
    Create a random neighbor by randomly changing each feature
    with probability 0.5 (simple tabular perturbation).
    """
    new_instance = instance[:]
    for i, feat in enumerate(features):
        if random.random() < 0.5:
            vals = possible_values[feat][:]
            if new_instance[i] in vals and len(vals) > 1:
                vals.remove(new_instance[i])
            new_instance[i] = random.choice(vals)
    return new_instance


def lime_explain(instance, label_counts, feature_counts, n_neighbors=100):
    """
    Very simple LIME-style explanation:
    - Generate neighbors around the instance
    - For each feature, measure how often changing that feature
      changes the model's prediction.
    - Return: base prediction, feature importance dict.
    """
    base_pred = predict_naive_bayes(instance, label_counts, feature_counts)

    flip_counts = {f: 0 for f in features}     # how often feature change flips prediction
    change_counts = {f: 0 for f in features}   # how often feature is changed

    for _ in range(n_neighbors):
        neighbor = generate_neighbor(instance)

        changed = []
        for i, feat in enumerate(features):
            if neighbor[i] != instance[i]:
                changed.append(feat)
                change_counts[feat] += 1

        if not changed:
            continue

        pred_neighbor = predict_naive_bayes(neighbor, label_counts, feature_counts)

        if pred_neighbor != base_pred:
            for feat in changed:
                flip_counts[feat] += 1

    # importance = how often change in feature flips the prediction (0 to 1)
    importance = {}
    for feat in features:
        if change_counts[feat] == 0:
            importance[feat] = 0.0
        else:
            importance[feat] = flip_counts[feat] / float(change_counts[feat])

    return base_pred, importance


def print_lime_explanation(instance, base_pred, importance):
    print(f"Instance: {instance}, model prediction: {base_pred}")
    print("LIME-style feature importance (0 to 1):")
    for feat in features:
        print(f"  {feat}: {importance[feat]:.3f}")
    print()


# ----------------------- Main -----------------------
def main():
    label_counts, feature_counts = train_naive_bayes(dataset)

    test_samples = [
        ['Sunny', 'Cool'],
        ['Overcast', 'Mild'],
        ['Rain', 'Hot'],
        ['Sunny', 'Hot']
    ]

    print("=== LIME-style local explanations ===\n")

    for sample in test_samples:
        base_pred, importance = lime_explain(sample, label_counts, feature_counts, n_neighbors=100)
        print_lime_explanation(sample, base_pred, importance)


if __name__ == "__main__":
    main()
