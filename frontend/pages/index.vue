<template>
  <div class="min-h-screen flex flex-col relative px-4 md:px-0">
    <!-- Container central para melhor leitura -->
    <div class="w-full max-w-3xl mx-auto flex-grow">
      <!-- Editor área -->
      <n-input
        v-model:value="noteContent"
        type="textarea"
        :autosize="{ minRows: 1 }"
        class="editor-input mt-16 mb-32"
        placeholder="Comece a escrever..."
        :bordered="false"
        :autofocus="true"
      />
    </div>

    <!-- Botão fixo -->
    <div class="fixed bottom-0 left-0 right-0 flex justify-center pb-16 bg-gradient-to-t from-white via-white to-transparent h-40 pointer-events-none">
      <transition name="fade">
        <n-button
          v-if="noteContent"
          type="primary"
          class="shadow-2xl px-8 h-12 pointer-events-auto save-btn text-base font-medium tracking-wide"
          @click="saveNote"
        >
          Salvar
        </n-button>
      </transition>
    </div>
  </div>
</template>

<script setup lang="ts">
import localStorageService from '~/services/localStorageService';
import { type Note } from '~/types/note';
const noteContent = ref('')

function saveNote() {
  console.log('Salvando nota:', noteContent.value)
  localStorageService.save(
    Date.now().toPrecision(),
    {
      id: Date.now().toPrecision(),
      content: noteContent.value,
      createdAt: new Date().toISOString(),
    } as Note
  );
  // Limpar o conteúdo após salvar
  noteContent.value = '';
}
</script>

<style>
.editor-input {
  background: transparent !important;
}

.editor-input .n-input__textarea-el {
  font-family: 'Inter', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif;
  font-size: 1.25rem !important;
  line-height: 1.9 !important;
  padding: 0 !important;
  color: #000000 !important;
  letter-spacing: -0.01em !important;
  font-weight: 400 !important;
  resize: none !important;
}

.editor-input .n-input__textarea-el::placeholder {
  color: #000000 !important;
  opacity: 0.3;
  font-size: 1.25rem !important;
  font-weight: 400 !important;
}

/* Estilo do cursor */
.editor-input .n-input__textarea-el:focus {
  caret-color: #000000;
}

/* Animação para o botão de salvar */
.fade-enter-active,
.fade-leave-active {
  transition: opacity 0.3s ease, transform 0.3s ease;
}

.fade-enter-from,
.fade-leave-to {
  opacity: 0;
  transform: translateY(10px);
}

/* Esconde a scrollbar mas mantém a funcionalidade */
.editor-input .n-input__textarea-el {
  scrollbar-width: none;
  -ms-overflow-style: none;
}

.editor-input .n-input__textarea-el::-webkit-scrollbar {
  display: none;
}

/* Estilo especial para o botão de salvar */
.save-btn {
  backdrop-filter: blur(12px);
  background: rgba(0, 0, 0, 0.8) !important;
  border: 1px solid rgba(255, 255, 255, 0.1) !important;
  transition: all 0.3s ease !important;
}

.save-btn:hover {
  background: rgba(0, 0, 0, 0.9) !important;
  box-shadow: 0 20px 25px -5px rgba(0, 0, 0, 0.1), 0 10px 10px -5px rgba(0, 0, 0, 0.04) !important;
  transform: translateY(-1px);
}

/* Ajuste de largura máxima para melhor leitura */
@media (min-width: 768px) {
  .editor-input .n-input__textarea-el {
    font-size: 1.3rem !important;
    line-height: 2 !important;
  }
}
</style>
