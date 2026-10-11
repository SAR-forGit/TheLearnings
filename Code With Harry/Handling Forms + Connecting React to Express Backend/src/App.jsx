import { useState } from 'react'
import './App.css'
import { useForm } from 'react-hook-form';

function App() {
  const {
    register,
    handleSubmit,
    watch,
    formState: { errors, isSubmitting },
    setError,
  } = useForm();

  // This Function is for only to stimulate backend delay
  // const delay = (delayTime) => {
  //   return new Promise((resolve, reject) => {
  //     setTimeout(() => {
  //       resolve();
  //     }, delayTime * 1000);
  //   })
  // }

  const onSubmit = async (data) => {
    let r = await fetch("http://localhost:3000/", {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify(data)
    });
    let res = await r.text();
    console.log(data, res);

    // await delay(2) // Was only to stimulate the backend
    // console.log(data);
    // if (data.username == '@' || data.username == ".com") { // Was only to stimulate the backend
    //   setError("myForm", {message: "Your Form is not in good order because credentials are invalid"}) // Was only to stimulate the backend
    // }
  }

  return (
    <>

      <div className="container">
        <form action="" onSubmit={handleSubmit(onSubmit)}>

          <input placeholder='username' {...register("username", { required: { value: true, message: "The username is required" }, minLength: { value: 3, message: "Min length is 3" }, maxLength: { value: 30, message: "Max length is 8" } })} type="text" />
          {errors.username && <div className='errorMessage'>{errors.username.message}</div>}
          <input {...register("password")} placeholder='password' type="password" />

          {isSubmitting ? <div>Loading</div> : <div>
            <input disabled={isSubmitting} type="submit" value="Submit" />
          </div>}

          {errors.myForm && <div className='red'>{errors.myForm.message}</div>}
        </form>
      </div>
    </>
  )
}

export default App
