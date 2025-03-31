<template>
  <div class="min-h-screen flex flex-col relative px-4 md:px-0">
    <div class="w-full max-w-3xl mx-auto flex-grow pt-24">
      <h1 class="text-2xl font-medium mb-8 text-black/90">Minhas Notas</h1>
      
      <!-- Lista de notas -->
      <div class="space-y-4">
        <div v-if="!notes.length" class="text-sm text-black/60">
          Nenhuma nota criada ainda
        </div>
        <div
          v-for="note in notes"
          :key="note.id"
          class="p-4 rounded-lg border border-black/10 hover:border-black/20 hover:bg-black/[0.02] cursor-pointer transition-all"
          @click="openNote(note)"
        >
          <div class="font-medium text-black/90">
            {{ note.title || 'Nota sem título' }}
          </div>
          <div class="text-sm text-black/70 mt-1 line-clamp-2">
            {{ note.content || 'Sem conteúdo' }}
          </div>
          <div class="text-xs text-black/50 mt-2">
            Atualizada em {{ formatDate(note.updatedAt) }}
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup lang="ts">
const notes = ref<any[]>([]) // TODO: Integrar com backend

function openNote(note: any) {
  // TODO: Implementar navegação para a nota
  console.log('Opening note:', note)
}

function formatDate(date: string) {
  return new Date(date).toLocaleDateString('pt-BR', {
    day: '2-digit',
    month: '2-digit',
    year: '2-digit',
    hour: '2-digit',
    minute: '2-digit'
  })
}
</script>
