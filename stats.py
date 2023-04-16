import streamlit as st
import numpy as np
import pandas as pd
from scipy.stats import skew, kurtosis

st.title("Statistical Analysis Application")

# Choose the type of data (ungrouped or grouped)
data_type = st.radio("Select the data type:",
                     ("Ungrouped Data", "Grouped Data"))

# Get data from the user
if data_type == "Grouped Data":
    input_lower_boundaries = st.text_input(
        "Enter the lower boundaries (comma-separated):")
    input_upper_boundaries = st.text_input(
        "Enter the upper boundaries (comma-separated):")
    input_frequencies = st.text_input(
        "Enter the frequencies (comma-separated, corresponding to the data):")
else:
    input_data = st.text_input("Enter your data (comma-separated):")

if data_type == "Grouped Data":
    if input_lower_boundaries and input_upper_boundaries and input_frequencies:
        try:
            lower_boundaries = np.array([float(x)
                                         for x in input_lower_boundaries.split(',')])
            upper_boundaries = np.array([float(x)
                                         for x in input_upper_boundaries.split(',')])
            frequencies = np.array([float(x)
                                   for x in input_frequencies.split(',')])

            # Calculate midpoints
            midpoints = (lower_boundaries + upper_boundaries) / 2

            # Calculate statistics for grouped data
            N = np.sum(frequencies)
            mean = np.sum(midpoints * frequencies) / N
            variance = np.sum((midpoints - mean)**2 * frequencies) / N

            # Display the results
            st.subheader("Results")
            st.write(f"Mean: {mean:.2f}")
            st.write(f"Variance: {variance:.2f}")

            # Step by step explanation for grouped data
            st.subheader("Step-by-step Explanation")
            st.write("Step 1: Calculate the midpoints of each class:")
            st.write("Midpoints: ", midpoints)
            st.write(
                "Step 2: Multiply each midpoint by its corresponding frequency:")
            st.write("Midpoints x Frequencies: ", (midpoints * frequencies))
            st.write("Step 3: Calculate the sum of the product from Step 2:")
            st.write("Sum of Midpoints x Frequencies: ",
                     np.sum(midpoints * frequencies))
            st.write(
                "Step 4: Divide the sum from Step 3 by the total number of observations (N):")
            st.write("Mean = (Sum of Midpoints x Frequencies) / N")
            st.write(f"Mean = {mean:.2f}")

            st.write(
                "Step 5: Calculate the squared deviation of each midpoint from the mean:")
            st.write("(Midpoints - Mean)^2: ", (midpoints - mean)**2)
            st.write(
                "Step 6: Multiply each squared deviation by its corresponding frequency:")
            st.write("(Midpoints - Mean)^2 x Frequencies: ",
                     (midpoints - mean)**2 * frequencies)
            st.write("Step 7: Calculate the sum of the product from Step 6:")
            st.write("Sum of (Midpoints - Mean)^2 x Frequencies: ",
                     np.sum((midpoints - mean)**2 * frequencies))
            st.write(
                "Step 8: Divide the sum from Step 7 by the total number of observations (N):")
            st.write("Variance = (Sum of (Midpoints - Mean)^2 x Frequencies) / N")
            st.write(f"Variance = {variance:.2f}")
        except ValueError:
            st.error(
                "Please make sure the input data is properly formatted (comma-separated numbers).")

        except Exception as e:
            st.error(f"An error occurred: {str(e)}")

elif input_data:
    try:
        values = [float(x) for x in input_data.split(',')]
        # Calculate statistics for ungrouped data
        mean = np.mean(values)
        variance = np.var(values)
        skewness = skew(values)
        kurt = kurtosis(values)
        # Display the results
        st.subheader("Results")
        st.write(f"Mean: {mean:.2f}")
        st.write(f"Variance: {variance:.2f}")
        st.write(f"Skewness: {skewness:.2f}")
        st.write(f"Kurtosis: {kurt:.2f}")

        # Step by step explanation for ungrouped data
        st.subheader("Step-by-step Explanation")
        st.write("Step 1: Calculate the sum of the data points:")
        st.write("Sum: ", np.sum(values))
        st.write(
            "Step 2: Divide the sum from Step 1 by the total number of data points (N):")
        st.write("Mean = Sum / N")
        st.write(f"Mean = {mean:.2f}")

        st.write(
            "Step 3: Calculate the squared deviation of each data point from the mean:")
        st.write("(Data - Mean)^2: ", (values - mean)**2)
        st.write(
            "Step 4: Calculate the sum of the squared deviations from Step 3:")
        st.write("Sum of (Data - Mean)^2: ", np.sum((values - mean)**2))
        st.write(
            "Step 5: Divide the sum from Step 4 by the total number of data points (N):")
        st.write("Variance = (Sum of (Data - Mean)^2) / N")
        st.write(f"Variance = {variance:.2f}")

    except ValueError:
        st.error(
            "Please make sure the input data is properly formatted (comma-separated numbers).")
    except Exception as e:
        st.error(f"An error occurred: {str(e)}")
