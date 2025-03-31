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
              <h3 class="font-medium text-black/90 text-lg mb-1">
                {{ note.title || 'Nota sem título' }}
              </h3>
              <div class="text-xs text-black/50">
                Atualizada {{ formatRelativeTime(note.updatedAt) }}
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
// Notas mockadas para visualização
const notes = ref([
  {
    id: 1,
    title: 'Ideias para o Projeto',
    content: 'Implementar autenticação com Google\nAdicionar suporte a markdown\nCriar sistema de tags\nAdicionar busca em tempo real\nIntegrar com API de IA para sugestões',
    updatedAt: '2025-03-30T22:45:00'
  },
  {
    id: 2,
    title: 'Lista de Compras',
    content: '🥖 Pão\n🥛 Leite\n🍎 Maçãs\n🧀 Queijo\n🥚 Ovos',
    updatedAt: '2025-03-30T20:30:00'
  },
  {
    id: 3,
    title: 'Reunião - Planejamento Q2',
    content: '1. Revisão das metas do Q1\n2. Definição dos OKRs para Q2\n3. Distribuição de responsabilidades\n4. Próximos passos',
    updatedAt: '2025-03-30T15:20:00'
  },
  {
    id: 4,
    content: 'Lembrar de agendar consulta médica para a próxima semana. Ligar no número (11) 9999-9999.',
    updatedAt: '2025-03-30T12:15:00'
  },
  {
    id: 5,
    title: 'Citações Favoritas',
    content: '"A simplicidade é o último grau de sofisticação" - Leonardo da Vinci\n\n"Menos é mais" - Ludwig Mies van der Rohe',
    updatedAt: '2025-03-29T18:40:00'
  },
  {
    id: 6,
    title: 'Recursos de UX/UI',
    content: '• Princípios de Design\n• Paleta de cores monocromática\n• Tipografia consistente\n• Micro-interações\n• Feedback visual\n• Animações sutis',
    updatedAt: '2025-03-29T14:10:00'
  },
  {
    id: 7,
    title: 'Snippet: Função Auxiliar',
    content: 'function formatDate(date) {\n  return new Date(date)\n    .toLocaleDateString("pt-BR")\n}',
    updatedAt: '2025-03-29T10:20:00'
  }
])

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
