import { useState } from "react";

const FormInput = (props) => {
  const name = props.name;
  const value = props.value;
  const type = props.type;
  const eventHandler = props.eventHandler;
  const additionalStyles = props.style;

  let style = {
    margin: "10px 10px",
  };

  if (additionalStyles) {
    style = { ...style, ...additionalStyles };
  }

  return (
    <div style={style}>
      <p>{name}</p>
      <input
        value={value}
        onChange={eventHandler}
        type={type ? type : "text"}
      />
    </div>
  );
};

function App() {
  const [firstName, setFirstName] = useState("");
  const [lastName, setLastName] = useState("");
  const [email, setEmail] = useState("");
  const [password, setPassword] = useState("");
  const [confirmPassword, setConfirmPassword] = useState("");

  const handleFirstNameChange = (event) => {
    console.log("First name is:", event.target.value);

    setFirstName(event.target.value);
  };

  const handleLastNameChange = (event) => {
    console.log("Last name is:", event.target.value);

    setLastName(event.target.value);
  };

  const handleEmailChange = (event) => {
    console.log("Email is:", event.target.value);

    setEmail(event.target.value);
  };

  const handlePasswordChange = (event) => {
    console.log("Password is:", event.target.value);
    setPassword(event.target.value);
  };

  const handleConfirmPasswordChange = (event) => {
    console.log("Confirm Password is:", event.target.value);

    setConfirmPassword(event.target.value);
  };

  const addCustomer = (event) => {
    event.preventDefault();

    if (password !== confirmPassword) {
      // TODO: Add a better way to display errors
      alert("Passwords do not match");
    }

    console.log("button click", event.target);
  };

  const nameStyle = {
    display: "flex",
  };

  const containerStyle = {
    display: "flex",
    justifyContent: "center",
    alignItems: "center",
  };

  return (
    <>
      <div style={containerStyle}>
        <form onSubmit={addCustomer}>
          <div style={nameStyle}>
            <FormInput
              name="First Name"
              value={firstName}
              eventHandler={handleFirstNameChange}
            />

            <FormInput
              name="Last Name"
              value={lastName}
              eventHandler={handleLastNameChange}
            />
          </div>

          <FormInput
            name="Email"
            type="email"
            value={email}
            eventHandler={handleEmailChange}
            style={containerStyle}
          />

          <FormInput
            name="Password"
            type="password"
            value={password}
            eventHandler={handlePasswordChange}
            style={containerStyle}
          />

          <FormInput
            name="Confirm Password"
            type="password"
            value={confirmPassword}
            eventHandler={handleConfirmPasswordChange}
            style={containerStyle}
          />

          <div style={containerStyle}>
            <button type="submit">Submit</button>
          </div>
        </form>
      </div>
    </>
  );
}

export default App;
