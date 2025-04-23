<template>
  <div class="min-h-screen flex flex-col relative px-4 md:px-0">
    <div class="w-full max-w-4xl mx-auto flex-grow pt-24">
      <h1 class="text-2xl font-medium mb-8 text-black/90">Minhas Notas</h1>
      
      <!-- Lista de notas -->
      <div v-if="!notes.length" class="text-sm text-black/60">
        Nenhuma nota criada ainda
      </div>

      <!-- Grid de notas -->
      <div class="grid grid-cols-1 md:grid-cols-2 gap-4">
        <div
          v-for="note in notes"
          :key="note.id"
          class="group relative bg-white rounded-xl border border-black/10 hover:border-black/20 shadow-sm hover:shadow transition-all duration-200 overflow-hidden"
          @click="openNote(note)"
        >
          <!-- Conteúdo do card -->
          <div class="p-5">
            <!-- Cabeçalho -->
            <div class="mb-3">
              <div class="text-xs text-black/50">
                Atualizada {{ formatRelativeTime(note.createdAt) }}
              </div>
            </div>

            <!-- Preview do conteúdo -->
            <div 
              class="text-sm text-black/70 whitespace-pre-line line-clamp-4 leading-relaxed"
              :class="{'font-mono text-xs': isCode(note.content)}"
            >
              {{ note.content || 'Sem conteúdo' }}
            </div>

            <!-- Overlay de hover -->
            <div class="absolute inset-0 bg-black/[0.02] opacity-0 group-hover:opacity-100 transition-opacity" />
          </div>

          <!-- Borda inferior decorativa -->
          <div 
            class="h-1 w-full bg-gradient-to-r from-black/5 via-black/10 to-black/5 transform origin-left scale-x-0 group-hover:scale-x-100 transition-transform"
          />
        </div>
      </div>
    </div>
  </div>
</template>

<script setup lang="ts">
import localStorageService from '~/services/localStorageService';
import type { Note } from '~/types/note'

// Notas mockadas para visualização
const notes = localStorageService.loadAll()

function openNote(note: any) {
  // TODO: Implementar navegação para a nota
  console.log('Opening note:', note)
}

function formatRelativeTime(date: string) {
  const now = new Date()
  const noteDate = new Date(date)
  const diffInHours = (now.getTime() - noteDate.getTime()) / (1000 * 60 * 60)
  
  if (diffInHours < 1) {
    return 'há alguns minutos'
  } else if (diffInHours < 24) {
    const hours = Math.floor(diffInHours)
    return `há ${hours} ${hours === 1 ? 'hora' : 'horas'}`
  } else if (diffInHours < 48) {
    return 'ontem'
  } else {
    return noteDate.toLocaleDateString('pt-BR', {
      day: '2-digit',
      month: '2-digit',
      year: '2-digit'
    })
  }
}

function isCode(content: string) {
  // Verifica se o conteúdo parece ser código
  return content?.includes('function') || 
         content?.includes('const ') || 
         content?.includes('let ') || 
         content?.includes('var ') ||
         content?.includes('{') ||
         content?.includes('=>')
}
</script>

<style>
/* Ajuste para emojis e código */
.whitespace-pre-line {
  word-break: break-word;
}

/* Ajuste para fonte monoespaçada */
.font-mono {
  font-family: ui-monospace, SFMono-Regular, Menlo, Monaco, Consolas, "Liberation Mono", "Courier New", monospace;
}
</style>
