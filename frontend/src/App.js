import React from 'react';
import logo from './logo.svg';
import './App.css';
import AuthorList from './components/Author.js';
import ProjectList from './components/Project.js';
import LoginForm from './components/Auth.js'
import { BrowserRouter, Route, Switch, Redirect, Link } from 'react-router-dom'

import axios from 'axios';
import Cookies from 'universal-cookie';

const NotFound404 = ({ location }) => {
  return (
    <div>
      <h1>Страница по адресу '{location.pathname}' не найдена</h1>
    </div>
  )
}

import { BrowserRouter, Route, Link, Switch, Redirect } from 'react-router-dom'

class App extends React.Component {
  constructor(props) {
    super(props)
    this.state = {
      'projects': [],
      'token': ''
    }
  }

  set_token(token) {
    const cookies = new Cookies()
    cookies.set('token', token)
    this.setState({ 'token': token })
  }

  is_authenticated() {
    return this.state.token != ''
  }
  logout() {
    this.set_token('')
  }

  get_token_from_storage() {
    const cookies = new Cookies()
    const token = cookies.get('token')
    this.setState({ 'token': token })
  }

  get_token(username, password) {
    axios.post('http://127.0.0.1:8000/api-token-auth/', {
      username: username,
      password: password
    })
      .then(response => {
        this.set_token(response.data['token'])
      }).catch(error => alert('Неверный логин или пароль'))
  }

  load_data() {
    axios.get('http://127.0.0.1:8000/api/projects/')
      .then(response => {
        this.setState({ authors: response.data })
      }).catch(error => console.log(error))
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
        <li>
          <Link to='/login'>Login</Link>
        </li>

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