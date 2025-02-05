import { useState, useEffect } from 'react'
import { Plus } from 'lucide-react'
import Todo from './components/Todo'

function App() {
  const [todos, setTodos] = useState(() => {
    const savedTodos = localStorage.getItem('todos')
    return savedTodos ? JSON.parse(savedTodos) : []
  })
  const [newTodo, setNewTodo] = useState('')

  useEffect(() => {
    localStorage.setItem('todos', JSON.stringify(todos))
  }, [todos])

  const addTodo = () => {
    if (newTodo.trim()) {
      const newTodos = [...todos, { 
        id: Date.now(), 
        text: newTodo, 
        completed: false 
      }]
      setTodos(newTodos)
      setNewTodo('')
    }
  }

  const toggleTodo = (id) => {
    const newTodos = todos.map(todo => 
      todo.id === id ? { ...todo, completed: !todo.completed } : todo
    )
    setTodos(newTodos)
  }

  const deleteTodo = (id) => {
    const newTodos = todos.filter(todo => todo.id !== id)
    setTodos(newTodos)
  }

  return (
    <div className="max-w-lg mx-auto p-6">
      <h1 className="text-3xl font-bold mb-6">Todo List</h1>
      
      <div className="flex gap-2 mb-6">
        <input
          type="text"
          value={newTodo}
          onChange={(e) => setNewTodo(e.target.value)}
          onKeyDown={(e) => e.key === 'Enter' && addTodo()}
          placeholder="Add new todo..."
          className="flex-1 p-2 border rounded"
          data-testid="todo-input"
        />
        <button 
          onClick={addTodo}
          className="bg-blue-500 text-white p-2 rounded hover:bg-blue-600"
          data-testid="add-button"
        >
          <Plus size={24} />
        </button>
      </div>

      <ul className="space-y-2">
        {todos.map(todo => (
          <Todo 
            key={todo.id}
            todo={todo}
            onToggle={toggleTodo}
            onDelete={deleteTodo}
          />
        ))}
      </ul>
    </div>
  )
}

export default App