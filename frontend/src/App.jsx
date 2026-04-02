import { useState, useEffect } from "react"

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
    const res = await fetch(
      `${import.meta.env.VITE_API_URL || ''}/api/comparar/?a=${seleccionados[0].id}&b=${seleccionados[1].id}`
    )
    const data = await res.json()
    setComparacion(data)
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
                          className="w-5 h-5 rounded-full object-cover" />
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
                      className={`bg-white rounded-xl p-5 shadow-sm border-2 cursor-pointer transition-all
                        ${estaSeleccionado
                          ? "border-red-600 bg-red-50"
                          : "border-gray-100 hover:border-red-300 hover:shadow-md"
                        }`}
                    >
                      {/* Foto candidato */}
                      <div className="w-20 h-20 rounded-full overflow-hidden mb-3 bg-red-100 mx-auto">
                        {candidato.foto_url ? (
                          <img src={candidato.foto_url} alt={candidato.nombre}
                            className="w-full h-full object-cover object-top"
                            onError={(e) => {
                              e.target.style.display = 'none'
                              e.target.parentElement.innerHTML = `<div class="w-full h-full flex items-center justify-center"><span class="text-2xl font-bold text-red-700">${candidato.nombre.charAt(0)}</span></div>`
                            }}
                          />
                        ) : (
                          <div className="w-full h-full flex items-center justify-center">
                            <span className="text-2xl font-bold text-red-700">
                              {candidato.nombre.charAt(0)}
                            </span>
                          </div>
                        )}
                      </div>

                      {/* Nombre */}
                      <h3 className="font-semibold text-gray-900 text-center text-sm">
                        {candidato.nombre}
                      </h3>

                      {/* Partido con logo */}
                      <div className="flex items-center justify-center gap-2 mt-2">
                        {candidato.partido.logo_url && (
                          <img src={candidato.partido.logo_url}
                            alt={candidato.partido.nombre}
                            className="w-6 h-6 object-contain"
                            onError={(e) => e.target.style.display = 'none'}
                          />
                        )}
                        <p className="text-xs text-gray-500 text-center">
                          {candidato.partido.nombre}
                        </p>
                      </div>

                      {estaSeleccionado && (
                        <div className="mt-2 text-center">
                          <span className="text-xs bg-red-600 text-white px-2 py-1 rounded-full">
                            ✓ Seleccionado
                          </span>
                        </div>
                      )}

                      {/* Botón IA */}
                      <button
                        onClick={(e) => { e.stopPropagation(); analizarCandidato(candidato) }}
                        className="mt-3 w-full text-xs bg-gray-800 text-white py-1.5 rounded-lg hover:bg-gray-700">
                        Analizar con IA →
                      </button>
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
            <h2 className="text-xl font-semibold text-gray-800 mb-6">
              Comparación de propuestas
            </h2>
            {loadingComparacion ? (
              <p className="text-gray-500">Cargando comparación...</p>
            ) : comparacion && (
              <div>
                <div className="grid grid-cols-3 gap-4 mb-6">
                  <div className="text-center font-semibold text-red-700 bg-red-50 rounded-lg p-3">
                    {comparacion.candidato_a.nombre}
                    <p className="text-xs text-gray-500 font-normal mt-1">
                      {comparacion.candidato_a.partido}
                    </p>
                  </div>
                  <div className="text-center font-bold text-gray-400 flex items-center justify-center">
                    VS
                  </div>
                  <div className="text-center font-semibold text-red-700 bg-red-50 rounded-lg p-3">
                    {comparacion.candidato_b.nombre}
                    <p className="text-xs text-gray-500 font-normal mt-1">
                      {comparacion.candidato_b.partido}
                    </p>
                  </div>
                </div>
                {Object.entries(comparacion.comparacion).map(([tema, props]) => (
                  <div key={tema} className="mb-4 bg-white rounded-xl shadow-sm overflow-hidden">
                    <div className="bg-gray-800 text-white px-5 py-3 font-medium">
                      {tema}
                    </div>
                    <div className="grid grid-cols-2 divide-x divide-gray-100">
                      <div className="p-4">
                        {props.a.map((p, i) => (
                          <p key={i} className="text-sm text-gray-700">{p}</p>
                        ))}
                      </div>
                      <div className="p-4">
                        {props.b.map((p, i) => (
                          <p key={i} className="text-sm text-gray-700">{p}</p>
                        ))}
                      </div>
                    </div>
                  </div>
                ))}
              </div>
            )}
          </div>
        )}

        {/* Vista: Análisis IA */}
        {vista === "analisis" && (
          <div>
            {/* Header del análisis con foto */}
            <div className="flex items-center gap-4 mb-6">
              {candidatoAnalisis?.foto_url && (
                <img src={candidatoAnalisis.foto_url}
                  alt={candidatoAnalisis.nombre}
                  className="w-16 h-16 rounded-full object-cover object-top shadow"
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
                      className="w-5 h-5 object-contain"
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
                <p className="text-gray-400 animate-pulse">
                  Claude está analizando...
                </p>
              )}
              <pre className="whitespace-pre-wrap font-sans text-gray-700 leading-relaxed text-sm">
                {analisisTexto}
              </pre>
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
