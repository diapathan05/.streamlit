import google.generativeai as genai

genai.configure(api_key="AIzaSyBSCBS4FlyS022uD8W_zg5Dv_rcebNe6m4")

for m in genai.list_models():
    print(m.name)                                                   