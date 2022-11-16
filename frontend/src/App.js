import React from 'react';
import logo from './logo.svg';
import './App.css';
import AuthorList from './components/Author.js';
import ProjectList from './components/Project.js';

import axios from 'axios';

class App extends React.Component {
  constructor(props) {
    super(props)
    this.state = {
      'projects': []
    }
  }

  componentDidMount() {
    axios.get('http://127.0.0.1:8000/project/projects')
      .then(response => {
        const authors = response.data
        this.setState(
          {
            'projects': projects
          }
        )
      }).catch(error => console.log(error))
  }

  render() {
    return (
      <div>
        <ProjectList projects={this.state.projects} />
      </div>
    )
  }
}

export default App;


// class App extends React.Component {
//   constructor(props) {
//     super(props)
//     this.state = {
//       'authors': [],
//       'project': []
//     }
//   }

//   componentDidMount() {
//     axios.get('http://127.0.0.1:8000/api/authors')
//       .then(response => {
//         const authors = response.data
//         this.setState(
//           {
//             'authors': authors,
//             'project': project
//           }
//         )
//       }).catch(error => console.log(error))
//   }

//   render() {
//     return (
//       <div>
//         <AuthorList authors={this.state.authors} />
//       </div>
//     )
//   }
// }

// export default App;