import streamlit as st
import time
import numpy as np
import requests
import streamlit.components.v1 as components

st.set_page_config(page_title="CPG Robo Agent Dossier Generator", page_icon="🗓️")

st.markdown("# Minion Researcher Agent")
st.write(
    """This demo illustrates the CPG Robo Assistant Dossier Creator, which takes several documents and creates a executive Dossier"""
)






last_rows = np.random.randn(1, 1)

with st.form(key='eval', clear_on_submit=True):
    #     uploaded_file = st.file_uploader(
    #         "Upload file", type=["pdf"],
    #         help="Only PDF files are supported",
    #         )
    topic_option = st.selectbox('Please Choose the Research Topic', ('New Product Research for Sunscreen' , 'Product Research for Sunscreen'))
    task_option = st.selectbox(
        'Please Choose the Task you want to Run',
        ('CPG Product Research', 'CPG Market Research'))
    # sub_section = st.multiselect('Select Documents for Research', SERIES.keys(), format_func=lambda y: SERIES[y],
    #                            help="Research Documents")


    submit_eval_button = st.form_submit_button(label='Perform My Task')

    if submit_eval_button and topic_option and task_option:

            # clear_submit()
        with st.spinner("Your Minion @ Work"):
            data = {'name': "Sample Run", 'topic': topic_option, 'userid': "arunneo", 'task_id': task_option}
            logs = """
            <!DOCTYPE html>
            <html>
            <head>
            <link href= 
'https://stackpath.bootstrapcdn.com/bootstrap/4.3.1/css/bootstrap.min.css'> 
  
    <script src= 
'https://stackpath.bootstrapcdn.com/bootstrap/4.3.1/js/bootstrap.bundle.min.js'> 
    </script> 
  
    <script src= 
'https://cdnjs.cloudflare.com/ajax/libs/jquery/3.2.1/jquery.min.js'> 
    </script> 
  
    <link rel="stylesheet" href="styles.css"> 
              <style>
              *{ 
    margin: 0; 
    padding: 0
} 
  
html { 
    height: 100%
} 
  
h2{ 
    color: #2F8D46; 
} 
#form { 
    text-align: center; 
    position: relative; 
    margin-top: 20px
} 
  
#form fieldset { 
    background: white; 
    border: 0 none; 
    border-radius: 0.5rem; 
    box-sizing: border-box; 
    width: 100%; 
    margin: 0; 
    padding-bottom: 20px; 
    position: relative
} 
  
.finish { 
    text-align: center
} 
  
#form fieldset:not(:first-of-type) { 
    display: none
} 
  
#form .previous-step, .next-step { 
    width: 100px; 
    font-weight: bold; 
    color: white; 
    border: 0 none; 
    border-radius: 0px; 
    cursor: pointer; 
    padding: 10px 5px; 
    margin: 10px 5px 10px 0px; 
    float: right
} 
  
.form, .previous-step { 
    background: #616161; 
} 
  
.form, .next-step { 
    background: #2F8D46; 
} 
  
#form .previous-step:hover, 
#form .previous-step:focus { 
    background-color: #000000
} 
  
#form .next-step:hover, 
#form .next-step:focus { 
    background-color: #2F8D46
} 
  
.text { 
    color: #2F8D46; 
    font-weight: normal
} 
  
#progressbar { 
    margin-bottom: 30px; 
    overflow: hidden; 
    color: lightgrey 
} 
  
#progressbar .active { 
    color: #2F8D46
} 
  
#progressbar li { 
    list-style-type: none; 
    font-size: 15px; 
    width: 25%; 
    float: left; 
    position: relative; 
    font-weight: 400
} 
  
#progressbar #step1:before { 
    content: "1"
} 
  
#progressbar #step2:before { 
    content: "2"
} 
  
#progressbar #step3:before { 
    content: "3"
} 
  
#progressbar #step4:before { 
    content: "4"
} 
  
#progressbar li:before { 
    width: 50px; 
    height: 50px; 
    line-height: 45px; 
    display: block; 
    font-size: 20px; 
    color: #ffffff; 
    background: lightgray; 
    border-radius: 50%; 
    margin: 0 auto 10px auto; 
    padding: 2px
} 
  
#progressbar li:after { 
    content: ''; 
    width: 100%; 
    height: 2px; 
    background: lightgray; 
    position: absolute; 
    left: 0; 
    top: 25px; 
    z-index: -1
} 
  
#progressbar li.active:before, 
#progressbar li.active:after { 
    background: #2F8D46
} 
  
.progress { 
    height: 20px
} 
  
.progress-bar { 
    background-color: #2F8D46
}
              #logs {
                background-color: black;
                color:white;
                height:600px;
                overflow-x: hidden;
                overflow-y: auto;
                text-align: left;
                padding-left:10px;
              }
              </style>
            </head>

            <body>
            
            <div class="container"> 
        <div class="row justify-content-center"> 
            <div class="col-11 col-sm-9 col-md-7  
                col-lg-6 col-xl-5 text-center p-0 mt-3 mb-2"> 
                <div class="px-0 pt-4 pb-0 mt-3 mb-3"> 
                    <form id="form"> 
                        <ul id="progressbar"> 
                            <li class="active" id="step1"> 
                                <strong>Generate Questions</strong> 
                            </li> 
                            <li id="step2"><strong>Search and Summarize VertexAI</strong></li> 
                            <li id="step3"><strong>Create Research Dossier</strong></li> 

                        </ul> 
                        <div class="progress"> 
                            <div class="progress-bar"></div> 
                        </div> <br> 
                        <fieldset> 
                            <h2>Now Generating Questions based on Research Topics</h2> 
                            <input type="button" name="next-step" 
                                class="next-step" value="Next Step" /> 
                        </fieldset> 
                        <fieldset> 
                            <h2>Now finding answers to the Questions using Vertex Search</h2> 
                            <input type="button" name="next-step" 
                                class="next-step" value="Next Step" /> 
                           
                        </fieldset> 
                        <fieldset> 
                            <h2>Collecting all factual data and Generating Dossier</h2> 
                            <input type="button" name="next-step" 
                                class="next-step" value="Next Step" /> 
                     </fieldset> 
                      <fieldset> 
                            <h2>Generate Top 5 Product Idea Concepts</h2> 
                            <input type="button" name="next-step" 
                                class="next-step" value="Final Step" /> 
                     </fieldset> 
                        
                    </form> 
                </div> 
            </div> 
        </div> 
         <h1>Server Logs:</h1>
            <div id="logs">
            </div>
    </div> 

           

            <script>
             var currentGfgStep, nextGfgStep; 
             var opacity; 
             var current = 1; 
             var steps = $("fieldset").length; 
             var source = new EventSource("http://localhost:8020/stream-logs");
             source.onmessage = function(event) {
                console.log(event.data)
                log = event.data
                document.getElementById("logs").innerHTML += event.data + "<br>";
                if(log.includes("ready to GenerateResearchQueries"))
                {
                 console.log("Inside Generate Search Queries");
                 
                 setProgressBar(1); 
                }
                
                else if(log.includes("ready to VertexSearchAndSummarize"))
                {
                
                  setProgressBar(2);
                }
                
                
            }
            
            function setProgressBar(currentStep) { 
                var percent = parseFloat(100 / steps) * current; 
                percent = percent.toFixed(); 
                $(".progress-bar") 
                    .css("width", percent + "%") 
    } 
                
              
              
            </script>

            """
            with st.expander("Minion Worker Logs"):
                components.html(logs, height=400, scrolling=True)

            data = requests.post("http://localhost:8010/agent/run", json=data).json()

        with st.expander("QnA"):
                with open(f"../data/research/{topic_option} QnA.md", "r") as f:
                    md_text = f.read()
                dossier = st.markdown(md_text)

        with st.expander("Dossier"):
            with open(f"../data/research/{topic_option}_Dossier.md", "r") as f:
                    md_text = f.read()
            dossier = st.markdown(md_text)

        with st.expander("Concept Development Document"):
            with open(f"../data/research/{topic_option}_ConceptDevelopment.md", "r") as f:
                    md_text = f.read()
            dossier = st.markdown(md_text)

    else:
        st.error("Please atleast choose one source to continue the research")



