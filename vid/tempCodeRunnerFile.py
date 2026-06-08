
        'Department': [department],
        'Country': [country],
        'Center': [center]
    })

    # Encode with same columns as training
    sample_encoded = pd.get_dummies(sample, drop_first=True)
    sample_encoded = sample_encoded.reindex(columns=model_columns, fill_value=0)

    # Predict
    prediction = model.predict(sample_encoded)
    st.write(f"Salary prediction is $ {prediction[0]:.2f}")
else:
    st.write("Please press the button for app to make the prediction")
