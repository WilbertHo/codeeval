(ns clj.core
  (:gen-class))

(defn fizzbuzz
  [x]
  (let [s (str (if (zero? (mod x 3)) "Fizz")
               (if (zero? (mod x 5)) "Buzz"))]
    (if (empty? s) x s)))

(defn -main
  [& args]
  (println (map fizzbuzz (range 1 101))))
