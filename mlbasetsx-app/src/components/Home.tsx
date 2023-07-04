import React, { ChangeEvent, useState } from "react";
import { useForm } from "react-hook-form";

function Home() {

  const { register, handleSubmit } = useForm();
  const [file, setFile] = useState<any>();
  const [outcome, setOutcome] = useState<any>();
  const [process, setProcess] = useState<Boolean>(false);

  const onSubmit = async (data: any) => {
    const formData = new FormData();
    formData.append("file", data.file[0]);

    const res = await fetch("http://localhost:5050/uploader", {
        method: "POST",
        body: formData,
    }).then((res) => res.json());
    setFile(res.filename);
    alert(JSON.stringify(`${res.status}, status: ${res.filename}`));
};

const onFileInputChange = (e: React.ChangeEvent<HTMLInputElement>) => {
  console.log(e.target.files);
};


const processFile = async (e: React.MouseEvent<HTMLButtonElement>) => {

  const res = await fetch("http://localhost:5050/process", {
    method: "POST",
    body: file,
    }).then((res) => res.json());
    setOutcome(res.outcome);
    if(res.success){
      setProcess(true)
    }
    alert(JSON.stringify(`${res.status}, status: ${res.message}`));
};

  return (
    <div className="home">
      <div className="container">
        <div className="row align-items-center my-5">
          <div className="col-lg-7">
          <label className="form-label" htmlFor="customFile">Default file input example</label>
          <form onSubmit={handleSubmit(onSubmit)}>
            <div className="input-group mb-3">
              <input type="file" className="form-control" id="customFile" {...register("file")} />
              <button className="btn btn-outline-primary" 
                id="button-addon2" 
                data-mdb-ripple-color="dark"
                type="submit"> Submit </button>
            </div>
          </form>
          </div>
        </div>

        <div className="row align-items-center my-5">
        <div className="col-lg-7">
        {(file && file.trim() !== '') &&
          <div>
            <div  className="form-label" >{file}</div>
            <div><p>To Process File Click here</p></div>
            <button className="btn btn-success" onClick={processFile}>Process File</button>
          </div>
        }
        </div>
        </div>

        <div className="row align-items-center my-5">
        <div className="col-lg-7">
        {(process) &&
          <div>
            <div><p> {file} Processed Success Full</p></div>
            <div><p> ML Model OutCome :  {outcome}</p></div>
          </div>
        }
        </div>
        </div>
      </div>
    </div>
  );
}

export default Home;