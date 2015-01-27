(ns clj.core
  (:gen-class))

(defn -main
  "Multiplication table 1 to 12"
  [& args]
  (dotimes [n 12]
    (println
      (map
        (fn [x]
          (format "%4d" (* (inc n) x)))
        (range 1 13)
      )
    )
  )
)
