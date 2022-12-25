import React from 'react';
import logo from './logo.svg';
import './App.css';
import AuthorList from './components/Author.js';
import ProjectList from './components/Project.js';

import axios from 'axios';
import { BrowserRouter, Route, Switch, Redirect, Link } from 'react-router-dom'

import { BrowserRouter, Route, Link, Switch, Redirect } from 'react-router-dom'

class App extends React.Component {
  constructor(props) {
    super(props)
    this.state = {
      'authorts': []
      // 'projects': []
    }
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
<<<<<<< HEAD
        <Route exact path='/books/create' component={() => <BookForm />} />
        <Route exact path='/books' component={() => <BookList items={this.state.books} deleteBook={(id) => this.deleteBook(id)} />} />
        <Route exact path='/books/create' component={() => <BookForm createBook={(name, author) => this.createBook(name, author)} />} />
=======
        <BrowserRouter>
          ...
        </BrowserRouter>
>>>>>>> 93783c285dd1ab35e4ccf852f2586c2b6daed28d
      </div>
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