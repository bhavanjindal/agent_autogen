from dotenv import load_dotenv
from openai import OpenAI
import pandas as pd
import json, os

load_dotenv()
client = OpenAI()

def intent_confirmation_layer(response_assistant):
    delimiter = "####"
    prompt = f""" 
    You are a senior evaluator who has an eye for detail.
    You are provided an input. You need to evaluate if the input has the following keys: 'GPU intensity','Display quality','Portability','Multitasking',' Processing speed','Budget'
    Next you need to evaluate if the keys have the the values filled correctly.
    The values for all keys, except 'budget', should be 'low', 'medium', or 'high' based on the importance as stated by user. The value for the key 'budget' needs to contain a number with currency.
    Output a string 'Yes' if the input contains the dictionary with the values correctly filled for all keys.
    Otherwise out the string 'No'.


    Here is the input: {response_assistant}
    Only output a one-word string - Yes/No.
    """

    confirmation = client.chat.completions.create(
        model="gpt-3.5-turbo-1106",
        prompt = prompt,
        temperature=0)

    return confirmation.choices[0].message.content


def dictionary_present(response):
    delimiter = "####"
    user_req = {'GPU intensity': 'high','Display quality': 'high','Portability': 'medium','Multitasking': 'high','Processing speed': 'high','Budget': '200000 INR'}
    prompt = f"""You are a python expert. You are provided an input.
            You have to check if there is a python dictionary present in the string.
            It will have the following format {user_req}.
            Your task is to just extract and return only the python dictionary from the input.
            The output should match the format as {user_req}.
            The output should contain the exact keys and values as present in the input.


            Here are some sample input output pairs for better understanding:
            {delimiter}
            input: - GPU intensity: low - Display quality: high - Portability: low - Multitasking: high - Processing speed: medium - Budget: 50,000 INR
            output: {{'GPU intensity': 'low', 'Display quality': 'high', 'Portability': 'low', 'Multitasking': 'high', 'Processing speed': 'medium', 'Budget': '50000'}}


            input: {{'GPU intensity':     'low', 'Display quality':     'high', 'Portability':    'low', 'Multitasking': 'high', 'Processing speed': 'medium', 'Budget': '90,000'}}
            output: {{'GPU intensity': 'low', 'Display quality': 'high', 'Portability': 'low', 'Multitasking': 'high', 'Processing speed': 'medium', 'Budget': '90000'}}


            input: Here is your user profile 'GPU intensity': 'high','Display quality': 'high','Portability': 'medium','Multitasking': 'low','Processing speed': 'high','Budget': '200000 INR'
            output: {{'GPU intensity': 'high','Display quality': 'high','Portability': 'medium','Multitasking': 'high','Processing speed': 'low','Budget': '200000'}}
            {delimiter}


            Here is the input {response}


            """


    response = OpenAI.chat.completions.create(
        model="gpt-3.5-turbo-1106",
        prompt=prompt,
        max_tokens = 2000
        # temperature=0.3,
        # top_p=0.4
    )
    return response.choices[0].message.content

def product_map_layer(laptop_description):


  delimiter = "#####"
  lap_spec = {
      "GPU intensity":"(Type of the Graphics Processor)",
      "Display quality":"(Screen Resolution)",
      "Portability":"(Laptop Weight)",
      "Multitasking":"(RAM)",
      "Processing speed":"(CPU Manufacturer, Core)"
  }


  values = {'low','medium','high'}


  prompt=f"""
  You are a Laptop Specifications Classifier whose job is to extract the key features of laptops as per their requirements.
  To analyze each laptop, perform the following steps:
  Step 1: Extract the laptop's primary features from the description {laptop_description}
  Step 2: Store the extracted features in {lap_spec} \
  Step 3: Classify each of the items in {lap_spec}into {values} based on the following rules: \
  {delimiter}
  GPU Intensity: low: < for entry-level graphics like Intel UHD > , \n
  medium: < if Mid-range dedicated graphics like M1, AMD Radeon, Intel Iris > , \n
  high: < High-end dedicated graphics like Nvidia, M2 > , \n


  Display Quality: low: < if resolution below Full HD (e.g., 1366x768). > , \n
  medium: < if Full HD resolution (1920x1080) > , \n
  high: < if High-resolution display (e.g., 4K, Retina) with excellent color accuracy and features like HDR support. > \n


  Portability: low: < if laptop weight is greater than 2.51 kg > , \n
  medium: < if laptop weight is between 1.51 kg and 2.51 kg> , \n
  high: < if laptop weight is less than 1.51 kg> \n


  Multitasking: low: < If the value of the RAM is 8GB or lower> , \n
  medium: < if the value of the RAM is between 8GB & 16GB > , \n
  high: < if the value of the RAM is more than 32GB> \n


  Processing Speed: low: < if entry-level processors like Intel Core i3, AMD Ryzen 3 > , \n
  medium: < if Mid-range processors like Intel Core i5, AMD Ryzen 5, M1 > , \n
  high: < if High-performance processors like M2, Intel Core i7, AMD Ryzen 7 or higher > \n
  {delimiter}


  {delimiter}
  Here are some input output pairs for few-shot learning:
  input1: "The Dell Inspiron is a versatile laptop that combines powerful performance and affordability. It features an Intel Core i5 processor clocked at 2.4 GHz, ensuring basic multitasking and efficient computing. With 8GB of RAM and an SSD, it offers quick data access and ample storage capacity. The laptop sports a vibrant 15.6" LCD display with a resolution of 1920x1080, delivering crisp visuals and immersive viewing experience. Weighing just 2.5 kg, it is decently portable. Additionally, it comes with an Intel UHD GPU for basic graphical performance and a backlit keyboard for enhanced typing convenience. With a one-year warranty and a battery life of up to 6 hours, the Dell Inspiron is a reliable companion for work or entertainment. "
  output1: {{'GPU intensity': 'medium','Display quality':'medium','Portability':'medium','Multitasking':'low','Processing speed':'medium'}}


  input2: "The Lenovo ThinkPad X1 Carbon is a sleek and lightweight laptop designed for professionals on the go. It is equipped with an Intel Core i7 processor running at 2.6 GHz, providing strong processing capabilities for productivity. With 16GB of RAM and an SSD, it offers decent multitasking performance along with ample storage capacity. The laptop features a 14" IPS display with a resolution of 2560x1440, delivering sharp visuals and accurate colors. It comes with Intel UHD integrated graphics for basic graphical performance. Weighing just 1.13 kg, it is extremely lightweight and highly portable. The laptop features an IR camera for face unlock, providing convenient and secure login options. With a three-year warranty and an impressive battery life of up to 12 hours, the Lenovo ThinkPad X1 Carbon ensures reliability and long-lasting productivity. "
  output2: {{'GPU intensity': 'low', 'Display quality': 'high', 'Portability': 'high', 'Multitasking':'medium', 'Processing speed':'high'}}


  input3: "The Apple MacBook Pro is a high-end laptop that combines top-tier performance with a stunning display. It is equipped with an M2 processor running at 2.9 GHz, providing exceptional processing power for demanding tasks and content creation. With 32GB of RAM and an SSD, it offers seamless multitasking and fast storage access for large projects. The laptop features a 16" Retina display with a resolution of 3072x1920, delivering breathtaking visuals and precise color reproduction. It comes with an Apple M2 dedicated graphics, ensuring smooth graphics performance for professional applications. Weighing 2.02 kg, it offers decent portability. The laptop features a True Tone display, adjusting the color temperature to match the ambient lighting for a more natural viewing experience. With a three-year warranty and a battery life of up to 10 hours, the Apple MacBook Pro offers reliability and endurance for professionals."
  output3: {{'GPU intensity': 'high', 'Display quality': 'high', 'Portability': 'medium','Multitasking': 'high', 'Processing speed': 'high'}}
  {delimiter}


  Follow the above instructions step-by-step and output the dictionary {lap_spec} for the following laptop {laptop_description}.
  """


#see that we are using the Completion endpoint and not the Chatcompletion endpoint


  response = OpenAI.chat.completions.create(
    model="gpt-3.5-turbo-1106",
    prompt=prompt,
    max_tokens = 2000,
    # temperature=0.3,
    # top_p=0.4
    )
  return response.choices[0].message.content

def compare_laptops_with_user(user_req_string):
    laptop_df= pd.read_csv('updated_laptop.csv')
    user_requirements = extract_dictionary_from_string(user_req_string)
    budget = int(user_requirements.get('budget', '0').replace(',', '').split()[0])
    #This line retrieves the value associated with the key 'budget' from the user_requirements dictionary.
    #If the key is not found, the default value '0' is used.
    #The value is then processed to remove commas, split it into a list of strings, and take the first element of the list.
    #Finally, the resulting value is converted to an integer and assigned to the variable budget.




    filtered_laptops = laptop_df.copy()
    filtered_laptops['Price'] = filtered_laptops['Price'].str.replace(',','').astype(int)
    filtered_laptops = filtered_laptops[filtered_laptops['Price'] <= budget].copy()
    #These lines create a copy of the laptop_df DataFrame and assign it to filtered_laptops.
    #They then modify the 'Price' column in filtered_laptops by removing commas and converting the values to integers.
    #Finally, they filter filtered_laptops to include only rows where the 'Price' is less than or equal to the budget.


    mappings = {
        'low': 0,
        'medium': 1,
        'high': 2
    }
    # Create 'Score' column in the DataFrame and initialize to 0
    filtered_laptops['Score'] = 0
    for index, row in filtered_laptops.iterrows():
        user_product_match_str = row['laptop_feature']
        laptop_values = extract_dictionary_from_string(user_product_match_str)
        score = 0


        for key, user_value in user_requirements.items():
            if key.lower() == 'budget':
                continue  # Skip budget comparison
            laptop_value = laptop_values.get(key, None)
            laptop_mapping = mappings.get(laptop_value.lower(), -1)
            user_mapping = mappings.get(user_value.lower(), -1)
            if laptop_mapping >= user_mapping:
                ### If the laptop value is greater than or equal to the user value the score is incremented by 1
                score += 1


        filtered_laptops.loc[index, 'Score'] = score


    # Sort the laptops by score in descending order and return the top 5 products
    top_laptops = filtered_laptops.drop('laptop_feature', axis=1)
    top_laptops = top_laptops.sort_values('Score', ascending=False).head(3)


    return top_laptops.to_json(orient='records')

def recommendation_validation(laptop_recommendation):
    data = json.loads(laptop_recommendation)
    data1 = []
    for i in range(len(data)):
        if data[i]['Score'] > 2:
            data1.append(data[i])


    return data1

if __name__ == '__main__':
    intent_confirmation_layer()