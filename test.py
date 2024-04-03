from inference_sdk import InferenceHTTPClient

CLIENT = InferenceHTTPClient(
    api_url="https://detect.roboflow.com",
    api_key="WmSsMwjYZwXvm0GsDeCO"
)

result = CLIENT.infer(your_image.jpg, model_id="furniture-appcw/1")