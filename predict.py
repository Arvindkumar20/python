import pickle
import sys
import traceback
from generate import feature_create

def load_model(model_path):
    try:
        with open(model_path, 'rb') as file:
            return pickle.load(file)
    except Exception as e:
        print(f"Error loading model: {e}", file=sys.stderr)
        traceback.print_exc()
        sys.exit(1)

def generate_features(arg1, arg2):
    try:
        return feature_create(arg1, arg2)[0]  # Ensure it returns a 1D array
    except Exception as e:
        print(f"Error generating features: {e}", file=sys.stderr)
        traceback.print_exc()
        sys.exit(1)

def predict(model, features):
    try:
        result = model.predict([features])  # Ensure it's passed as a 2D array
        print(result[0])  # Output the first prediction
    except Exception as e:
        print(f"Error during prediction: {e}", file=sys.stderr)
        traceback.print_exc()
        sys.exit(1)

def main():
    if len(sys.argv) < 3:
        print("Usage: python predict.py <arg1> <arg2>", file=sys.stderr)
        sys.exit(1)

    arg1, arg2 = sys.argv[1], sys.argv[2]

    model = load_model('./model.pkl')  # Ensure the path is correct
    features = generate_features(arg1, arg2)
    predict(model, features)

if __name__ == "__main__":
    main()
