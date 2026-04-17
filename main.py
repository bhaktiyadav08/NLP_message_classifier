# main.py

from models.train_model import predict_message

if __name__ == "__main__":
    message = input("Enter a message: ")
    result = predict_message(message)

    print("\nPrediction:")
    print("Priority :", result["priority"])
    print("Complaint:", result["complaint"])
    print("Type     :", result["type"])