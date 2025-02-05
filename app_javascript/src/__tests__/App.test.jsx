import { render, screen, fireEvent } from '@testing-library/react'
import userEvent from '@testing-library/user-event'
import App from '../App'

describe('Todo App', () => {
  beforeEach(() => {
    localStorage.clear()
  })

  test('adds new todo', async () => {
    render(<App />)
    const input = screen.getByTestId('todo-input')
    const button = screen.getByTestId('add-button')
    
    await userEvent.type(input, 'New Todo')
    await userEvent.click(button)
    
    expect(screen.getByText('New Todo')).toBeInTheDocument()
  })

  test('toggles todo completion', async () => {
    render(<App />)
    const input = screen.getByTestId('todo-input')
    const button = screen.getByTestId('add-button')
    
    await userEvent.type(input, 'Test Todo')
    await userEvent.click(button)
    
    const toggleButton = screen.getByTestId('toggle-button')
    await userEvent.click(toggleButton)
    
    expect(toggleButton).toHaveClass('bg-green-500')
  })

  test('deletes todo', async () => {
    render(<App />)
    const input = screen.getByTestId('todo-input')
    const button = screen.getByTestId('add-button')
    
    await userEvent.type(input, 'Delete Me')
    await userEvent.click(button)
    
    const deleteButton = screen.getByTestId('delete-button')
    await userEvent.click(deleteButton)
    
    expect(screen.queryByText('Delete Me')).not.toBeInTheDocument()
  })

  test('persists todos in localStorage', async () => {
    render(<App />)
    const input = screen.getByTestId('todo-input')
    const button = screen.getByTestId('add-button')
    
    await userEvent.type(input, 'Persistent Todo')
    await userEvent.click(button)
    
    // Re-render app
    render(<App />)
    
    expect(screen.getByText('Persistent Todo')).toBeInTheDocument()
  })
})