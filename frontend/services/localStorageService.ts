import { type Note } from '~/types/note';

const save = (key: string, value: Note) => {
  try {
    const serializedValue = JSON.stringify(value);
    localStorage.setItem(key, serializedValue);
  } catch (error) {
    console.error(`Error saving to localStorage with key "${key}":`, error);
  }
}

const loadAll = () => {
  try {
    const keys = Object.keys(localStorage);
    const items: Record<string, any> = {};
    keys.forEach((key) => {
      const value = localStorage.getItem(key);
      if (value !== null) {
        items[key] = JSON.parse(value);
      }
    });
    return items;
  } catch (error) {
    console.error('Error loading all from localStorage:', error);
    return {};
  }
}

const load = (key: string) => {
  try {
    const serializedValue = localStorage.getItem(key);
    if (serializedValue === null) {
      return undefined;
    }
    return JSON.parse(serializedValue);
  } catch (error) {
    console.error(`Error loading from localStorage with key "${key}":`, error);
    return undefined;
  }
}
const remove = (key: string) => {
  try {
    localStorage.removeItem(key);
  } catch (error) {
    console.error(`Error removing from localStorage with key "${key}":`, error);
  }
}
const clear = () => {
  try {
    localStorage.clear();
  } catch (error) {
    console.error('Error clearing localStorage:', error);
  }
}

export default {
  save,
  load,
  loadAll,
  remove,
  clear,
}