 Plotting
sns.set(style="darkgrid")

# Linear Regression Plot
plt.figure(figsize=(8, 6))
sns.scatterplot(x=column1, y=column2, data=df)
plt.plot(df[column1], linear_model.predict(df[[column1]]), color='red')
plt.title('Linear Regression')
plt.xlabel(column1)
plt.ylabel(column2)
plt.show()

# Logistic Regression Plot
plt.figure(figsize=(8, 6))
sns.scatterplot(x=column1, y=column2, data=df)
sns.lineplot(x=df[column1], y=logistic_model.predict_proba(df[[column1]])[:, 1], color='red')
plt.title('Logistic Regression')
plt.xlabel(column1)
plt.ylabel(column2)
plt.show()

# Print the coefficients
print('Linear Regression Coefficient:', linear_model.coef_[0])
print('Logistic Regression Coefficients:', logistic_model.coef_[0])