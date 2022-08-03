import streamlit as st
import pickle
from datetime import datetime

# date_string = "21 June, 2018"
# print("date_string =", date_string)

# date_object = datetime.strptime(date_string, "%d %B, %Y")
# print("date_object =", date_object)

st.title("Flight Price Prediction")
# st.subheader("Predict survival on the Titanic and get familiar with ML basics")

app_mode = st.selectbox("select Titanic dataset mode",["Home","Classification"])

# if app_mode == "Home":
#     data = pd.read_csv("train.csv")
#     st.image("./images/titanic2.jpg")
#     st.markdown("Train Dataset Example Of Titanic Dataset")
#     st.write(data)
#     st.markdown("Description of Numerical Dataset")
#     st.write(data.describe())


if app_mode == "Classification":
    st.title("..")
    # gender_data = {"male":0 ,"female":1}
    # pclass = [1,2,3]
    # Embarked = {"Cherbourg" : 0, "Queenstown": 1, "Southampton":2}

    airline_data = ['IndiGo', 'Air India', 'Jet Airways', 'SpiceJet',
       'Multiple carriers', 'GoAir', 'Vistara', 'Air Asia',
       'Vistara Premium economy', 'Jet Airways Business',
       'Multiple carriers Premium economy', 'Trujet']

    sourve_data = ['Banglore', 'Kolkata', 'Delhi', 'Chennai', 'Mumbai']

    destination_data = ['New Delhi', 'Banglore', 'Cochin', 'Kolkata', 'Delhi', 'Hyderabad']

    airline = st.sidebar.selectbox("Select Airline TO travel",airline_data)
    IndiGo,Air_India,Jet_Airways,SpiceJet,Multiple_carriers,GoAir,Vistara,Air_Asia,Vistara_Premium_economy,Jet_Airways_Business,Multiple_carriers_Premium_economy, Trujet= 0,0,0,0,0,0,0,0,0,0,0,0

    if airline == "IndiGo":
        IndiGo = 1
    elif airline == "Air India":
        Air_India = 1
    elif airline == "Jet Airways":
        Jet_Airways = 1
    elif airline == "SpiceJet":
        SpiceJet = 1
    elif airline == "Multiple carriers":
        Multiple_carriers = 1
    elif airline == "GoAir":
        GoAir = 1
    elif airline == "Vistara":
        Vistara = 1
    elif airline == "Air Asia":
        Air_Asia = 1
    elif airline == "Vistara Premium economy":
        Vistara_Premium_economy = 1
    elif airline == "Multiple carriers Premium economy":
        Multiple_carriers_Premium_economy = 1
    elif airline == "Trujet":
        Trujet = 1
    elif airline == "Jet Airways Business":
        Jet_Airways_Business = 1


    date_journey = st.sidebar.date_input("Date of Journey")
    journey_day = date_journey.day
    journey_month = date_journey.month

    dep_time = st.sidebar.time_input("Department time")
    dep_hour = dep_time.hour
    dep_min = dep_time.minute

    arrival_time = st.sidebar.time_input("arrival time")
    arrival_hour = arrival_time.hour
    arrival_min = arrival_time.minute

    source = st.sidebar.selectbox("Select source TO travel", sourve_data)
    destination_New_Delhi,destination_Banglore,destination_Cochin,destination_Kolkata,destination_Delhi,destination_Hyderabad = 0,0,0,0,0,0
    if source == "New Delhi":
        destination_New_Delhi = 1
    elif source == "Banglore":
        destination_Banglore = 1
    elif source == "Cochin":
        destination_Cochin = 1
    elif source == "Kolkata":
        destination_Kolkata = 1
    elif source == "Delhi":
        destination_Delhi = 1
    elif source == "Hyderabad":
        destination_Hyderabad = 1


    destination = st.sidebar.selectbox("Select destination TO travel", destination_data)
    source_Banglore, source_Kolkata, source_Delhi, source_Chennai, source_Mumbai = 0, 0, 0, 0, 0
    if source == "Banglore":
        source_Banglore = 1
    elif source == "Kolkata":
        source_Kolkata = 1
    elif source == "Delhi":
        source_Delhi = 1
    elif source == "Chennai":
        source_Chennai = 1
    elif source == "Mumbai":
        source_Mumbai = 1


    total_stop = st.sidebar.number_input("Enter Stop",0,10)

    col1,col2 = st.sidebar.columns(2)
    duration_hour = col1.number_input("hour",value = 0)
    duration_min = col2.number_input("min",0,60)

    if st.sidebar.button("Predict"):
        st.write("clicked")
        model = pickle.load(open("flight_rf.pkl", "rb"))

        st.write(
            {
                "total_stop": total_stop,
                "date_journey": date_journey,
                "journey_day": journey_day,
                "journey_month": journey_month,
                "dep_time": dep_time,
                "dep_hour": dep_hour,
                "dep_min": dep_min,
                "arrival_time": arrival_time,
                "arrival_hour": arrival_hour,
                "arrival_min": arrival_min,
                "duration_hour": duration_hour,
                "duration_min": duration_min,

            }
        )
        Y = model.predict([[total_stop, journey_day, journey_month, dep_hour, dep_min, arrival_hour, arrival_min,
                            duration_hour, duration_min, Air_India, GoAir, IndiGo, Jet_Airways, Jet_Airways_Business,
                            Multiple_carriers, Multiple_carriers_Premium_economy, SpiceJet, Vistara,
                            Vistara_Premium_economy, Trujet, source_Chennai, source_Delhi, source_Kolkata,
                            source_Mumbai, destination_Cochin, destination_Delhi, destination_Hyderabad,
                            destination_Kolkata, destination_New_Delhi]])[0]
        st.write(Y)
    st.sidebar.write("               ")
    st.sidebar.write("               ")
    st.sidebar.write("               ")


    # st.write(date.day)
    # st.sidebar.number_input("Enter Age Value:",0,100)
    # st.sidebar.radio("Select Your Gender",gender_data)
    # st.sidebar.radio("Select Pclass",pclass)
    # st.sidebar.selectbox("Select Embarked",tuple(Embarked.keys()))
    # st.sidebar.number_input("Enter Fare Value:")
    #
    # model = pickle.load(open("Titanic.pkl", "rb"))
    # Y = model.predict([[3,0,0,1,0,1,0]])[0]
    # Y = 1
    # col1,col2,col3 = st.columns(3)
    #
    # with col2:
    #     if Y == 0:
    #         st.image("./images/not.gif")
    #     elif Y == 1:
    #         st.image("./images/yes.gif")

#
# st.title("titanic data")
# pclass = st.selectbox('selecr class',[1,2,3])
#
# number = st.number_input("number enter",0,1)
#
# m =  st.number_input("male,female",0,1)
#
# gender = st.radio("gender select",tuple({"male":0,"female":1}.keys()))
#
# emb  = st.number_input("embark",0,2)
#
# set_background("data:image/jpeg;base64,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")
# class_0 , class_3 , class_1,class_2 = 0,0,0,0
# if emb == 0:
#     class_0 = 1
# elif emb == 1:
#     class_1 = 1
# elif emb == 2 :
#     class_2 = 1
#
# male ,female  = 0,0
# if m == 0:
#     male = 1
# elif m == 1:
#     female = 1
#
#
# if st.button("predict"):
#     st.write({
#         "Pclass" : pclass,
#         "Parch" : number,
#         "Sex_female" : male,
#         "Sex_male" : female,
#         "Embarked_C" : class_0,
#         "Embarked_Q" : class_1 ,
#         "Embarked_S" : class_2,
#         "gender":gender
#     });
#     model = pickle.load(open("Titanic.pkl","rb"))
#     st.write(model.predict([[pclass,number,male,female,class_1,class_2,class_3]]))

