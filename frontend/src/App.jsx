import { useState, useEffect } from "react"
import ReactMarkdown from 'react-markdown'

export default function App() {
  const [candidatos, setCandidatos] = useState([])
  const [loading, setLoading] = useState(true)
  const [vista, setVista] = useState("lista")
  const [seleccionados, setSeleccionados] = useState([])
  const [comparacion, setComparacion] = useState(null)
  const [loadingComparacion, setLoadingComparacion] = useState(false)
  const [analizando, setAnalizando] = useState(false)
  const [analisisTexto, setAnalisisTexto] = useState("")
  const [candidatoAnalisis, setCandidatoAnalisis] = useState(null)
  const [busqueda, setBusqueda] = useState("")

  useEffect(() => {
    fetch(`${import.meta.env.VITE_API_URL || ''}/api/candidatos/`)
      .then(res => res.json())
      .then(data => { setCandidatos(data); setLoading(false) })
      .catch(err => { console.error(err); setLoading(false) })
  }, [])

  const toggleSeleccion = (candidato) => {
    if (seleccionados.find(c => c.id === candidato.id)) {
      setSeleccionados(seleccionados.filter(c => c.id !== candidato.id))
    } else if (seleccionados.length < 2) {
      setSeleccionados([...seleccionados, candidato])
    }
  }

  const comparar = async () => {
    if (seleccionados.length !== 2) return
    setLoadingComparacion(true)
    setVista("comparar")
    setComparacion(null)
    setAnalisisTexto("")
    setAnalizando(true)

    const response = await fetch(
      `${import.meta.env.VITE_API_URL || ''}/api/ai/comparar/${seleccionados[0].id}/${seleccionados[1].id}`,
      { method: "POST" }
    )

    const reader = response.body.getReader()
    const decoder = new TextDecoder()
    while (true) {
      const { done, value } = await reader.read()
      if (done) break
      const chunk = decoder.decode(value)
      const lines = chunk.split("\n")
      for (const line of lines) {
        if (line.startsWith("data: ") && line !== "data: [DONE]") {
          try {
            const data = JSON.parse(line.replace("data: ", ""))
            setAnalisisTexto(prev => prev + data.texto)
          } catch {}
        }
      }
    }
    setAnalizando(false)
    setLoadingComparacion(false)
  }

  const analizarCandidato = async (candidato) => {
    setCandidatoAnalisis(candidato)
    setAnalizando(true)
    setAnalisisTexto("")
    setVista("analisis")
    const response = await fetch(
      `${import.meta.env.VITE_API_URL || ''}/api/ai/pros-contras/${candidato.id}`,
      { method: "POST" }
    )
    const reader = response.body.getReader()
    const decoder = new TextDecoder()
    while (true) {
      const { done, value } = await reader.read()
      if (done) break
      const chunk = decoder.decode(value)
      const lines = chunk.split("\n")
      for (const line of lines) {
        if (line.startsWith("data: ") && line !== "data: [DONE]") {
          try {
            const data = JSON.parse(line.replace("data: ", ""))
            setAnalisisTexto(prev => prev + data.texto)
          } catch {}
        }
      }
    }
    setAnalizando(false)
  }

  const volverALista = () => {
    setVista("lista")
    setComparacion(null)
    setAnalisisTexto("")
    setCandidatoAnalisis(null)
  }

  const candidatosFiltrados = candidatos.filter(c =>
    c.nombre.toLowerCase().includes(busqueda.toLowerCase()) ||
    c.partido.nombre.toLowerCase().includes(busqueda.toLowerCase())
  )

  const analizarViabilidad = async (candidato) => {
    setCandidatoAnalisis(candidato)
    setAnalizando(true)
    setAnalisisTexto("")
    setVista("analisis")
    const response = await fetch(
      `${import.meta.env.VITE_API_URL || ''}/api/ai/viabilidad/${candidato.id}`,
      { method: "POST" }
    )
    const reader = response.body.getReader()
    const decoder = new TextDecoder()
    while (true) {
      const { done, value } = await reader.read()
      if (done) break
      const chunk = decoder.decode(value)
      const lines = chunk.split("\n")
      for (const line of lines) {
        if (line.startsWith("data: ") && line !== "data: [DONE]") {
          try {
            const data = JSON.parse(line.replace("data: ", ""))
            setAnalisisTexto(prev => prev + data.texto)
          } catch {}
        }
      }
    }
    setAnalizando(false)
  }

  return (
    <div className="min-h-screen bg-gray-50">

      {/* Header */}
      <header className="bg-red-700 text-white py-6 px-8 shadow-lg">
        <div className="max-w-5xl mx-auto flex items-center justify-between">
          <div>
            <h1 className="text-3xl font-bold">VoxIA 🗳️</h1>
            <p className="text-red-200 text-sm mt-1">
              Análisis electoral inteligente · Elecciones Perú 2026
            </p>
          </div>
          {(vista === "comparar" || vista === "analisis") && (
            <button onClick={volverALista}
              className="bg-white text-red-700 px-4 py-2 rounded-lg font-medium hover:bg-red-50">
              ← Volver
            </button>
          )}
        </div>
      </header>

      <main className="max-w-5xl mx-auto px-8 py-8">

        {/* Vista: Lista */}
        {vista === "lista" && (
          <div>
            <div className="flex items-center justify-between mb-6">
              <h2 className="text-xl font-semibold text-gray-800">
                Candidatos presidenciales
              </h2>
              {seleccionados.length === 2 && (
                <button onClick={comparar}
                  className="bg-red-700 text-white px-6 py-2 rounded-lg font-medium hover:bg-red-800">
                  Comparar seleccionados →
                </button>
              )}
            </div>

            {/* Buscador */}
            <div className="mb-6">
              <input type="text"
                placeholder="Buscar por nombre o partido..."
                value={busqueda}
                onChange={(e) => setBusqueda(e.target.value)}
                className="w-full px-4 py-3 rounded-xl border border-gray-200 bg-white shadow-sm focus:outline-none focus:ring-2 focus:ring-red-400 text-gray-700"
              />
            </div>

            {/* Seleccionados */}
            {seleccionados.length > 0 && (
              <div className="bg-red-50 border border-red-200 rounded-lg p-4 mb-6">
                <p className="text-red-700 text-sm font-medium mb-2">
                  Seleccionados para comparar ({seleccionados.length}/2):
                </p>
                <div className="flex gap-2 flex-wrap">
                  {seleccionados.map(c => (
                    <span key={c.id} className="bg-red-700 text-white px-3 py-1 rounded-full text-sm flex items-center gap-2">
                      {c.foto_url && (
                        <img src={c.foto_url} alt={c.nombre}
                          className="w-5 h-5 rounded-full object-cover object-top" />
                      )}
                      {c.nombre}
                    </span>
                  ))}
                </div>
              </div>
            )}

            {/* Grid candidatos */}
            {loading ? (
              <p className="text-gray-500">Cargando candidatos...</p>
            ) : (
              <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-4">
                {candidatosFiltrados.map(candidato => {
                  const estaSeleccionado = seleccionados.find(c => c.id === candidato.id)
                  return (
                    <div key={candidato.id} onClick={() => toggleSeleccion(candidato)}
                      className={`bg-white rounded-xl overflow-hidden shadow-sm border-2 cursor-pointer transition-all
                        ${estaSeleccionado
                          ? "border-red-600"
                          : "border-gray-100 hover:border-red-300 hover:shadow-md"
                        }`}
                    >
                      {/* Foto */}
                      <div className="w-full h-48 bg-white overflow-hidden relative">
                        {candidato.foto_url ? (
                          <img
                            src={candidato.foto_url}
                            alt={candidato.nombre}
                            className="w-full h-full object-contain object-top"
                            onError={(e) => {
                              e.target.style.display = 'none'
                              e.target.parentElement.innerHTML += `<div class="w-full h-full flex items-center justify-center absolute inset-0"><span class="text-5xl font-bold text-red-200">${candidato.nombre.charAt(0)}</span></div>`
                            }}
                          />
                        ) : (
                          <div className="w-full h-full flex items-center justify-center bg-red-50">
                            <span className="text-5xl font-bold text-red-200">
                              {candidato.nombre.charAt(0)}
                            </span>
                          </div>
                        )}
                        {estaSeleccionado && (
                          <div className="absolute top-2 right-2 bg-red-600 text-white text-xs px-2 py-1 rounded-full font-bold">
                            ✓
                          </div>
                        )}
                      </div>

                      {/* Info */}
                      <div className="p-4">
                        <h3 className="font-semibold text-gray-900 text-sm text-center mb-2 leading-tight">
                          {candidato.nombre}
                        </h3>
                        <div className="flex items-center justify-center gap-2 mb-3">
                          {candidato.partido.logo_url && (
                            <img
                              src={candidato.partido.logo_url}
                              alt={candidato.partido.nombre}
                              className="w-6 h-6 object-contain flex-shrink-0"
                              onError={(e) => e.target.style.display = 'none'}
                            />
                          )}
                          <p className="text-xs text-gray-500 text-center leading-tight">
                            {candidato.partido.nombre}
                          </p>
                        </div>
                        <button
                          onClick={(e) => { e.stopPropagation(); analizarCandidato(candidato) }}
                          className="w-full text-xs bg-gray-800 text-white py-2 rounded-lg hover:bg-gray-700">
                          Analizar con IA →
                        </button>
                        <button
                          onClick={(e) => { e.stopPropagation(); analizarViabilidad(candidato) }}
                          className="w-full text-xs bg-red-700 text-white py-2 rounded-lg hover:bg-red-800 mt-2">
                          Verificar viabilidad →
                        </button>
                      </div>
                    </div>
                  )
                })}
              </div>
            )}
            <p className="text-gray-400 text-sm mt-6 text-center">
              Selecciona dos candidatos para compararlos · VoxIA no recomienda votos
            </p>
          </div>
        )}

        {/* Vista: Comparación */}
        {vista === "comparar" && (
          <div>
            {/* Header con los dos candidatos */}
            <div className="grid grid-cols-3 gap-4 mb-6">
              <div className="bg-white rounded-xl p-4 shadow-sm flex flex-col items-center text-center">
                {seleccionados[0]?.foto_url && (
                  <img src={seleccionados[0].foto_url}
                    className="w-20 h-20 object-contain object-top mb-2" />
                )}
                <p className="font-semibold text-red-700 text-sm">{seleccionados[0]?.nombre}</p>
                <p className="text-xs text-gray-500 mt-1">{seleccionados[0]?.partido?.nombre}</p>
              </div>
              <div className="flex items-center justify-center font-bold text-2xl text-gray-300">
                VS
              </div>
              <div className="bg-white rounded-xl p-4 shadow-sm flex flex-col items-center text-center">
                {seleccionados[1]?.foto_url && (
                  <img src={seleccionados[1].foto_url}
                    className="w-20 h-20 object-contain object-top mb-2" />
                )}
                <p className="font-semibold text-red-700 text-sm">{seleccionados[1]?.nombre}</p>
                <p className="text-xs text-gray-500 mt-1">{seleccionados[1]?.partido?.nombre}</p>
              </div>
            </div>

            {/* Resultado IA */}
            <div className="bg-white rounded-xl shadow-sm p-6">
              <div className="flex items-center gap-2 mb-4">
                <span className="bg-red-100 text-red-700 text-xs px-3 py-1 rounded-full font-medium">
                  Generado por Claude AI
                </span>
                <span className="text-gray-400 text-xs">
                  Análisis informativo — no constituye recomendación de voto
                </span>
              </div>
              {loadingComparacion && analisisTexto === "" && (
                <p className="text-gray-400 animate-pulse">Claude está comparando...</p>
              )}
              <div className="prose prose-sm max-w-none text-gray-700">
                <ReactMarkdown
                  components={{
                    h2: ({children}) => (
                      <h2 className="text-lg font-semibold text-gray-900 mt-6 mb-3 border-b border-gray-100 pb-2">
                        {children}
                      </h2>
                    ),
                    h3: ({children}) => (
                      <h3 className="text-base font-medium text-red-700 mt-4 mb-2">
                        {children}
                      </h3>
                    ),
                    strong: ({children}) => (
                      <strong className="font-semibold text-gray-900">{children}</strong>
                    ),
                    p: ({children}) => (
                      <p className="text-sm text-gray-700 leading-relaxed mb-3">{children}</p>
                    ),
                    ul: ({children}) => (
                      <ul className="list-disc list-inside text-sm text-gray-700 mb-3 space-y-1">
                        {children}
                      </ul>
                    ),
                    li: ({children}) => (
                      <li className="text-sm text-gray-700">{children}</li>
                    ),
                  }}
                >
                  {analisisTexto}
                </ReactMarkdown>
              </div>
              {analizando && (
                <span className="inline-block w-2 h-4 bg-red-600 animate-pulse ml-1" />
              )}
            </div>
          </div>
        )}

        {/* Vista: Análisis IA */}
        {vista === "analisis" && (
          <div>
            <div className="flex items-center gap-4 mb-6 bg-white rounded-xl p-4 shadow-sm">
              {candidatoAnalisis?.foto_url && (
                <img src={candidatoAnalisis.foto_url}
                  alt={candidatoAnalisis.nombre}
                  className="w-20 h-20 rounded-full object-cover object-center shadow border-2 border-red-100"
                />
              )}
              <div>
                <h2 className="text-xl font-semibold text-gray-800">
                  {candidatoAnalisis?.nombre}
                </h2>
                <div className="flex items-center gap-2 mt-1">
                  {candidatoAnalisis?.partido?.logo_url && (
                    <img src={candidatoAnalisis.partido.logo_url}
                      alt={candidatoAnalisis.partido.nombre}
                      className="w-6 h-6 object-contain"
                    />
                  )}
                  <p className="text-sm text-gray-500">
                    {candidatoAnalisis?.partido?.nombre}
                  </p>
                </div>
              </div>
            </div>

            <div className="bg-white rounded-xl shadow-sm p-6">
              <div className="flex items-center gap-2 mb-4 flex-wrap">
                <span className="bg-red-100 text-red-700 text-xs px-3 py-1 rounded-full font-medium">
                  Generado por Claude AI
                </span>
                <span className="text-gray-400 text-xs">
                  Este análisis es informativo — no constituye recomendación de voto
                </span>
              </div>
              {analizando && analisisTexto === "" && (
                <p className="text-gray-400 animate-pulse">Claude está analizando...</p>
              )}
              <div className="prose prose-sm max-w-none text-gray-700">
                <ReactMarkdown
                  components={{
                    h2: ({children}) => (
                      <h2 className="text-lg font-semibold text-gray-900 mt-6 mb-3 flex items-center gap-2 border-b border-gray-100 pb-2">
                        {children}
                      </h2>
                    ),
                    h3: ({children}) => (
                      <h3 className="text-base font-medium text-gray-800 mt-4 mb-2">
                        {children}
                      </h3>
                    ),
                    strong: ({children}) => (
                      <strong className="font-semibold text-gray-900">{children}</strong>
                    ),
                    p: ({children}) => (
                      <p className="text-sm text-gray-700 leading-relaxed mb-3">{children}</p>
                    ),
                    ul: ({children}) => (
                      <ul className="list-disc list-inside text-sm text-gray-700 mb-3 space-y-1">
                        {children}
                      </ul>
                    ),
                    li: ({children}) => (
                      <li className="text-sm text-gray-700 leading-relaxed">{children}</li>
                    ),
                    hr: () => <hr className="border-gray-100 my-4" />,
                  }}
                >
                  {analisisTexto}
                </ReactMarkdown>
              </div>
              {analizando && (
                <span className="inline-block w-2 h-4 bg-red-600 animate-pulse ml-1" />
              )}
            </div>
          </div>
        )}

      </main>
    </div>
  )
}
