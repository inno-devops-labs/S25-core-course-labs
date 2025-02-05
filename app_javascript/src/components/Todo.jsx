import React from 'react';
import { Check, Trash2 } from 'lucide-react';

const Todo = ({ todo, onToggle, onDelete }) => {
  return (
    <li 
      className="flex items-center justify-between p-3 bg-white border rounded shadow-sm hover:shadow-md transition-shadow" 
      data-testid="todo-item"
    >
      <div className="flex items-center gap-3">
        <button 
          onClick={() => onToggle(todo.id)}
          className={`p-1 rounded-full transition-colors ${
            todo.completed ? 'bg-green-500' : 'border hover:bg-gray-100'
          }`}
          data-testid="toggle-button"
        >
          {todo.completed && <Check size={16} className="text-white" />}
        </button>
        <span className={`${
          todo.completed ? 'line-through text-gray-500' : 'text-gray-900'
        } transition-colors`}>
          {todo.text}
        </span>
      </div>
      <button 
        onClick={() => onDelete(todo.id)}
        className="text-red-500 hover:text-red-600 transition-colors"
        data-testid="delete-button"
      >
        <Trash2 size={20} />
      </button>
    </li>
  );
};

export default Todo;