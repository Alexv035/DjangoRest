import React from 'react';
import logo from './logo.svg';
import './App.css';
import AuthorList from './components/Author.js';
import ProjectList from './components/Project.js';
import LoginForm from './components/Auth.js'
import { BrowserRouter, Route, Switch, Redirect, Link } from 'react-router-dom'

import axios from 'axios';

import { BrowserRouter, Route, Switch, Redirect, Link } from 'react-router-dom'
import Cookies from 'universal-cookie';

const NotFound404 = ({ location }) => {
  return (
    <div>
      <h1>Страница по адресу '{location.pathname}' не найдена</h1>
    </div>
  )
}


class App extends React.Component {
  constructor(props) {
    super(props)
    this.state = {
      'authorts': [],
      // 'projects': []
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
    axios.get('http://127.0.0.1:8000/api/authors')
      .then(response => {
        const authors = response.data
        this.setState(
          {
            'authors': authors,
            'project': project
          }
        )
      }).catch(error => console.log(error))
  }

  render() {
    return (

      <div className="App">

        <Route exact path='/books/create' component={() => <BookForm />} />
        <Route exact path='/books' component={() => <BookList items={this.state.books} deleteBook={(id) => this.deleteBook(id)} />} />
        <Route exact path='/books/create' component={() => <BookForm createBook={(name, author) => this.createBook(name, author)} />} />


        <ProjectList projects={this.state.projects} />
        <li>
          <Link to='/login'>Login</Link>
        </li>

      </div >
    )
  }

  deleteBook(id) {
    const headers = this.get_headers()
    axios.delete(`http://127.0.0.1:8000/api/books/${id}`, { headers, headers })
      .then(response => {
        this.setState({
          books: this.state.books.filter((item) => item.id !==
            id)
        })
      }).catch(error => console.log(error))
  }

  createBook(name, author) {
    const headers = this.get_headers()
    const data = { name: name, author: author }
    axios.post(`http://127.0.0.1:8000/api/books/`, data, { headers, headers })
      .then(response => {
        let new_book = response.data
        const author = this.state.authors.filter((item) => item.id ===
          new_book.author)[0]
        new_book.author = author
        this.setState({ books: [...this.state.books, new_book] })
      }).catch(error => console.log(error))
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


// axios.get('http://127.0.0.1:8000/project/projects')
// .then(response => {
//     const authors = response.data
//   this.setState(
//   {
//     'projects': projects
//   }
// )
// }).catch (error => console.log(error))
// }

// render() {
//   return (
//     <div>
//       <ProjectList projects={this.state.projects} />
//     </div>
//   )
// }