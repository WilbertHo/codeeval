(ns clj.core
  ; (:require [clojure.string :as str])
  (:gen-class))

(defn fizzbuzz
  [fizz buzz x]
  (let [s (str (if (zero?
                 (mod x fizz))
                 "F")
               (if (zero?
                 (mod x buzz))
                 "B"))]
    (if (empty? s)
      x
      s)))

(defn -main
  [& args]
  (doseq [line (line-seq (java.io.BufferedReader.
                           (if (> (count *command-line-args*) 0)
                             (java.io.FileReader. (first *command-line-args*))
                             *in*)))]
    (let [[fizz buzz end] (map read-string (clojure.string/split line #"\s+"))]
      (apply println (map (partial fizzbuzz fizz buzz) (range 1 (+ end 1)))))))
