from flask import Blueprint, request, jsonify
import pandas as pd

fertilizer_recommendation_bp = Blueprint('fertilizer_recommendation', __name__)

fertilizer_dic = {
    'NHigh': "The N value of soil is high and might give rise to weeds. "
             "Please consider the following suggestions:\n"
             "1. Manure – adding manure is one of the simplest ways to amend your soil with nitrogen. "
             "Be careful as there are various types of manures with varying degrees of nitrogen.\n"
             "2. Coffee grinds – use your morning addiction to feed your gardening habit! Coffee grinds are considered "
             "a green compost material which is rich in nitrogen. Once the grounds break down, your soil will be fed "
             "with delicious nitrogen. An added benefit to including coffee grounds to your soil is while it will compost, "
             "it will also help provide increased drainage to your soil.\n"
             "3. Plant nitrogen fixing plants – planting vegetables that are in Fabaceae family like peas, beans, and soybeans "
             "have the ability to increase nitrogen in your soil.\n"
             "4. Plant ‘green manure’ crops like cabbage, corn, and broccoli.\n"
             "5. Use mulch (wet grass) while growing crops – Mulch can also include sawdust and scrap soft woods.",

    'Nlow': "The N value of your soil is low. Please consider the following suggestions:\n"
            "1. Add sawdust or fine woodchips to your soil – the carbon in the sawdust/woodchips love nitrogen and will help "
            "absorb and soak up any excess nitrogen.\n"
            "2. Plant heavy nitrogen feeding plants – tomatoes, corn, broccoli, cabbage, and spinach are examples of plants "
            "that thrive off nitrogen and will suck the nitrogen dry.\n"
            "3. Water – soaking your soil with water will help leach the nitrogen deeper into your soil, effectively leaving "
            "less for your plants to use.\n"
            "4. Sugar – In limited studies, it was shown that adding sugar to your soil can help potentially reduce the amount "
            "of nitrogen in your soil. Sugar is partially composed of carbon, an element which attracts and soaks up the nitrogen "
            "in the soil. This is a similar concept to adding sawdust/woodchips which are high in carbon content.\n"
            "5. Add composted manure to the soil.\n"
            "6. Plant Nitrogen fixing plants like peas or beans.\n"
            "7. Use NPK fertilizers with high N value.\n"
            "8. Do nothing – It may seem counter-intuitive, but if you already have plants that are producing lots of foliage, "
            "it may be best to let them continue to absorb all the nitrogen to amend the soil for your next crops.",

    'PHigh': "The P value of your soil is high. Please consider the following suggestions:\n"
             "1. Avoid adding manure – manure contains many key nutrients for your soil but typically including high levels of phosphorous. "
             "Limiting the addition of manure will help reduce phosphorus being added.\n"
             "2. Use only phosphorus-free fertilizer – if you can limit the amount of phosphorous added to your soil, you can let the plants "
             "use the existing phosphorus while still providing other key nutrients such as Nitrogen and Potassium. Find a fertilizer with "
             "numbers such as 10-0-10, where the zero represents no phosphorous.\n"
             "3. Water your soil – soaking your soil liberally will aid in driving phosphorous out of the soil. This is recommended as a last ditch effort.\n"
             "4. Plant nitrogen fixing vegetables to increase nitrogen without increasing phosphorous (like beans and peas).\n"
             "5. Use crop rotations to decrease high phosphorous levels.",

    'Plow': "The P value of your soil is low. Please consider the following suggestions:\n"
            "1. Bone meal – a fast acting source that is made from ground animal bones which is rich in phosphorous.\n"
            "2. Rock phosphate – a slower acting source where the soil needs to convert the rock phosphate into phosphorous that the plants can use.\n"
            "3. Phosphorus Fertilizers – applying a fertilizer with a high phosphorous content in the NPK ratio (example: 10-20-10, 20 being phosphorous percentage).\n"
            "4. Organic compost – adding quality organic compost to your soil will help increase phosphorous content.\n"
            "5. Manure – as with compost, manure can be an excellent source of phosphorous for your plants.\n"
            "6. Clay soil – introducing clay particles into your soil can help retain & fix phosphorus deficiencies.\n"
            "7. Ensure proper soil pH – having a pH in the 6.0 to 7.0 range has been scientifically proven to have the optimal phosphorus uptake in plants.\n"
            "8. If soil pH is low, add lime or potassium carbonate to the soil as fertilizers. Pure calcium carbonate is very effective in increasing the pH value of the soil.\n"
            "9. If pH is high, the addition of an appreciable amount of organic matter will help acidify the soil. Application of acidifying fertilizers, such as ammonium sulfate, can help lower soil pH.",

    'KHigh': "The K value of your soil is high. Please consider the following suggestions:\n"
             "1. Loosen the soil deeply with a shovel, and water thoroughly to dissolve water-soluble potassium. Allow the soil to fully dry, and repeat digging and watering the soil two or three more times.\n"
             "2. Sift through the soil, and remove as many rocks as possible, using a soil sifter. Minerals occurring in rocks such as mica and feldspar slowly release potassium into the soil through weathering.\n"
             "3. Stop applying potassium-rich commercial fertilizer. Apply only commercial fertilizer that has a '0' in the final number field. Commercial fertilizers use a three number system for measuring levels of nitrogen, phosphorous, and potassium. The last number stands for potassium. Another option is to stop using commercial fertilizers altogether and to begin using only organic matter to enrich the soil.\n"
             "4. Mix crushed eggshells, crushed seashells, wood ash, or soft rock phosphate to the soil to add calcium. Mix in up to 10 percent of organic compost to help amend and balance the soil.\n"
             "5. Use NPK fertilizers with low K levels and organic fertilizers since they have low NPK values.\n"
             "6. Grow a cover crop of legumes that will fix nitrogen in the soil. This practice will meet the soil’s needs for nitrogen without increasing phosphorus or potassium.",

    'Klow': "The K value of your soil is low. Please consider the following suggestions:\n"
            "1. Mix in muricate of potash or sulphate of potash.\n"
            "2. Try kelp meal or seaweed.\n"
            "3. Try Sul-Po-Mag.\n"
            "4. Bury banana peels an inch below the soil's surface.\n"
            "5. Use Potash fertilizers since they contain high values of potassium."
}

@fertilizer_recommendation_bp.route('/fertilizer-predict', methods=['POST'])
def fert_recommend():
    data = request.json
    crop_name = data.get('cropname')
    N = int(data.get('nitrogen'))
    P = int(data.get('phosphorous'))
    K = int(data.get('pottasium'))

    df = pd.read_csv('routes/Data/fertilizer.csv')

    nr = df[df['Crop'] == crop_name]['N'].iloc[0]
    pr = df[df['Crop'] == crop_name]['P'].iloc[0]
    kr = df[df['Crop'] == crop_name]['K'].iloc[0]

    n = nr - N
    p = pr - P
    k = kr - K
    temp = {abs(n): "N", abs(p): "P", abs(k): "K"}
    max_value = temp[max(temp.keys())]

    if max_value == "N":
        if n < 0:
            key = 'NHigh'
        else:
            key = "Nlow"
    elif max_value == "P":
        if p < 0:
            key = 'PHigh'
        else:
            key = "Plow"
    else:
        if k < 0:
            key = 'KHigh'
        else:
            key = "Klow"

    response = fertilizer_dic[key]

    return jsonify({'recommendation': response})