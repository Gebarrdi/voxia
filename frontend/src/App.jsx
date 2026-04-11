import { useState, useEffect } from "react"
import ReactMarkdown from 'react-markdown'
import remarkGfm from 'remark-gfm'

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
  const [temaExpandido, setTemaExpandido] = useState(null)
  const [analisisTecnico, setAnalisisTecnico] = useState("")
  const [loadingTecnico, setLoadingTecnico] = useState(false)

  useEffect(() => {
    fetch(`${import.meta.env.VITE_API_URL || ''}/api/candidatos/`)
      .then(res => res.json())
      .then(data => { setCandidatos(data); setLoading(false) })
      .catch(err => { console.error(err); setLoading(false) })
  }, [])

  const limpiarMarkdown = (texto) => {
    if (!texto) return texto
    let limpio = texto

    const matchEncabezado = limpio.match(/^(#{1,3} )/m)
    if (matchEncabezado) {
      const idx = limpio.indexOf(matchEncabezado[0])
      if (idx > 0) {
        const antesDelEncabezado = limpio.substring(0, idx)
        const tieneIntro = /voy a|busco|ahora busco|permíteme|let me|procedo|realiz|analiz|necesito buscar|a continuación|procedere/i.test(antesDelEncabezado)
        if (tieneIntro) {
          limpio = limpio.substring(idx).trim()
        }
      }
    }

    limpio = limpio.replace(/^([-*])\s*\n+(\*\*)/gm, '$1 $2')
    limpio = limpio.replace(/^([-*])\s*\n+([^\n\-*#>])/gm, '$1 $2')
    limpio = limpio.replace(/^[-*]\s*$/gm, '')
    limpio = limpio.replace(/^---+\s*$/gm, '')
    limpio = limpio.replace(/\n{3,}/g, '\n\n')

    return limpio.trim()
  }

  const textoListo = (texto) => {
    const limpio = limpiarMarkdown(texto)
    return limpio && /#{1,3} /.test(limpio) ? limpio : null
  }

  // ── Helper: POST a un endpoint JSON con timeout ───────────────────────────
  const fetchJSON = async (url, timeoutMs = 300000) => {
    const controller = new AbortController()
    const timeoutId = setTimeout(() => controller.abort(), timeoutMs)
    try {
      const response = await fetch(url, {
        method: "POST",
        signal: controller.signal
      })
      clearTimeout(timeoutId)
      if (!response.ok) throw new Error(`HTTP ${response.status}`)
      return await response.json()
    } catch (err) {
      clearTimeout(timeoutId)
      if (err.name === 'AbortError') {
        console.warn('Request abortado por timeout')
      } else {
        console.error('Error en fetch:', err)
      }
      return null
    }
  }

  const getNombreCorto = (nombre) => {
    const p = nombre.split(" ")
    const segundosNombres = [
      "Soledad", "Gonsalo", "Jorge", "Helbert",
      "Bernardo", "Pablo", "Ernesto", "Patrick",
      "Fernando", "Antonio", "Enrique", "Gilmer",
      "Carlos", "Darwin", "Alfonso", "Joaquin",
      "Roy", "Mario", "Davis", "Leon"
    ]
    if (p.length >= 3 && segundosNombres.includes(p[1])) {
      return `${p[0]} ${p[2]}`
    }
    return `${p[0]} ${p[1]}`
  }

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
    setAnalisisTecnico("")
    setAnalizando(true)
    setTemaExpandido(null)

    const data = await fetchJSON(
      `${import.meta.env.VITE_API_URL || ''}/api/ai/comparar/${seleccionados[0].id}/${seleccionados[1].id}`
    )
    if (data) setComparacion(data)

    setAnalizando(false)
    setLoadingComparacion(false)
  }

  const verAnalisisTecnico = async () => {
    if (loadingTecnico || analisisTecnico) return
    setLoadingTecnico(true)
    setAnalisisTecnico("")

    const data = await fetchJSON(
      `${import.meta.env.VITE_API_URL || ''}/api/ai/analisis-tecnico/${seleccionados[0].id}/${seleccionados[1].id}`
    )
    if (data?.texto) setAnalisisTecnico(data.texto)

    setLoadingTecnico(false)
  }

  const analizarCandidato = async (candidato) => {
    setCandidatoAnalisis(candidato)
    setAnalizando(true)
    setAnalisisTexto("")
    setVista("analisis")

    const data = await fetchJSON(
      `${import.meta.env.VITE_API_URL || ''}/api/ai/pros-contras/${candidato.id}`
    )
    if (data?.texto) setAnalisisTexto(data.texto)

    setAnalizando(false)
  }

  const analizarViabilidad = async (candidato) => {
    setCandidatoAnalisis(candidato)
    setAnalizando(true)
    setAnalisisTexto("")
    setVista("analisis")

    const data = await fetchJSON(
      `${import.meta.env.VITE_API_URL || ''}/api/ai/viabilidad/${candidato.id}`
    )
    if (data?.texto) setAnalisisTexto(data.texto)

    setAnalizando(false)
  }

  const volverALista = () => {
    setVista("lista")
    setComparacion(null)
    setAnalisisTexto("")
    setAnalisisTecnico("")
    setCandidatoAnalisis(null)
    setTemaExpandido(null)
  }

  const candidatosFiltrados = candidatos.filter(c =>
    c.nombre.toLowerCase().includes(busqueda.toLowerCase()) ||
    c.partido.nombre.toLowerCase().includes(busqueda.toLowerCase())
  )

  const limpiarCitas = (texto) => {
    if (!texto) return texto
    return texto
      .replace(/<cite[^>]*>/g, '')
      .replace(/<\/cite>/g, '')
      .replace(/\\u003ccite[^>]*>/g, '')
      .replace(/\\u003c\/cite>/g, '')
  }

  const mdComponents = {
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
    p: ({children, node}) => {
      if (node?.parent?.tagName === 'li') {
        return <span className="text-sm text-gray-700 leading-relaxed">{children}</span>
      }
      return <p className="text-sm text-gray-700 leading-relaxed mb-3">{children}</p>
    },
    ul: ({children}) => {
      const filtered = Array.isArray(children)
        ? children.filter(c => c && c !== '\n')
        : children
      return (
        <ul className="list-disc list-inside text-sm text-gray-700 mb-3 space-y-1">
          {filtered}
        </ul>
      )
    },
    li: ({children}) => {
      const content = Array.isArray(children)
        ? children.filter(c => c && c !== '\n')
        : children

      if (!content || (Array.isArray(content) && content.length === 0)) {
        return null
      }

      return (
        <li className="text-sm text-gray-700 leading-relaxed">
          {content}
        </li>
      )
    },
  }

  const iconosTema = {
    "Economía": "💰",
    "Seguridad": "🔒",
    "Educación": "📚",
    "Salud": "🏥",
    "Transporte": "🚆",
    "Medio Ambiente": "🌿",
    "Corrupción": "⚖️",
  }

  const BarraComparacion = ({ tema, datos, nombreA, nombreB }) => {
    const pA = datos.puntaje_a
    const pB = datos.puntaje_b
    const ganador = datos.ganador

    return (
      <div className="bg-white rounded-xl shadow-sm overflow-hidden mb-3">
        <div className="px-5 py-3 bg-gray-50 border-b border-gray-100 flex items-center justify-between">
          <div className="flex items-center gap-2">
            <span className="text-lg">{iconosTema[tema] || "📊"}</span>
            <span className="font-semibold text-gray-800">{tema}</span>
          </div>
          {ganador === "A" && (
            <span className="text-xs bg-blue-100 text-blue-700 px-2 py-1 rounded-full font-medium">
              🏆 Ventaja: {getNombreCorto(nombreA)}
            </span>
          )}
          {ganador === "B" && (
            <span className="text-xs bg-red-100 text-red-700 px-2 py-1 rounded-full font-medium">
              🏆 Ventaja: {getNombreCorto(nombreB)}
            </span>
          )}
          {ganador === "empate" && (
            <span className="text-xs bg-gray-100 text-gray-600 px-2 py-1 rounded-full font-medium">
              🤝 Empate
            </span>
          )}
        </div>

        <div className="px-5 py-4">
          <div className="mb-3">
            <div className="flex items-center justify-between mb-1">
              <span className="text-xs font-medium text-gray-600 truncate max-w-48">
                {getNombreCorto(nombreA)}
              </span>
              <span className="text-xs font-bold text-blue-600 ml-2">
                {pA}/10
              </span>
            </div>
            <div className="w-full bg-gray-100 rounded-full h-6 relative">
              <div
                className="bg-blue-500 h-6 rounded-full transition-all duration-500 flex items-center justify-end pr-2"
                style={{ width: `${pA * 10}%` }}
              >
                {pA >= 3 && (
                  <span className="text-white text-xs font-bold">{pA}</span>
                )}
              </div>
            </div>
          </div>

          <div className="mb-3">
            <div className="flex items-center justify-between mb-1">
              <span className="text-xs font-medium text-gray-600 truncate max-w-48">
                {getNombreCorto(nombreB)}
              </span>
              <span className="text-xs font-bold text-red-600 ml-2">
                {pB}/10
              </span>
            </div>
            <div className="w-full bg-gray-100 rounded-full h-6 relative">
              <div
                className="bg-red-500 h-6 rounded-full transition-all duration-500 flex items-center justify-end pr-2"
                style={{ width: `${pB * 10}%` }}
              >
                {pB >= 3 && (
                  <span className="text-white text-xs font-bold">{pB}</span>
                )}
              </div>
            </div>
          </div>

          <div className="grid grid-cols-2 gap-3 mt-3 text-xs text-gray-600">
            <div className="bg-blue-50 rounded-lg p-2">
              <p className="font-medium text-blue-700 mb-1">
                {getNombreCorto(nombreA)}:
              </p>
              <p className="leading-relaxed">
                {limpiarCitas(datos.resumen_a)}
              </p>
            </div>
            <div className="bg-red-50 rounded-lg p-2">
              <p className="font-medium text-red-700 mb-1">
                {getNombreCorto(nombreB)}:
              </p>
              <p className="leading-relaxed">
                {limpiarCitas(datos.resumen_b)}
              </p>
            </div>
          </div>
        </div>
      </div>
    )
  }

  return (
    <div className="min-h-screen bg-gray-50">

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

            <div className="mb-6">
              <input type="text"
                placeholder="Buscar por nombre o partido..."
                value={busqueda}
                onChange={(e) => setBusqueda(e.target.value)}
                className="w-full px-4 py-3 rounded-xl border border-gray-200 bg-white shadow-sm focus:outline-none focus:ring-2 focus:ring-red-400 text-gray-700"
              />
            </div>

            {seleccionados.length > 0 && (
              <div className="bg-red-50 border border-red-200 rounded-lg p-4 mb-6">
                <p className="text-red-700 text-sm font-medium mb-2">
                  Seleccionados para comparar ({seleccionados.length}/2):
                </p>
                <div className="flex gap-2 flex-wrap">
                  {seleccionados.map(c => (
                    <span key={c.id}
                      className="bg-red-700 text-white px-3 py-1 rounded-full text-sm flex items-center gap-2">
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

            {loading ? (
              <p className="text-gray-500">Cargando candidatos...</p>
            ) : (
              <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-4">
                {candidatosFiltrados.map(candidato => {
                  const estaSeleccionado = seleccionados.find(
                    c => c.id === candidato.id
                  )
                  return (
                    <div key={candidato.id}
                      onClick={() => toggleSeleccion(candidato)}
                      className={`bg-white rounded-xl overflow-hidden shadow-sm border-2 cursor-pointer transition-all
                        ${estaSeleccionado
                          ? "border-red-600"
                          : "border-gray-100 hover:border-red-300 hover:shadow-md"
                        }`}
                    >
                      <div className="w-full h-48 bg-white overflow-hidden relative">
                        {candidato.foto_url ? (
                          <img src={candidato.foto_url}
                            alt={candidato.nombre}
                            className="w-full h-full object-contain object-top"
                            onError={(e) => { e.target.style.display = 'none' }}
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
                      <div className="p-4">
                        <h3 className="font-semibold text-gray-900 text-sm text-center mb-2 leading-tight">
                          {candidato.nombre}
                        </h3>
                        <div className="flex items-center justify-center gap-2 mb-3">
                          {candidato.partido.logo_url && (
                            <img src={candidato.partido.logo_url}
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
                          onClick={(e) => {
                            e.stopPropagation()
                            analizarCandidato(candidato)
                          }}
                          className="w-full text-xs bg-gray-800 text-white py-2 rounded-lg hover:bg-gray-700">
                          Análisis de candidato y plan de gobierno →
                        </button>
                        <button
                          onClick={(e) => {
                            e.stopPropagation()
                            analizarViabilidad(candidato)
                          }}
                          className="w-full text-xs bg-red-700 text-white py-2 rounded-lg hover:bg-red-800 mt-2">
                          Viabilidad de plan de gobierno →
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
            <div className="grid grid-cols-3 gap-4 mb-6">
              <div className="bg-white rounded-xl p-4 shadow-sm flex flex-col items-center text-center border-t-4 border-blue-500">
                {seleccionados[0]?.foto_url && (
                  <img src={seleccionados[0].foto_url}
                    alt={seleccionados[0].nombre}
                    className="w-24 h-24 object-contain object-top mb-2" />
                )}
                <p className="font-semibold text-blue-700 text-sm">
                  {seleccionados[0]?.nombre}
                </p>
                <div className="flex items-center gap-1 mt-1">
                  {seleccionados[0]?.partido?.logo_url && (
                    <img src={seleccionados[0].partido.logo_url}
                      className="w-4 h-4 object-contain" />
                  )}
                  <p className="text-xs text-gray-500">
                    {seleccionados[0]?.partido?.nombre}
                  </p>
                </div>
                {comparacion && (
                  <div className="mt-2 bg-blue-50 rounded-lg px-3 py-1">
                    <span className="text-lg font-bold text-blue-600">
                      {comparacion.puntaje_total_a}
                    </span>
                    <span className="text-xs text-gray-500"> pts</span>
                  </div>
                )}
              </div>

              <div className="flex flex-col items-center justify-center">
                <span className="font-bold text-2xl text-gray-300">VS</span>
                {comparacion && (
                  <div className="mt-2 text-center">
                    {comparacion.ganador_general === "A" ? (
                      <div className="bg-blue-100 text-blue-700 text-xs px-3 py-1 rounded-full font-bold">
                        🏆 Gana {getNombreCorto(seleccionados[0]?.nombre || "")}
                      </div>
                    ) : comparacion.ganador_general === "B" ? (
                      <div className="bg-red-100 text-red-700 text-xs px-3 py-1 rounded-full font-bold">
                        🏆 Gana {getNombreCorto(seleccionados[1]?.nombre || "")}
                      </div>
                    ) : (
                      <div className="bg-gray-100 text-gray-600 text-xs px-3 py-1 rounded-full font-bold">
                        🤝 Empate
                      </div>
                    )}
                  </div>
                )}
              </div>

              <div className="bg-white rounded-xl p-4 shadow-sm flex flex-col items-center text-center border-t-4 border-red-500">
                {seleccionados[1]?.foto_url && (
                  <img src={seleccionados[1].foto_url}
                    alt={seleccionados[1].nombre}
                    className="w-24 h-24 object-contain object-top mb-2" />
                )}
                <p className="font-semibold text-red-700 text-sm">
                  {seleccionados[1]?.nombre}
                </p>
                <div className="flex items-center gap-1 mt-1">
                  {seleccionados[1]?.partido?.logo_url && (
                    <img src={seleccionados[1].partido.logo_url}
                      className="w-4 h-4 object-contain" />
                  )}
                  <p className="text-xs text-gray-500">
                    {seleccionados[1]?.partido?.nombre}
                  </p>
                </div>
                {comparacion && (
                  <div className="mt-2 bg-red-50 rounded-lg px-3 py-1">
                    <span className="text-lg font-bold text-red-600">
                      {comparacion.puntaje_total_b}
                    </span>
                    <span className="text-xs text-gray-500"> pts</span>
                  </div>
                )}
              </div>
            </div>

            {loadingComparacion && !comparacion && (
              <div className="bg-white rounded-xl p-8 text-center shadow-sm">
                <p className="text-gray-400 animate-pulse text-sm">
                  Claude está analizando los planes de gobierno...
                </p>
              </div>
            )}

            {comparacion && (
              <div>
                <div className="flex items-center gap-2 mb-4">
                  <span className="bg-red-100 text-red-700 text-xs px-3 py-1 rounded-full font-medium">
                    Generado por Claude AI
                  </span>
                  <span className="text-gray-400 text-xs">
                    Análisis informativo — no constituye recomendación de voto
                  </span>
                </div>

                {Object.entries(comparacion.temas).map(([tema, datos]) => (
                  <BarraComparacion
                    key={tema}
                    tema={tema}
                    datos={datos}
                    nombreA={seleccionados[0]?.nombre || ""}
                    nombreB={seleccionados[1]?.nombre || ""}
                  />
                ))}

                {comparacion.resumen_ganador && (
                  <div className="bg-white rounded-xl shadow-sm p-4 mt-4 border-l-4 border-yellow-400">
                    <p className="text-sm text-gray-700 leading-relaxed">
                      {limpiarCitas(comparacion.resumen_ganador)}
                    </p>
                    <p className="text-xs text-gray-400 mt-2 italic">
                      {comparacion.nota_neutralidad}
                    </p>
                  </div>
                )}

                <div className="mt-6 bg-white rounded-xl shadow-sm p-6">
                  <div className="flex items-center justify-between mb-4">
                    <h3 className="font-semibold text-gray-800 text-base">
                      🎓 Análisis técnico completo
                    </h3>
                    {!analisisTecnico && !loadingTecnico && (
                      <button
                        onClick={verAnalisisTecnico}
                        className="bg-gray-800 text-white text-xs px-4 py-2 rounded-lg hover:bg-gray-700"
                      >
                        Generar análisis técnico →
                      </button>
                    )}
                  </div>

                  {!analisisTecnico && !loadingTecnico && (
                    <p className="text-sm text-gray-400">
                      Análisis técnico riguroso por tema con datos
                      estadísticos, comparaciones internacionales
                      y evaluación de antecedentes. Se genera bajo demanda.
                    </p>
                  )}

                  {loadingTecnico && !textoListo(analisisTecnico) && (
                    <p className="text-gray-400 animate-pulse text-sm">
                      Claude está redactando el análisis técnico...
                    </p>
                  )}

                  {textoListo(analisisTecnico) && (
                    <div className="prose prose-sm max-w-none">
                      <ReactMarkdown
                        components={mdComponents}
                        remarkPlugins={[remarkGfm]}
                      >
                        {textoListo(analisisTecnico)}
                      </ReactMarkdown>
                    </div>
                  )}
                </div>
              </div>
            )}
          </div>
        )}

        {/* Vista: Análisis IA */}
        {vista === "analisis" && (
          <div>
            <div className="flex items-center gap-4 mb-6 bg-white rounded-xl p-4 shadow-sm">
              {candidatoAnalisis?.foto_url && (
                <img src={candidatoAnalisis.foto_url}
                  alt={candidatoAnalisis.nombre}
                  className="w-20 h-20 object-contain object-top shadow border-2 border-red-100 rounded-lg"
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

              {analizando && (
                <p className="text-gray-400 animate-pulse">
                  Claude está analizando...
                </p>
              )}

              {!analizando && textoListo(analisisTexto) && (
                <div className="prose prose-sm max-w-none">
                  <ReactMarkdown
                    components={mdComponents}
                    remarkPlugins={[remarkGfm]}
                  >
                    {textoListo(analisisTexto)}
                  </ReactMarkdown>
                </div>
              )}
            </div>
          </div>
        )}

      </main>
    </div>
  )
}
